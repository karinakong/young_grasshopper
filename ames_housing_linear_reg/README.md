# Linear Regression Model to Predict House Prices using the Ames Housing Dataset

## Problem Statement
We are employees of a real estate agency in Ames, Iowa who have been tasked with doing market research for the company to find out the features of a house that are the strongest predictors of the sale price of the house and the magnitude to which these features affect the sale price of the house.

This project aims to create a linear, LASSO and Ridge regression model, comparing these models to find the best model, determined by R2 and RMSE, to predict house prices using various factors from the Ames Housing Dataset.

This information can help our company’s agents determine a fair price range for each house and highlight the strongest features of each house they sell in order to maximise selling price for our customers.

## Conclusion and Findings

The Lasso regression model produced the best test R2 and RMSE scores. This makes sense since the Lasso model is known to perform well with datasets that have many features as it has a penalty term that zeroes out/reduces the coefficients of many features, which leave only the most useful features.

Based on Lasso regression, the strongest positive predictors of SalePrice are

`Gr Liv Area`: Above grade (ground) living area square feet
`Overall Qual`: Rating of the overall material and finish of the house
The type of neighbourhood the house is located in
`Garage Cars`: Size of garage in car capacity
`Bsmt Full Bath`: The number of full bathrooms in the basement
`Full Bath`: The number of full bathrooms above ground
`Screen Porch`: Screen porch area in square feet

Our company's real estate agents can use this information to get estimate a price for each house and ensure that our customers sell their house at a good market price. In addition, based on this information, our company can start collecting this data on the houses we sell to start our own database for future predictions.

## Limitations of the model 
However, as with every model, this model has limitations as well. 

1. Assumption of linearity between the response variable, `SalePrice`, and the features. Real world data like the Ames housing dataset rarely has a straight-line relationship between the dependent and independent variables. 

2. In reality, there can be many outliers for `SalePrice` and the model would not be able to predict the prices of such outliers accurately since outliers are removed when training the model. 

3. This model is specific to Ames and may not be useful to predict house prices in other towns. 

## For Reference: Data Dictionary

This data dictionary describes the features in the training dataset.

|Feature|Data Type|Description|
|---|---|---|
|MS SubClass|Nominal|Identifies the type of dwelling involved in the sale|
|MS Zoning|Nominal|Identifies the general zoning classification of the sale|
|Lot Frontage|Continuous|Linear feet of street connected to property|
|Lot Area|Continuous|Lot size in square feet|
|Street|Nominal|Type of road access to property|
|Lot Shape|Ordinal|General shape of property|
|Land Contour|Nominal|Flatness of the property|
|Utilities|Ordinal|Type of utilities available|
|Lot Config|Nominal|Lot configuration|
|Land Slope|Ordinal|Slope of property|
|Neighborhood|Nominal|Physical locations within Ames city limits (map available)|
|Condition 1|Nominal|Proximity to various conditions|
|Condition 2|Nominal|Proximity to various conditions (if more than one is present)|
|Bldg Type|Nominal|Type of dwelling|
|House Style|Nominal|Style of dwelling|
|Overall Qual|Ordinal|Rates the overall material and finish of the house|
|Overall Cond|Ordinal|Rates the overall condition of the house|
|Year Remod/Add|Discrete|Remodel date (same as construction date if no remodeling or additions)|
|Roof Style|Nominal|Type of roof|
|Roof Matl|Nominal|Roof material|
|Exterior 1|Nominal|Exterior covering on house|
|Exterior 2|Nominal|Exterior covering on house (if more than one material)|
|Mas Vnr Type|Nominal|Masonry veneer type|
|Mas Vnr Area|Continuous|Masonry veneer area in square feet|
|Exter Qual|Ordinal|Evaluates the quality of the material on the exterior|
|Exter Cond|Ordinal|Evaluates the present condition of the material on the exterior|
|Foundation|Nominal|Type of foundation|
|Bsmt Qual|Ordinal|Evaluates the height of the basement|
|Bsmt Cond|Ordinal|Evaluates the general condition of the basement|
|Bsmt Exposure|Ordinal|Refers to walkout or garden level walls|
|BsmtFin Type 1|Ordinal|Rating of basement finished area|
|BsmtFin SF 1|Continuous|Type 1 finished square feet|
|BsmtFinType 2|Ordinal|Rating of basement finished area (if multiple types)|
|BsmtFin SF 2|Continuous|Type 2 finished square feet|
|Bsmt Unf SF|Continuous|Unfinished square feet of basement area|
|Total Bsmt SF|Continuous|Total square feet of basement area|
|Heating|Nominal| Type of heating|
|HeatingQC|Ordinal|Heating quality and condition|
|Central Air|Nominal|Central air conditioning|
|Electrical|Ordinal|Electrical system|
|1st Flr SF|Continuous|First Floor square feet|
|2nd Flr SF|Continuous|Second floor square feet|
|Low Qual Fin SF|Continuous|Low quality finished square feet (all floors)|
|Gr Liv Area|Continuous|Above grade (ground) living area square feet|
|Bsmt Full Bath|Discrete|Basement full bathrooms|
|Bsmt Half Bath|Discrete|Basement half bathrooms|
|Full Bath|Discrete|Full bathrooms above grade|
|Half Bath|Discrete|Half baths above grade|
|Bedroom|Discrete|Bedrooms above grade (does NOT include basement bedrooms)|
|Kitchen|Discrete|Kitchens above grade|
|KitchenQual|Ordinal|Kitchen quality|
|TotRmsAbvGrd|Discrete|Total rooms above grade (does not include bathrooms)|
|Functional|Ordinal|Home functionality|
|Fireplaces|Discrete|Number of fireplaces|
|FireplaceQu|Ordinal|Fireplace quality|
|Garage Type|Nominal|Garage location|
|Garage Yr Blt|Discrete|Year garage was built|
|Garage Finish|Ordinal|Interior finish of the garage|
|Garage Cars|Discrete|Size of garage in car capacity|
|Garage Area|Continuous|Size of garage in square feet|
|Garage Qual|Ordinal|Garage quality|
|Garage Cond|Ordinal|Garage condition|
|Paved Drive|Ordinal|Paved driveway|
|Wood Deck SF|Continuous|Wood deck area in square feet|
|Open Porch SF|Continuous|Open porch area in square feet|
|Enclosed Porch|Continuous|Enclosed porch area in square feet|
|3-Ssn Porch|Continuous|Three season porch area in square feet|
|Screen Porch|Continuous|Screen porch area in square feet|
|Pool Area|Continuous|Pool area in square feet|
|Pool QC|Ordinal|Pool quality|
|Fence|Ordinal|Fence quality|
|Sale Type|Nominal|Type of sale|
|Sale Condition|Nominal|Condition of sale|
|SalePrice|Continuous|Sale price|
