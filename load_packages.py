SUCCESSFUL = True

def error_message(modul_name):
    print("- Module '"+modul_name+"' is not installed\n\n  Run \x1b[33mpip install "+modul_name+"\x1b[30m in your shell to install the package\n")

def error_message2(modul_name):
    print("- Module '"+error.name+"' cannot be found\n\n  Ensure that the file '"+error.name+".py' is in the working directory (directory of the notebook). The module ist provided with this jupyter notebook at \x1b[4mhttps://github.com/ChristianGebhardt/hmm\x1b[0m\n")

# numpy
try:
    import numpy as np
except ImportError as error:
    error_message(error.name)
    SUCCESSFUL = False

# pandas
try:
    import pandas as pd
except ImportError as error:
    error_message(error.name)
    SUCCESSFUL = False

# matplotlib
try:
    import matplotlib.pyplot as plt
except ImportError as error:
    error_message(error.name)
    SUCCESSFUL = False

# scipy
try:
    from scipy.optimize import curve_fit
except ImportError as error:
    error_message(error.name)
    SUCCESSFUL = False
    
# warnings
try:
    import warnings
except ImportError as error:
    error_message(error.name)
    SUCCESSFUL = False
    
#hmmlearn
try:
    import hmmlearn
    from hmmlearn import hmm
except ImportError as error:
    error_message(error.name)
    print("  << Warning: hmmlearn requires a c-compiler (on Windows: go to https://visualstudio.microsoft.com/visual-cpp-build-tools/ and install 'Build Tools for Visual Studio' first) >>")
    SUCCESSFUL = False

try:
    import os
    import sys
    import time
    
    from importlib import reload
    
    import ipywidgets
    from ipywidgets import widgets
    from IPython.display import display,clear_output
except ImportError as error:
    raise error

# oshelper
try:    
    import oshelper as oh
except ImportError as error:
    error_message2(error.name)
    SUCCESSFUL = False  
# hmmhelper
try:
    import hmmhelper as hh
except ImportError as error:
    error_message2(error.name)
    SUCCESSFUL = False

#Final message
if SUCCESSFUL:
    print("All required modules are installed and loaded.\n\nYou can go on and play!")
else:
    print("\n(Note that this program is not extensively tested with different operating systems and python/package versions. You have to ensure yourself that all installed packages work together)\n\n================\n\n\x1b[1mPlease, install all required packages first, before moving on to the next sections of this Jupyter Notebook!\x1b[0m\n")
    raise Exception('Not all required modules found!')