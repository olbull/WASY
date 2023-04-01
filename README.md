# WASY
This is a project for the course GEO374

DATACLEANING
## Description of the Class Data
#### The class has 2 imputs: A Pandas DataFrame and a name:

--> To create an instance ot the Class Data, use following lines:
```json
dataframe = pd.read_csv("PATH TO DATA")
name="DESIRED NAME"
LakeAegeri=Data(dataframe,name)
```

#### The Class has various methods:
##### 1. The INSTANCE_CLASS_DATA.calc_rolling_statistics(column,window,plot="n",save_plot="n")
This method will calculate the rolling statistics and outputs a plot.

If you don't want the plot plotted in the notebook, use show_plot="n".

If you want to save the plot in the /data/output/.. folder:
- save_plot="y" -> It asks you to input a name without a space.
- save_plot="CUSTOM_NAME" -> It creates a plot with the name CUSTOM_NAME in the specified folder
- save_plot="n": It will not save the created figure
If you want to define the rolling window, use window=INTEGER


##### 2. The INSTANCE_CLASS_DATA.check_stationarity(column)
This method will check the stationarity using the Augmented Dickey-Fuller Test (ADF). As an input use the column you want the stationarity checked on.


##### 3. INSTANCE_CLASS_DATA.detect_outlier(column,knn_imputation="y",PERIOD=24,display_plots="y"):
This method will clean the data with help of the seasonal decomposition of the specified column (column=COLUMN_NAME). The method returns a (TimeSeries) cleaned DataFrame with the selected column. The physical impossible outlier are not cleaned in this method.

If you want the more "fancy" K-nearest Neighbours Algorithm Imputation, use knn_imputation="y". It looks at the 4 neighbours of the outlier and calculates an optimal value to replace the outlier. Otherwise, use knn_imputation="n" to use the simple imputer: It looks at the normalized residuals and sets >3 values to 3 and <-3 values to -3. In the last step.

PERIOD: If you want to change the period of the data, change the PERIOD parameter.

Display plots in the notebook: If you want to display the plots, use display_plots="y", else display_plots="n"

##### 4. INSTANCE_CLASS_DATA.outlier_physical()...
