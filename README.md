# BlackBoard - Test Analyzer

## User manual

### 1. Use python 2.7 or higher
- To determine if Python is already installed, type “python –version” or “py –version” into a terminal. If a version of Python is displayed, it is already installed. 
- Another way to determine if Python is already installed is by searching “Python” using the search feature of Window’s Start Menu or Apple’s Spotlight.
- Alternatively, if Python is not installed, refer to the following web page for installation guide: https://www.python.org/downloads/

### 2. Install necessary libraries 
· To install necessary libraries, make sure you already have pip installed
o To determine if pip is already installed type “pip –version” in a terminal. If the version of the library is displayed, it is already installed
o Alternatively, if pip was not installed, refer to the following web page for installation guide: https://pip.pypa.io/en/stable/installation/

· If pip is already installed, install all the necessary libraries by executing the command “pip install <Library Name>”. Necessary libraries include the following:
o textblob

· To install the textblob library, you also need to execute the following line: “python -m textblob.download_corpora”
o PySimpleGUI
o matplotlib
o concurrent.futures
o abc
o threading
o imp
o language_tool_python
o turtle
o numpy

### 3. Now you are ready to run the app
The app implements the Blackboard archetecture pattern as each KS accesses the blackboard once at a time and changes are then saved to the back KS and main board.

## The app has multiple fuctions with the crown jewels being: 
- Spelling Check
- Grammar Check 
- Punctuaction Check
- Word Frequency Analysis
- Sentiment Analysis

