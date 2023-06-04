# <span style=color:#FA7528> Water System <span>
![output](https://user-images.githubusercontent.com/92168021/233785853-56913452-2507-4cff-b611-8633a668f919.png)<br>

This is a project for the course GEO374.


Data: https://www.datalakes-eawag.ch/

# Description of the files used:
- Data_Cleaning.ipynb: <br>
  This Jupyter file introduces a Class Data, which will visualize/plot and clean the data into the quality flags explained in the final report. It uses differenc cleaning mechanism and can be customized to e.g. only clean certain amount of the data.
  
- Skin_effect_matchp.ipynb: <br>
  This Jupyter file preprocess the data in order to be further processed in the Data_Cleaning.ipynb
  
- Time_matchup.ipynb <br>
  This Jupyter file combines the metreological data with the data obtained from Eawag to further be processed into the Data_Cleaning.ipynb
  
- physicalModelEasy.ipynb:<br>
  In this Jupyter file there is the simple model from Minnett et al (2011).
  
- PhysicalModelLambda.ipynb <br>
  In this Jupyter file there is the more advanced model from Saunders (1967) and Wilson et al (2013).
