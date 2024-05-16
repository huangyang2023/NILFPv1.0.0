# NILFPv1.0.0
Nano-induced Lung Fibrosis Prediction (NILFPv1.0.0)
![](/images/llogo.png)
- [Overview](#overview)
- [Documentation](#documentation)
- [System Requirements](#system-requirements)
- [Installation Guide](#installation-guide)
- [Instructions for Use](#Instructions-for-Use)
- [License](#License)
# Overview
`NILFPv1.0.0` (`Nano-induced Lung Fibrosis Prediction`) is a Python package containing tools for predicting in vivo lung fibrosis using in vitro and in chemico data.
NILFP aims to be a computational toxicology tool based on machine learning approaches for high-through put predicting of in vivo toxicity. Seven input parameters are needed in the user interface of the software for predicting lung fibrosis. Three of the input parameters can be generated from MeONPs characterization (dissolution in PSF, zeta potential, hydrodynamic size), while four of the them need to be collected by in vitro tests (IL-1β in macrophages, NADH in macrophages, TGF-β1 in epithelial cells, and NADH in epithelial cells). The detailed test procedures can be found in HELP profile. The package can be installed on all major platforms (e.g. *Linux*, *macOS*, *Windows*).

# Documenation


# System Requirements
## Hardware requirements
`NILFPv1.0.0` package requires only a standard computer.

## Software requirements
### OS Requirements
This package is supported for *Windows*, *macOS* and *Linux*. The package has been tested on the following systems:
+ Windows: Windows 10(22H2)/ Windows 11(22H2)
+ macOS: Sonoma 14.1.2
+ Linux: Ubuntu 18.04

### Python Dependencies
`NILFPv1.0.0` mainly depends on the Python scientific stack.
```
pandas==2.1.4
scikit-learn==1.3.0
```
# Installation Guide
### Install in Python
```
git clone https://github.com/huangyang2023/NILFPv1.0.0.git
cd NILFPv1.0.0
pip3 install -r requirements.txt
```
### Non-installed Version on *Windows*
- Click [***here***](https://github.com/huangyang2023/NILFPv1.0.0/releases/download/NILFPv1.0.0/NILFP.v1.0.0.zip) to download the ZIP file for the portable version of this package.
- Unzip the ZIP file and enter the extracted folder.
- Run *NILFP v1.0.0.exe*.
### Typical Install Time on a *Normal* Desktop Computer
Approximately 60 seconds.

# Instructions for Use
## How to Run the Software on Your Data
### Expected Run Time for Demo on a *Normal* Desktop Computer
Approximately 60 seconds (excluding data input time).
### Lung Fibrosis Prediction
![](/images/LungFibrosis.gif)
### Inflammation Classification
![](/images/InflammationClassification.gif)
### Inflammation Prediction
![](/images/InflammationPrediction.gif)
# License
This project is covered under the **GNU General Public License version 3**.
