![version](https://img.shields.io/badge/version-1.0.0-blue)
[![PyPI license](https://img.shields.io/pypi/l/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/)

# Hidden-Markury (Beta-Version)
FRET Trace Analysis with Hidden-Markov-Model (Jupyter Notebook)

![Software preview](images/Preview.png?raw=true "Software Preview")

## Installation
#### 1. Install a C compiler for hmmlearn (optional, if missing) 
The basic implementation of the Hidden-Markov-Process and the model optimization is based on build-in functions of the python library `hmmlearn`[[1]](#1).
`hmmlearn` requires a C compiler. If you don't have a C compiler installed, the installation of `hmmlearn` will raise an error.

On Windows: 
- Go to https://visualstudio.microsoft.com/downloads/ -> Select "Tools for Visual Studio 2019" -> "Build Tools for Visual Studio 2019" -> Download
- Install "Python development" with "Python native development tools" selected
![Python development tools](images/MicrosoftDevTools.png?raw=true "Python Development Tools")

On Linux/Mac:
- Not tested yet! Installation of hmmlearn (see next section) should raise informative error what to do.

#### 2. Create new environment (optional)
Create a new python environment to install the required packages

Example in Anaconda prompt: `conda create -n hmm`

#### 3. Install hmmlearn
- `pip install --upgrade --user hmmlearn`

If pip installation fails, you can try to directly download and install the wheel.

- (alternative: download wheel from http://pypi.fcio.net/simple/hmmlearn/ and install with `pip install PATH_TO_WHEEL`)

#### 4. Install other required packages

The following packages are needed for full functionality:
- numpy
- pandas
- matplotlib
- scipy

#### Test system
* Windows 10, 64 bit system
* Anaconda3 (64 bit)
* Python 3.7 environment
* Packages:
  * hmmlearn 0.2.2
  * numpy 1.17.3
  * pandas 0.25.3
  * matplotlib 3.1.1
  * scipy 1.3.1

## Getting Started
#### 1. Clone or download this repository
Clone repository via git

`git clone https://github.com/ChristianGebhardt/Hidden-Markury`

or clone/download repository manually:

![Download repository](images/Download.png?raw=true "Download Repository")

#### 2. Open "Hidden-Markury Notebook" in jupyter notebook
* Activate python environment in python console (e.g. `activate hmm` in Anaconda prompt) with required packages installed (see [Installation](#Installation))
* Navigate into repository folder `cd PATH_TO_HIDDEN-MARCURY`
* Start jupyter with command `jupyter notebook`
* Run notebook "Hidden-Marcury Notebook.ipynb"
![Jupyter Preview](images/Jupyter.png?raw=true "Jupyter Preview")

#### 3. Check installations
There is an extra import file, which checks and imports all the required packages at the beginning. If everything works fine, it should look the following:
![Import preview](images/PreviewImport.png?raw=true "Import Preview")
Otherwise, an error should inform you what to do.

#### 4. Run example analysis
There are several example traces provided in the folder `examples` provided by the "kinSoftChallenge"[[2]](#2). Those traces can directly be used to get familiar with the software.



If you run the notebook cell-by-cell and follow the instructions, you should get the optimized model with the fitted transition rates and the state prediction for the analyzed traces:

![Prediction preview](images/PreviewPrediction.png?raw=true "Prediction Preview")

## Author(s)
* **Christian Gebhardt** - *Initial work* - [ChristianGebhardt](https://github.com/ChristianGebhardt)

See also the list of [contributors](https://github.com/ChristianGebhardt/Hidden-Markury/contributors) who participated in this project.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Release Notes
### Version
v1.0.1 - 2020-02-25
### Features
* Global trace analysis
* 1D (E-Trace) or 2D (photon channels) analysis
* Model optimization
* Lifetime fitting
* Sample variation (error estimation)

## Acknowledgments
This software was designed and created by Christian Gebhardt within ongoing work of the Cordes lab (http://www.mikrobiologie.biologie.uni-muenchen.de/forschung/ag_cordes/index.html). The project was financed by the German Science Foundation (SFB863, TP A13, to Thorben Cordes), an ERC Starting Grant (No. 638536 – SM-IMPORT to Thorben Cordes) and a PhD fellowship of the Studienstiftung des deutsche Volkes (to Christian Gebhardt). 

## Bibliography
<a id="1">[1]</a> https://hmmlearn.readthedocs.io/en/latest/index.html

<a id="2">[2]</a> https://sites.google.com/view/kinsoftchallenge/
