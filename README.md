# <span style=color:#FA7528> Water System <span>
![output](https://user-images.githubusercontent.com/92168021/233785853-56913452-2507-4cff-b611-8633a668f919.png)<br>

This is a project for the course GEO374.


Data: https://www.datalakes-eawag.ch/

# Data_cleaning.ipynb
  
##  <span style=color:#7fc97f>Description of the Output (Quality Flags)</span>
### The file will outputed in "./data/cleaned_data/currentDate/currentDate_name_Category.csv"
There exist different Quality Flags:
0A: Raw Data, downloaded from Datalakes with same timestamps
<br>
1A: Physical Outlier corrected (imputed): New column "Quality" with was_outlier(imputed)/no_outlier -> 1/0 <br>
1B: Physical Outlier deleted
 <br>
2A: Time-Series corrected (and outlier corrected) (imputed): New column "Quality" with was_outlier/no_outlier ->1/0 <br>
2B: Time-Series (and physical) deleted
<br>
3A: 2A + statistical outlier selection imputed -> New column "Quality" with was_outlier/no_outlier ->1/0 <br>
3B: 2B + statistical outlier selection deleted
 <br>
4A: Scaled Dataset (from 2A) for ML-Algorithms <br>
4B: Scaled Dataset (from 2B) for ML-Algorithms
  <br>
### 


Naming of Datasets (CSV):
"./data/cleaned_data/currentDate/currentDate_name_Category.csv", <br> e.g.
".\data\cleaned_data\230422\230422_LakeAegeri_3A.csv" <br>
It is from Lake Aegeri, created on 22.04.2023, with the quality Flag 3A (see above)
  
<br>
  

  
## <span style=color:#7fc97f>Description of the Class Data</span>
#### The class has 2 inputs: A Pandas DataFrame and a name:

--> To create an instance ot the Class Data, use following lines:
```json
dataframe = pd.read_csv("PATH TO DATA")
name="DESIRED NAME"
LakeAegeri=Data(dataframe,name)
```
<br>
<br>

#### <span style=color:#7fc97f>The Class has various methods:</span> <br>
#####  <span style=color:#386cb0>1. The INSTANCE_CLASS_DATA.calc_rolling_statistics(column,window,plot="n",save_plot="n")</span>
This method will calculate the rolling statistics and outputs a plot.

If you don't want the plot plotted in the notebook, use show_plot="n".

If you want to save the plot in the /data/output/.. folder:
- save_plot="y" -> It asks you to input a name without a space.
- save_plot="CUSTOM_NAME" -> It creates a plot with the name CUSTOM_NAME in the specified folder
- save_plot="n": It will not save the created figure
If you want to define the rolling window, use window=INTEGER
<br>
<br>

##### <span style=color:#386cb0>2. The INSTANCE_CLASS_DATA.check_stationarity(column):</span>
This method will check the stationarity using the Augmented Dickey-Fuller Test (ADF). As an input use the column you want the stationarity checked on.
We dont need this method.
<br>
<br>

##### <span style=color:#386cb0>3. INSTANCE_CLASS_DATA.detect_outlier(self, column, pchip_imputation="y", PERIOD=24, display_plots="y"):</span>

This method will clean the data with help of the seasonal decomposition of the specified column (column=COLUMN_NAME).<br>

The method returns an instance of the class Data (with the whole DataFrame with the (timeseries) cleaned column). The physical impossible outliers are not cleaned in this method.<br>

If you want the more "fancy" PChip (Piecewise Cubic Hermite Interpolating Polynomial) Imputation, use pchip_imputation="y". It looks at outlier and puts a mathematical function over the dataset. The method estimates values that minimize overall curvature, thus obtaining a smooth surface passing through the input points. Spline interpolation is computationally efficient and can be used to interpolate large datasets quickly and accurately. Otherwise, use pchip_imputation="n" to use the simple imputer: It looks at the normalized residuals and sets >3 values to 3 and <-3 values to -3. In the last step. If you want to delete the outliers, use pchip_imputation="delete". Note, that many data is lost due to this process, because it will delete the entire column.<br>

PERIOD: If you want to change the period of the data, change the PERIOD parameter.<br>

Display plots in the notebook: If you want to display the plots, use display_plots="y", else display_plots="n"
<br>
<br>

##### <span style=color:#386cb0>4. INSTANCE_CLASS_DATA.remove_outliers_temperature(self, skin_column_name="y", bulk_column_name="y1", airtemp_column_name="air_temp", imputation="y"):</span>

This method will clean the physically impossible outliers of the skin, bulk and air temperatures.

skin_column_name="XXX" : input the name of the skin temperature column
bulk_column_name="XXX" : input the name of the bulk temperature column
airtemp_column_name="XXX" : input the name of the air temperature column

imputation="y": If you want the physically impossible values imputed, make imputation="y". The imputation method is the PChip (Piecewise Cubic Hermite Interpolating Polynomial) method. It looks at outlier and puts a mathematical function over the dataset. The method estimates values that minimize overall curvature, thus obtaining a smooth surface passing through the input points. Spline interpolation is computationally efficient and can be used to interpolate large datasets quickly and accurately.
imputation="n": If you want the physically impossible values deleted, use imputation="n". Note, that many data is lost due to this process, because it will delete the entire column.
<br>
<br>

##### <span style=color:#386cb0>5. Instance_CLASS_DATA.remove_outliers_static(self, column_name, imputation="y"):</span>

This method will remove the statistical outliers of a column. Note, that this column will not look at the seasonality in the data, and will use the normalized values of the selected column (column_name="XXX") to determine the outliers.

If the Z-Score (COLUMN_VALUE-mean/std) exceeds 3 (or -3), the point will be considered as an outlier.
-> If you want to impute the missing data with the Splines Imputation, use imputation = "y", else imputation = "n". The  PChip (Piecewise Cubic Hermite Interpolating Polynomial) Imputation looks at the missing points (here the outliers) and puts a mathematical function over the dataset. The method estimates values that minimize overall curvature, thus obtaining a smooth surface passing through the input points.  PChip interpolation is computationally efficient and can be used to interpolate large datasets quickly and accurately.
<br>
<br>

##### <span style=color:#386cb0>6. Instance_CLASS_DATA.rename_columns(self,columns={"y": "skin_temp", "y1": "bulk_temp"}): </span>

This method will rename the columns of the instance. With a dictionary, the columns can be added by {"name_before":"name_after",...}
<br>
<br>

##### <span style=color:#386cb0>7. Instance_CLASS_DATA.create_histogram(self,column_name): </span>
This method creates a histogram from the selected column. It also adds the Kernel Denstity Estimation (KDE) onto the histogram.
<br>
<br>

##### <span style=color:#386cb0>8. create_paiplot(self,column_names=[]) </span>
This method will create a pairplot of the selected columns (column_names=["column1","column2",...]). <br> If the parameter column_names is not defined, the whole dataset will be plotted as a pairplot.
<br>
<br>

# Physical_Model_simple.ipynb
  ![Unbenannt](https://user-images.githubusercontent.com/92168021/233786239-d07e8443-1a90-417f-8ae3-7cc6477437e6.PNG)<br>
  ![Unbenannt](https://user-images.githubusercontent.com/92168021/233786284-cd1514e7-542b-4610-ac9b-907416ada12a.PNG)


This model will use the approach described in [1] Wilson, R.C. et al. (2013) ‘Skin and bulk temperature difference at Lake Tahoe: A case study on lake skin effect’, Journal of Geophysical Research Atmospheres, 118(18), pp. 10,332-10,346. Available at: https://doi.org/10.1002/jgrd.50786.<br>
The .csv files from the file DataCleaning will be used to make this model. This file is function-oriented.
