# Hidden-Markury
FRET Trace Analysis with Hidden-Markov-Model (Jupyter Notebook)

## Installation
#### 1. Install a C compiler for hmmlearn (optional, if missing) 

hmmlearn requires a C compiler. If you don't have a C compiler installed, the installation of hmmlearn will raise an error.

On Windows: 
- Go to https://visualstudio.microsoft.com/downloads/ -> Select "Tools for Visual Studio 2019" -> "Build Tools for Visual Studio 2019" -> Download
- Install "Python Development" with "Python native development tools" selected
![Python development tools](images/MicrosoftDevTools.png?raw=true "Python Development Tools")

#### 2. Install hmmlearn
- `pip install --upgrade --user hmmlearn`

If pip installation fails, you can try to directly download and install the wheel.

- (alternative: download wheel from http://pypi.fcio.net/simple/hmmlearn/ and install with `pip install PATH_TO_WHEEL`)

#### 3. Install other required packages

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
TODO
#### 2. Open Jupyter Notebook
TODO
#### 3. Check installations
TODO
#### 4. Run example analysis
TODO
## Author(s)

* **Christian Gebhardt** - *Initial work* - [ChristianGebhardt](https://github.com/ChristianGebhardt)

See also the list of [contributors](https://github.com/ChristianGebhardt/Hidden-Markury/contributors) who participated in this project.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgments
This software was designed and created by Christian Gebhardt within ongoing work of the Cordes lab (http://www.mikrobiologie.biologie.uni-muenchen.de/forschung/ag_cordes/index.html). The project was financed by the German Science Foundation (SFB863, TP A13, to Thorben Cordes), an ERC Starting Grant (No. 638536 – SM-IMPORT to Thorben Cordes) and a PhD fellowship of the Studienstiftung (to Christian Gebhardt). 
