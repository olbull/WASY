# LéXPLORE Meteostation

## Project Information

The data is collected within the frame of the [LeXPLORE project](https://wp.unil.ch/lexplore/) on Lake Geneva. 
The data is used and displayed on the [Datalakes website](https://www.datalakes-eawag.ch/).

## Sensors

Meteostation is a weather station collecting a wide range of meteorological data.
Every 10 minutes it measures wind speed, wind direction, amount of rainfal, temperature and solar irradiance. 

## Installation

:warning You need to have [git](https://git-scm.com/downloads) and [git-lfs](https://git-lfs.github.com/) installed in order to successfully clone the repository.

- Clone the repository to your local machine using the command: 

 `git clone https://renkulab.io/gitlab/lexplore/meteostation.git`
 
 Note that the repository will be copied to your current working directory.

- Use Python 3 and install the requirements with:

 `pip install -r requirements.txt`

 The python version can be checked by running the command `python --version`. In case python is not installed or only an older version of it, it is recommend to install python through the anaconda distribution which can be downloaded [here](https://www.anaconda.com/products/individual). 

## Usage

### Process new data

In order to process new data locally on your machine the file path needs to be adapted to your local file system. The following steps are therefore necessary: 

- Edit the `scripts/input_batch.bat` file. Change all the directory paths to match your local file system. This file contains all the file paths necessary to launch the batch scripts `runfile.bat`.

- Edit the `scripts/input_python.py` file. Change all the directory paths to match your local file system. This file contains all the directories where the python script outputs data to.

To process new data, place the data in the input directory which you specified in the `scripts/input_batch.bat` file. Double-clicking on the `runfile.bat` file will automaticall process all the data in the input directory and store the output in the directories specified in the `scripts/input_python.py` file.

### Adapt/Extend data processing piepeline

The python script `scripts/main_meteostation.py` defines the different processing steps while the python script `scripts/meteostation.py` contains the python class thetis with all the corresponding 
class methods to process the data. To add a new processing or visualization step, a new class method can be created in the `meteostation.py` file and the step can be added in `main_meteostation.py` file.
Both above mentioned python scripts are independent of the local file system.

## Data

The data can be found in the folder `data`. The data is structured as follows:

### Data Structure

- **Level 0**: Raw data collected from the different sensors.

- **Level 1A**: Raw data stored to NetCDF file where attributes (such as sensors used, units, description of data, etc.) are added to the data.

- **Level 1B**: Column with quality flags are added to the Level 1A data. Quality flag "1" indicates that the data point didn't pass the 
quality checks and further investigation is needed, quality flag "0" indicates that no further investiagion is needed.

## Quality assurance

Quality checks include but are not limited to range validation, data type checking and flagging missing data.

