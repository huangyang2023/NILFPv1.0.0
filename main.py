# Nano-induced Lung Fibrosis Prediction (NILFP v1.0.0) is a Python package containing tools for predicting in vivo lung fibrosis using in vitro and in chemico data.
# Copyright (C) <2023> <Yang Huang> 
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General 
# Public License as published by the Free Software Foundation, either version 3 of the License, or (at your 
# option) any later version. This program is distributed in the hope that it will be useful, but WITHOUT ANY 
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details. You should have received a copy of the GNU General Public License 
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import pandas as pd
# import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
import tkinter as tk
from tkinter import ttk
from tkinter import *

# from tkinter import filedialog



# 定义语言变量字典
language_vars = {
    "page_1": "  HOME  ",
    "page_2": "  Lung Fibrosis Prediction  ",
    "page_3": "  Inflammation Classification  ",
    "page_4": "  Inflammation Prediction  ",
    "home_label0": "Nano-induced Lung Fibrosis Prediction (NILFP v1.0.0)",
    "home_label1": "An in silico approach for predicting lung fibrosis \ninduced by metal oxide nanomaterials",
    "input_label0": "Input parameters",
    "input_label1": "Within applicability domain ?",
    "para_label1": "IL-1β in THP-1 cell",
    "para_label2": "NADH in THP-1",
    "para_label3": "TGF-β in BEAS-2B cell",
    "para_label4": "Dissociation in PSF",
    "para_label5": "Zeta potential (mV)",
    "para_label6": "Hydrodynamic size (nm)",
    "para_label7": "NADH in BEAS-2B",
    "output_label8": "Predicted Fibrosis",
    "predict_button": "Predict",
    "metal_label": "Metal oxide nanoparticle",
    "metal_label1": "Metal oxide nanoparticle",
    "xme_label1": "Electronegativity of metal atom",
    "charge_label": "Cation charge",
    "concentration_label": "Concentration (μg/mL)",
    "inflammation_label": "Inflammation",
    "search_button1": "Search",
    "predict_button1": "Predict",
    "xme_label2": "Electronegativity of metal atom",
    "potential_label": "Zeta-potential (mV)",
    "dwater_label": "Hydrodynamic size (nm)",
    "fcil_label": "Fold change of IL-1b",
    "search_button2": "Search",
    "predict_button2": "Predict",
    "switch_lang_button": "English/中文"
}

# 英文语言
english = {
    "page_1": "  HOME  ",
    "page_2": "  Lung Fibrosis Prediction  ",
    "page_3": "  Inflammation Classification  ",
    "page_4": "  Inflammation Prediction  ",
    "home_label0": "Nano-induced Lung Fibrosis Prediction (NILFP v1.0.0)",
    "home_label1": "An in silico approach for predicting lung fibrosis \ninduced by metal oxide nanomaterials",
    "input_label0": "Input parameters",
    "input_label1": "Within applicability domain ?",
    "para_label1": "IL-1β in THP-1 cell",
    "para_label2": "NADH in THP-1",
    "para_label3": "TGF-β in BEAS-2B cell",
    "para_label4": "Dissociation in PSF",
    "para_label5": "Zeta potential (mV)",
    "para_label6": "Hydrodynamic size (nm)",
    "para_label7": "NADH in BEAS-2B",
    "output_label8": "Predicted Fibrosis",
    "predict_button": "Predict",
    "metal_label": "Metal oxide nanoparticle",
    "metal_label1": "Metal oxide nanoparticle",
    "xme_label1": "Electronegativity of metal atom",
    "charge_label": "Cation charge",
    "concentration_label": "Concentration (μg/mL)",
    "inflammation_label": "Inflammation",
    "search_button1": "Search",
    "predict_button1": "Predict",
    "xme_label2": "Electronegativity of metal atom",
    "potential_label": "Zeta-potential (mV)",
    "dwater_label": "Hydrodynamic size (nm)",
    "fcil_label": "Fold change of IL-1b",
    "search_button2": "Search",
    "predict_button2": "Predict",
    "switch_lang_button": "English/中文"
}

# 中文语言
chinese = {
    "page_1": "  主页  ",
    "page_2": "  肺纤维化预测  ",
    "page_3": "  炎症分类模型  ",
    "page_4": "  炎症定量预测  ",
    "home_label0": "Nano-induced Lung Fibrosis Prediction (NILFP v1.0.0)",
    "home_label1": "预测纳米金属氧化物诱导肺纤维化的 in silico 工具",
    "input_label0": "输入参数",
    "input_label1": "是否在应用域范围内 ?",
    "para_label1": "THP-1细胞的IL-1β释放",
    "para_label2": "THP-1细胞中NADH",
    "para_label3": "BEAS-2B细胞的TGF-β释放",
    "para_label4": "PSF中的解离度",
    "para_label5": "Zeta电势(mV)",
    "para_label6": "水合粒径 (nm)",
    "para_label7": "BEAS-2B细胞中NADH",
    "output_label8": "纤维化预测结果",
    "predict_button": "预测",
    "metal_label": "金属氧化物",
    "metal_label1": "金属氧化物",
    "xme_label1": "金属原子电负性",
    "charge_label": "金属阳离子电荷",
    "concentration_label": "暴露浓度(μg/mL)",
    "inflammation_label": "是否具有炎症效应",
    "search_button1": "查询",
    "predict_button1": "预测",
    "xme_label2": "金属原子电负性",
    "potential_label": "Zeta电势(mV)",
    "dwater_label": "水合粒径(nm)",
    "fcil_label": "IL-1b释放量的差异倍数",
    "search_button2": "查询",
    "predict_button2": "预测",
    "switch_lang_button": "English/中文"
}

# 默认使用英文语言
current_language = english

# 建立主窗口
window = tk.Tk()
# 定义主窗口属性
window.title("Nano-induced Lung Fibrosis Prediction (NILFP v1.0.0)")
width = 990
height = 600
window.resizable(0, 0)
screenwidth = window.winfo_screenwidth()
screenheight = window.winfo_screenheight()
size_geo = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
window.geometry(size_geo)
window.config(background="white")
window.iconbitmap('./images/logo.ico')

# 创建一个样式对象
style = ttk.Style()
# 修改样式的字体大小
style.configure("TNotebook.Tab", font=('times new roman', 18))
# 为主窗口创建 Notebook
notebook = ttk.Notebook(window)
notebook.pack(expand=True, fill="both")
style = ttk.Style()
style.configure("My.TFrame", background="white")

# 为notebook创建第一个页面page1
page1 = ttk.Frame(notebook, style="My.TFrame")
notebook.add(page1, text=language_vars["page_1"])
# # 加载图片
homebg_image = tk.PhotoImage(file="./images/homebackground.png")
# # 创建一个Label组件，并将图片设置为其背景
bg_label = tk.Label(page1, image=homebg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1, anchor="nw")
# # 修改Label组件的大小
bg_label.bind("<Configure>", lambda e: bg_label.config(width=e.width, height=e.height))

# 为page1创建label
home_label0 = Label(page1, text=language_vars["home_label0"], anchor="center", font=('times new Roman', 25, 'bold'),
                    fg="#004578")
# home_label0.configure(bg=bg_label['bg'], highlightthickness=0, borderwidth=0, transparentcolor=bg_label['bg'])
home_label0.place(x=105, y=50, width=800, height=50)
home_label1 = Label(page1, text=language_vars["home_label1"], width=40, height=2, anchor="center",
                    font=('times new roman', 20), fg="black")
home_label1.place(x=175, y=110)
home_label2 = Label(page1, text="in silico", width=6, height=1, anchor="center", font=('times new roman', 20, 'italic'),
                    fg="black")
home_label2.place(x=245, y=110)

# 定义初始位置
pos = "left"

# 为notebook创建第二个页面page2
page2 = ttk.Frame(notebook, style="My.TFrame")
notebook.add(page2, text=language_vars["page_2"])
# # 加载图片
page2_image = tk.PhotoImage(file="./images/page2background.png")
# # 创建一个Label组件，并将图片设置为其背景
page2_label = tk.Label(page2, image=page2_image)
page2_label.place(x=0, y=0, relwidth=1, relheight=1, anchor="nw")
# # 修改Label组件的大小
page2_label.bind("<Configure>", lambda e: bg_label.config(width=e.width, height=e.height))

# 为page2创建label
input_label0 = Label(page2, text=language_vars["input_label0"], anchor="center", font=('times new roman', 18, 'bold'),
                     fg="#004578")
input_label0.place(x=300, y=50, width=320, height=30)
input_label1 = Label(page2, text=language_vars["input_label1"], anchor="center", font=('times new roman', 18, 'bold'),
                     fg="#004578")
input_label1.place(x=550, y=50, width=320, height=30)
para_label1 = Label(page2, text=language_vars["para_label1"], anchor="e", font=('times new roman', 17), fg="black")
para_label1.place(x=20, y=100, width=355, height=25)
para_label2 = Label(page2, text=language_vars["para_label2"], anchor="e", font=('times new roman', 17), fg="black")
para_label2.place(x=20, y=140, width=355, height=25)
para_label3 = Label(page2, text=language_vars["para_label3"], anchor="e", font=('times new roman', 17), fg="black")
para_label3.place(x=20, y=180, width=355, height=25)
para_label4 = Label(page2, text=language_vars["para_label4"], anchor="e", font=('times new roman', 17), fg="black")
para_label4.place(x=20, y=220, width=355, height=25)
para_label5 = Label(page2, text=language_vars["para_label5"], anchor="e", font=('times new roman', 17), fg="black")
para_label5.place(x=20, y=260, width=355, height=25)
para_label6 = Label(page2, text=language_vars["para_label6"], anchor="e", font=('times new roman', 17), fg="black")
para_label6.place(x=20, y=300, width=355, height=25)
para_label7 = Label(page2, text=language_vars["para_label7"], anchor="e", font=('times new roman', 17), fg="black")
para_label7.place(x=20, y=340, width=355, height=25)
output_label8 = Label(page2, text=language_vars["output_label8"], anchor="e", font=('times new roman', 18), fg="black")
output_label8.place(x=20, y=440, width=350, height=30)
output_label = tk.Label(page2, text="", relief="solid", borderwidth=1)
output_label.place(x=380, y=440, width=180, height=30)
# 为page2创建entry
entry1 = tk.Entry(page2, relief="solid", font=("times new roman", 14), justify="center", bg="SystemButtonFace")
entry1.place(x=380, y=100, width=180, height=25)


def update_label2_1():
    try:
        value2_1 = float(entry1.get())
        if 0.51 <= value2_1 <= 13.42:
            label2_1.config(text="YES")
        else:
            label2_1.config(text="NO")
    except ValueError:
        label2_1.config(text="")


label2_1 = Label(page2, text="", font=("times new roman", 14), relief="solid", borderwidth=1)
label2_1.place(x=559, y=100, width=180, height=25)
entry1.bind("<KeyRelease>", lambda event: update_label2_1())

entry2 = tk.Entry(page2, relief="solid", font=("times new roman", 14), justify="center", bg="SystemButtonFace")
entry2.place(x=380, y=140, width=180, height=25)


def update_label2_2():
    try:
        value2_2 = float(entry2.get())
        if 8.64 <= value2_2 <= 129.44:
            label2_2.config(text="YES")
        else:
            label2_2.config(text="NO")
    except ValueError:
        label2_2.config(text="")


label2_2 = Label(page2, text="", font=("times new roman", 14), relief="solid", borderwidth=1)
label2_2.place(x=559, y=140, width=180, height=25)
entry2.bind("<KeyRelease>", lambda event: update_label2_2())

entry3 = tk.Entry(page2, relief="solid", font=("times new roman", 14), justify="center", bg="SystemButtonFace")
entry3.place(x=380, y=180, width=180, height=25)


def update_label2_3():
    try:
        value2_3 = float(entry3.get())
        if 0.90 <= value2_3 <= 2.15:
            label2_3.config(text="YES")
        else:
            label2_3.config(text="NO")
    except ValueError:
        label2_3.config(text="")


label2_3 = Label(page2, text="", font=("times new roman", 14), relief="solid", borderwidth=1)
label2_3.place(x=559, y=180, width=180, height=25)
entry3.bind("<KeyRelease>", lambda event: update_label2_3())

entry4 = tk.Entry(page2, relief="solid", font=("times new roman", 14), justify="center", bg="SystemButtonFace")
entry4.place(x=380, y=220, width=180, height=25)


def update_label2_4():
    try:
        value2_4 = float(entry4.get())
        if 0 <= value2_4 <= 0.94:
            label2_4.config(text="YES")
        else:
            label2_4.config(text="NO")
    except ValueError:
        label2_4.config(text="")


label2_4 = Label(page2, text="", font=("times new roman", 14), relief="solid", borderwidth=1)
label2_4.place(x=559, y=220, width=180, height=25)
entry4.bind("<KeyRelease>", lambda event: update_label2_4())

entry5 = tk.Entry(page2, relief="solid", font=("times new roman", 14), justify="center", bg="SystemButtonFace")
entry5.place(x=380, y=260, width=180, height=25)


def update_label2_5():
    try:
        value2_5 = float(entry5.get())
        if -29.5 <= value2_5 <= 42.6:
            label2_5.config(text="YES")
        else:
            label2_5.config(text="NO")
    except ValueError:
        label2_5.config(text="")


label2_5 = Label(page2, text="", font=("times new roman", 14), relief="solid", borderwidth=1)
label2_5.place(x=559, y=260, width=180, height=25)
entry5.bind("<KeyRelease>", lambda event: update_label2_5())

entry6 = tk.Entry(page2, relief="solid", font=("times new roman", 14), justify="center", bg="SystemButtonFace")
entry6.place(x=380, y=300, width=180, height=25)


def update_label2_6():
    try:
        value2_6 = float(entry6.get())
        if 2.07 <= value2_6 <= 3493:
            label2_6.config(text="YES")
        else:
            label2_6.config(text="NO")
    except ValueError:
        label2_6.config(text="")


label2_6 = Label(page2, text="", font=("times new roman", 14), relief="solid", borderwidth=1)
label2_6.place(x=559, y=300, width=180, height=25)
entry6.bind("<KeyRelease>", lambda event: update_label2_6())

entry7 = tk.Entry(page2, relief="solid", font=("times new roman", 14), justify="center", bg="SystemButtonFace")
entry7.place(x=380, y=340, width=180, height=25)


def update_label2_7():
    try:
        value2_7 = float(entry7.get())
        if 18.04 <= value2_7 <= 128.68:
            label2_7.config(text="YES")
        else:
            label2_7.config(text="NO")
    except ValueError:
        label2_7.config(text="")


label2_7 = Label(page2, text="", font=("times new roman", 14), relief="solid", borderwidth=1)
label2_7.place(x=559, y=340, width=180, height=25)
entry7.bind("<KeyRelease>", lambda event: update_label2_7())

# page2中的模型训练
# 导入数据集
data = pd.read_csv('./data/data.csv')
label = pd.read_csv('./data/label.csv')
X = data
y = label
# 定义随机森林分类器并拟合训练集数据
model = RandomForestClassifier(n_estimators=100, max_depth=None, min_samples_split=2, random_state=42)
model.fit(X, y)
scores = cross_val_score(model, X, y, cv=10)


# 输出交叉验证结果
# print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))

# 定义predict预测函数
def predict():
    parameter1 = float(entry1.get())
    parameter2 = float(entry2.get())
    parameter3 = float(entry3.get())
    parameter4 = float(entry4.get())
    parameter5 = float(entry5.get())
    parameter6 = float(entry6.get())
    parameter7 = float(entry7.get())
    # 调用模型，生成预测结果
    prediction = model.predict([[parameter2, parameter1, parameter7, parameter3, parameter6, parameter5, parameter4]])
    # 更新输出标签文本
    output_label.configure(text=str(prediction[0]), font=('times new roman', 18, 'bold'), fg="#004578")
    if output_label.cget("text") == "YES":
        output_label.configure(fg="red")
    elif output_label.cget("text") == "NO":
        output_label.configure(fg="green")


# 在page2中创建预测button并绑定predict函数
predict_button = tk.Button(page2, text=language_vars["predict_button"], font=('times new roman', 15, 'bold'),
                           fg="white", bg="#004578", command=predict)
predict_button.place(x=380, y=380, width=180, height=30)


# 在page2中创建help button
def open_file():
    file_path = "./help.txt"
    with open(file_path, "rb") as file:
        content = file.read()
        # 在弹出的对话框中显示文件内容
        dialog = tk.Toplevel(page2)
        text = tk.Text(dialog, font=('Arial', 10), fg="black")
        text.insert("1.0", content)
        text.pack()


help_button = tk.Button(page2, text="HELP", font=('times new roman', 10), fg="black", relief="flat", command=open_file)
help_button.place(x=10, y=10)

# 建立金属氧化物属性库
people_info = {
    "Al2O3": {"xme": 1.61, "potential": 22.95, "dwater": 429.5, "charge": 3.0},
    "CeO2": {"xme": 1.61, "charge": 4.0},
    "Co3O4": {"xme": 1.88, "potential": 20.78, "dwater": 202.1, "charge": 2.67},
    "CoO": {"xme": 1.88, "potential": 28.67, "dwater": 408.6, "charge": 2.0},
    "Cr2O3": {"xme": 1.66, "potential": -5.62, "dwater": 416.3, "charge": 3.0},
    "CuO": {"xme": 1.9, "potential": 21.06, "dwater": 246.2, "charge": 2.0},
    "Fe2O3": {"xme": 1.83, "potential": -3.87, "dwater": 297.2, "charge": 3.0},
    "Fe3O4": {"xme": 1.83, "potential": -14.27, "dwater": 358.6, "charge": 2.67},
    "HfO2": {"xme": 1.3, "potential": -27.78, "dwater": 262.2, "charge": 4.0},
    "In2O3": {"xme": 1.78, "potential": 5.4, "dwater": 310.6, "charge": 3.0},
    "La2O3": {"xme": 1.1, "potential": 23.04, "dwater": 711.3, "charge": 3.0},
    "NiO": {"xme": 1.91, "charge": 2.0},
    "Sb2O3": {"xme": 2.05, "charge": 3.0},
    "SnO2": {"xme": 1.96, "potential": -27.45, "dwater": 480.0, "charge": 4.0},
    "Bi2O3": {"xme": 2.02, "potential": 18.12, "dwater": 515.6, "charge": 3.0},
    "Dy2O3": {"xme": 1.22, "potential": 22.24, "dwater": 751.7, "charge": 3.0},
    "Er2O3": {"xme": 1.24, "potential": 26.14, "dwater": 442.5, "charge": 3.0},
    "Gd2O3": {"xme": 1.2, "potential": 22.63, "dwater": 687.3, "charge": 3.0},
    "Ni2O3": {"xme": 1.91, "potential": -4.36, "dwater": 386.9, "charge": 3.0},
    "Yb2O3": {"xme": 1.1, "potential": 13.48, "dwater": 799.9, "charge": 3.0},
    "TiO2": {"xme": 1.54, "potential": 14.68, "dwater": 310.0, "charge": 4.0},
    "WO3": {"xme": 2.36, "potential": 35.84, "dwater": 111.6, "charge": 6.0},
    "Y2O3": {"xme": 1.22, "potential": 26.09, "dwater": 743.3, "charge": 3.0},
    "ZnO": {"xme": 1.65, "potential": -14.85, "dwater": 276.6, "charge": 2.0},
    "ZrO2": {"xme": 1.33, "potential": -14.85, "dwater": 508.8, "charge": 4.0},
    "Sm2O3": {"xme": 1.17, "potential": 47.34, "dwater": 765.1, "charge": 3.0},
    "Nd2O3": {"xme": 1.14, "potential": 30.26, "dwater": 652.1, "charge": 3.0},
    "βMnO2": {"xme": 1.55, "potential": 28.38, "dwater": 432.2, "charge": 3.0},
    "Ho2O3": {"xme": 1.23, "potential": -13.33, "dwater": 1145.33, "charge": 3.0},
    "Pr6O11": {"xme": 1.13, "potential": -11.6, "dwater": 911.97, "charge": 3.67},
    "MoO3": {"xme": 2.16, "potential": -13.5, "dwater": 439.37, "charge": 6.0},
    "MoO2": {"xme": 2.16, "potential": -16.33, "dwater": 381.97, "charge": 4.0},
    "Ta2O5": {"xme": 1.5, "potential": -12.17, "dwater": 399.03, "charge": 5.0},
    "Nb2O5": {"xme": 1.6, "potential": -18.83, "dwater": 332.93},
    "Mn3O4": {"xme": 1.55, "potential": 1.33, "dwater": 530.53, "charge": 2.67},
}

# 为notebook创建第三个页面page3
page3 = ttk.Frame(notebook, style="My.TFrame")
notebook.add(page3, text=language_vars["page_3"])
# # 加载图片
page3_image = tk.PhotoImage(file="./images/page3background.png")
# # 创建一个Label组件，并将图片设置为其背景
page3_label = tk.Label(page3, image=page3_image)
page3_label.place(x=0, y=0, relwidth=1, relheight=1, anchor="nw")
# # 修改Label组件的大小
page3_label.bind("<Configure>", lambda e: bg_label.config(width=e.width, height=e.height))

# 在page3中创建标签和文本框，用于输入金属氧化物名称和显示查询结果
input_label2 = Label(page3, text=language_vars["input_label0"], anchor="center", font=('times new roman', 18, 'bold'),
                     fg="#004578")
input_label2.place(x=270, y=50, width=320, height=30)
input_label3 = Label(page3, text=language_vars["input_label1"], anchor="center", font=('times new roman', 18, 'bold'),
                     fg="#004578")
input_label3.place(x=520, y=50, width=320, height=30)
name_label0 = Label(page3, text=language_vars["metal_label"], anchor="e", font=('times new roman', 17), fg="black")
name_label0.place(x=20, y=100, width=320, height=25)
name_entry1 = tk.Entry(page3, relief="solid", font=("times new roman", 14), justify="center", bg="SystemButtonFace")
name_entry1.place(x=340, y=100, width=180, height=25)

xme_label1 = Label(page3, text=language_vars["xme_label1"], anchor="e", font=('times new roman', 17), fg="black")
xme_label1.place(x=20, y=180, width=320, height=25)
xme_entry1 = tk.Entry(page3, relief="solid", font=("times new roman", 14), justify="center", bg="SystemButtonFace")
xme_entry1.place(x=340, y=180, width=180, height=25)


def update_label3_1():
    try:
        value3_1 = float(xme_entry1.get())
        if 1.1 <= value3_1 <= 2.05:
            label3_1.config(text="YES")
        else:
            label3_1.config(text="NO")
    except ValueError:
        label3_1.config(text="")


label3_1 = Label(page3, text="", font=("times new roman", 14), relief="solid", borderwidth=1)
label3_1.place(x=519, y=180, width=180, height=25)
xme_entry1.bind("<KeyRelease>", lambda event: update_label3_1())

charge_label2 = Label(page3, text=language_vars["charge_label"], anchor="e", font=('times new roman', 17), fg="black")
charge_label2.place(x=20, y=240, width=320, height=25)
charge_entry1 = tk.Entry(page3, relief="solid", font=("times new roman", 14), justify="center", bg="SystemButtonFace")
charge_entry1.place(x=340, y=240, width=180, height=25)


def update_label3_2():
    try:
        value3_2 = float(charge_entry1.get())
        if 2 <= value3_2 <= 4:
            label3_2.config(text="YES")
        else:
            label3_2.config(text="NO")
    except ValueError:
        label3_2.config(text="")


label3_2 = Label(page3, text="", font=("times new roman", 14), relief="solid", borderwidth=1)
label3_2.place(x=519, y=240, width=180, height=25)
charge_entry1.bind("<KeyRelease>", lambda event: update_label3_2())

concentration_label3 = Label(page3, text=language_vars["concentration_label"], anchor="e", font=('times new roman', 17),
                             fg="black")
concentration_label3.place(x=20, y=300, width=320, height=25)
concentration_entry = tk.Entry(page3, relief="solid", font=("times new roman", 14), justify="center",
                               bg="SystemButtonFace")
concentration_entry.place(x=340, y=300, width=180, height=25)


def update_label3_3():
    try:
        value3_3 = float(concentration_entry.get())
        if 0 <= value3_3 <= 200:
            label3_3.config(text="YES")
        else:
            label3_3.config(text="NO")
    except ValueError:
        label3_3.config(text="")


label3_3 = Label(page3, text="", font=("times new roman", 14), relief="solid", borderwidth=1)
label3_3.place(x=519, y=300, width=180, height=25)
concentration_entry.bind("<KeyRelease>", lambda event: update_label3_3())

result_label10 = Label(page3, text=language_vars["inflammation_label"], anchor="e", font=('times new roman', 18),
                       fg="black")
result_label10.place(x=20, y=400, width=320, height=30)
result_label11 = Label(page3, font=('times new roman', 18), relief="solid", fg="#004578", borderwidth=1)
result_label11.place(x=340, y=400, width=180, height=30)


# 查询金属氧化物信息
def search1():
    name1 = name_entry1.get()
    if name1 in people_info:
        info = people_info[name1]
        xme_entry1.delete(0, tk.END)
        xme_entry1.insert(0, str(info["xme"]))
        charge_entry1.delete(0, tk.END)
        charge_entry1.insert(0, str(info["charge"]))
    else:
        xme_entry1.delete(0, tk.END)
        charge_entry1.delete(0, tk.END)
        tk.messagebox.showerror("Not Found", "")


# 创建按钮，用于触发查询操作
search1_button = tk.Button(page3, text=language_vars["search_button1"], font=('times new roman', 15, 'bold'),
                           fg="white", bg="#004578", command=search1)
search1_button.place(x=340, y=140, width=180, height=25)


# 创建按钮，用于触发计算操作
def check0():
    xme1 = float(xme_entry1.get())
    charge = float(charge_entry1.get())
    concentration = float(concentration_entry.get())
    if xme1 <= 1.55 and charge > 3.15:
        result_label11.configure(text="NO", fg="green")
    elif xme1 <= 1.55 and charge <= 3.15 and concentration > 6.2:
        result_label11.configure(text="YES", fg="red")
    elif xme1 <= 1.2 and charge <= 3.15 and 3.1 < concentration <= 6.2:
        result_label11.configure(text="YES", fg="red")
    elif 1.55 >= xme1 > 1.2 and charge <= 3.15 and 3.1 < concentration <= 6.2:
        result_label11.configure(text="NO", fg="green")
    elif xme1 <= 1.55 and charge <= 3.15 and concentration <= 3.1:
        result_label11.configure(text="NO", fg="green")
    elif xme1 > 1.55 and concentration <= 65.0:
        result_label11.configure(text="NO", fg="green")
    elif xme1 > 1.83 and concentration > 65.0:
        result_label11.configure(text="NO", fg="green")
    elif 1.55 < xme1 <= 1.78 and 65.0 < concentration <= 100.0:
        result_label11.configure(text="NO", fg="green")
    elif 1.55 < xme1 <= 1.78 and concentration > 100.0:
        result_label11.configure(text="YES", fg="red")
    elif 1.78 < xme1 <= 1.83 and concentration > 65.0:
        result_label11.configure(text="YES", fg="red")
    else:
        result_label11.configure(text="Error")


# 创建按钮，用于触发计算操作
check_button = tk.Button(page3, text=language_vars["predict_button1"], font=('times new roman', 15, 'bold'), fg="white",
                         bg="#004578", command=check0)
check_button.place(x=340, y=350, width=180, height=30)

# 为notebook创建第四个页面page4
page4 = ttk.Frame(notebook, style="My.TFrame")
notebook.add(page4, text=language_vars["page_4"])
# # 加载图片
page4_image = tk.PhotoImage(file="./images/page3background.png")
# # 创建一个Label组件，并将图片设置为其背景
page4_label = tk.Label(page4, image=page4_image)
page4_label.place(x=0, y=0, relwidth=1, relheight=1, anchor="nw")
# # 修改Label组件的大小
page4_label.bind("<Configure>", lambda e: bg_label.config(width=e.width, height=e.height))
# 在page4中创建标签和文本框，用于输入金属氧化物名称和显示查询结果
input_label4 = Label(page4, text=language_vars["input_label0"], anchor="center", font=('times new roman', 18, 'bold'),
                     fg="#004578")
input_label4.place(x=270, y=50, width=320, height=30)
input_label5 = Label(page4, text=language_vars["input_label1"], anchor="center", font=('times new roman', 18, 'bold'),
                     fg="#004578")
input_label5.place(x=520, y=50, width=320, height=30)
name_label4 = Label(page4, text=language_vars["metal_label1"], anchor="e", font=('times new roman', 17), fg="black")
name_label4.place(x=20, y=100, width=320, height=25)
name_entry = tk.Entry(page4, relief="solid", font=("times new roman", 14), justify="center", bg="SystemButtonFace")
name_entry.place(x=340, y=100, width=180, height=25)

xme_label5 = Label(page4, text=language_vars["xme_label2"], anchor="e", font=('times new roman', 17), fg="black")
xme_label5.place(x=20, y=180, width=320, height=25)
xme_entry = tk.Entry(page4, relief="solid", font=("times new roman", 14), justify="center", bg="SystemButtonFace")
xme_entry.place(x=340, y=180, width=180, height=25)


def update_label4_1():
    try:
        value4_1 = float(xme_entry.get())
        if 1.1 <= value4_1 <= 2.36:
            label4_1.config(text="YES")
        else:
            label4_1.config(text="NO")
    except ValueError:
        label4_1.config(text="")


label4_1 = Label(page4, text="", font=("times new roman", 14), relief="solid", borderwidth=1)
label4_1.place(x=519, y=180, width=180, height=25)
xme_entry.bind("<KeyRelease>", lambda event: update_label4_1())

potential_label6 = Label(page4, text=language_vars["potential_label"], anchor="e", font=('times new roman', 17),
                         fg="black")
potential_label6.place(x=20, y=240, width=320, height=25)
potential_entry = tk.Entry(page4, relief="solid", font=("times new roman", 14), justify="center", bg="SystemButtonFace")
potential_entry.place(x=340, y=240, width=180, height=25)


def update_label4_2():
    try:
        value4_2 = float(potential_entry.get())
        if -30.04 <= value4_2 <= 47.34:
            label4_2.config(text="YES")
        else:
            label4_2.config(text="NO")
    except ValueError:
        label4_2.config(text="")


label4_2 = Label(page4, text="", font=("times new roman", 14), relief="solid", borderwidth=1)
label4_2.place(x=519, y=240, width=180, height=25)
potential_entry.bind("<KeyRelease>", lambda event: update_label4_2())

dwater_label7 = Label(page4, text=language_vars["dwater_label"], anchor="e", font=('times new roman', 17), fg="black")
dwater_label7.place(x=20, y=300, width=320, height=25)
dwater_entry = tk.Entry(page4, relief="solid", font=("times new roman", 14), justify="center", bg="SystemButtonFace")
dwater_entry.place(x=340, y=300, width=180, height=25)


def update_label4_3():
    try:
        value4_3 = float(dwater_entry.get())
        if 111.6 <= value4_3 <= 862.1:
            label4_3.config(text="YES")
        else:
            label4_3.config(text="NO")
    except ValueError:
        label4_3.config(text="")


label4_3 = Label(page4, text="", font=("times new roman", 14), relief="solid", borderwidth=1)
label4_3.place(x=519, y=300, width=180, height=25)
dwater_entry.bind("<KeyRelease>", lambda event: update_label4_3())

result_label8 = Label(page4, text=language_vars["fcil_label"], anchor="e", font=('times new roman', 17), fg="black")
result_label8.place(x=20, y=400, width=320, height=25)
result_label9 = Label(page4, relief="solid", borderwidth=1, font=('times new roman', 15), fg="black")
result_label9.place(x=340, y=400, width=180, height=25)


# 查询金属氧化物信息
def search2():
    name = name_entry.get()
    if name in people_info:
        info = people_info[name]
        xme_entry.delete(0, tk.END)
        xme_entry.insert(0, str(info["xme"]))
        potential_entry.delete(0, tk.END)
        potential_entry.insert(0, str(info["potential"]))
        dwater_entry.delete(0, tk.END)
        dwater_entry.insert(0, str(info["dwater"]))
    else:
        xme_entry.delete(0, tk.END)
        potential_entry.delete(0, tk.END)
        dwater_entry.delete(0, tk.END)
        tk.messagebox.showerror("Not Found", "")


# 创建按钮，用于触发查询操作
search2_button = tk.Button(page4, text=language_vars["search_button2"], relief="raised",
                           font=('times new roman', 15, 'bold'), fg="white", bg="#004578", command=search2)
search2_button.place(x=340, y=140, width=180, height=25)


def calculate1():
    xme = float(xme_entry.get())
    potential = float(potential_entry.get())
    dwater = float(dwater_entry.get())
    result1 = 25.4 - 20.6 * xme + 0.283 * potential + 0.0343 * dwater
    result = round(result1, 2)
    result_label9.configure(text=str(result), font=('times new roman', 15), fg="#004578")


# 创建按钮，用于触发计算操作
calculate_button = tk.Button(page4, text=language_vars["predict_button2"], font=('times new roman', 15, 'bold'),
                             fg="white", bg="#004578", command=calculate1)
calculate_button.place(x=340, y=350, width=180, height=30)


# 定义语言切换函数
def switch_language():
    global current_language

    # 切换到中文语言
    if current_language == english:
        current_language = chinese
    # 切换到英文语言
    else:
        current_language = english
    # 更新语言变量字典
    language_vars["page_1"] = current_language["page_1"]
    language_vars["page_2"] = current_language["page_2"]
    language_vars["page_3"] = current_language["page_3"]
    language_vars["page_4"] = current_language["page_4"]
    language_vars["home_label0"] = current_language["home_label0"]
    language_vars["home_label1"] = current_language["home_label1"]
    language_vars["input_label0"] = current_language["input_label0"]
    language_vars["input_label1"] = current_language["input_label1"]
    language_vars["para_label1"] = current_language["para_label1"]
    language_vars["para_label2"] = current_language["para_label2"]
    language_vars["para_label3"] = current_language["para_label3"]
    language_vars["para_label4"] = current_language["para_label4"]
    language_vars["para_label5"] = current_language["para_label5"]
    language_vars["para_label6"] = current_language["para_label6"]
    language_vars["para_label7"] = current_language["para_label7"]
    language_vars["output_label8"] = current_language["output_label8"]
    language_vars["switch_lang_button"] = current_language["switch_lang_button"]
    language_vars["predict_button"] = current_language["predict_button"]
    language_vars["predict_button1"] = current_language["predict_button1"]
    language_vars["predict_button2"] = current_language["predict_button2"]
    language_vars["search_button1"] = current_language["search_button1"]
    language_vars["search_button2"] = current_language["search_button2"]
    language_vars["metal_label"] = current_language["metal_label"]
    language_vars["metal_label1"] = current_language["metal_label1"]
    language_vars["xme_label1"] = current_language["xme_label1"]
    language_vars["xme_label2"] = current_language["xme_label2"]
    language_vars["charge_label"] = current_language["charge_label"]
    language_vars["concentration_label"] = current_language["concentration_label"]
    language_vars["inflammation_label"] = current_language["inflammation_label"]
    language_vars["potential_label"] = current_language["potential_label"]
    language_vars["dwater_label"] = current_language["dwater_label"]
    language_vars["fcil_label"] = current_language["fcil_label"]

    # 更新标签和按钮文本属性
    predict_button.configure(text=language_vars["predict_button"])
    check_button.configure(text=language_vars["predict_button1"])
    calculate_button.configure(text=language_vars["predict_button2"])
    search1_button.configure(text=language_vars["search_button1"])
    search2_button.configure(text=language_vars["search_button2"])

    switch_lang_button.configure(text=language_vars["switch_lang_button"])
    notebook.tab(0, text=language_vars["page_1"])
    notebook.tab(1, text=language_vars["page_2"])
    notebook.tab(2, text=language_vars["page_3"])
    notebook.tab(3, text=language_vars["page_4"])
    home_label0.configure(text=language_vars["home_label0"])
    home_label1.configure(text=language_vars["home_label1"])
    input_label0.configure(text=language_vars["input_label0"])
    input_label1.configure(text=language_vars["input_label1"])
    input_label2.configure(text=language_vars["input_label0"])
    input_label3.configure(text=language_vars["input_label1"])
    input_label4.configure(text=language_vars["input_label0"])
    input_label5.configure(text=language_vars["input_label1"])
    para_label1.configure(text=language_vars["para_label1"])
    para_label2.configure(text=language_vars["para_label2"])
    para_label3.configure(text=language_vars["para_label3"])
    para_label4.configure(text=language_vars["para_label4"])
    para_label5.configure(text=language_vars["para_label5"])
    para_label6.configure(text=language_vars["para_label6"])
    para_label7.configure(text=language_vars["para_label7"])
    output_label8.configure(text=language_vars["output_label8"])
    name_label0.configure(text=language_vars["metal_label"])
    name_label4.configure(text=language_vars["metal_label1"])
    xme_label1.configure(text=language_vars["xme_label1"])
    xme_label5.configure(text=language_vars["xme_label2"])
    charge_label2.configure(text=language_vars["charge_label"])
    concentration_label3.configure(text=language_vars["concentration_label"])
    result_label10.configure(text=language_vars["inflammation_label"])
    result_label8.configure(text=language_vars["fcil_label"])
    potential_label6.configure(text=language_vars["potential_label"])
    dwater_label7.configure(text=language_vars["dwater_label"])
    global pos
    if pos == "left":
        home_label2.place_forget()  # 从初始英文位置移除label
        home_label2.place(x=620, y=125)  # 将label移到中文位置
        pos = "right"
    else:
        home_label2.place_forget()  # 从中文位置移除label
        home_label2.place(x=245, y=110)  # 将label移到初始英文位置
        pos = "left"


# 创建切换语言按钮并绑定语言切换函数
switch_lang_button = tk.Button(window, text=language_vars["switch_lang_button"], font=('times new roman', 8),
                               fg="black", bg="white", command=switch_language)
switch_lang_button.place(x=20, y=550)

# 主循环
window.mainloop()
