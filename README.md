# elec-inspec-protec
## Contents

 * [Data](#data)
 * [Geo](#geo)
 * [Data Pipeline](#data-pipeline) 
 * [Decision Tree](#decision-tree)
 * [Logistic Regression](#logistic-regression)
 * [Light GBM](#light-gbm)
 * [Writeups](#writeups)
 * [Figures](#figures)

 Warning: Due to reorganization/cleaning of the folder at the end of the project, file addresses hard-coded in some of the scripts and notebooks may need modification.

 #### Data

 This folder contains CSVs saving intermediate and final results for our model and analysis Jupyter notebooks.
 Note that some of the raw data sources, such as the raw Census demographic data, are not included.

 #### Geo

 + [mi_acs5_2018_bg](data_pipeline/mi_acs5_2018_bg) contains shapefiles for Census block groups in Michigan in 2018
 + [MI_VTDs_2020](data_pipeline/MI_VTDs_2020) contains shapefiles for Census VTDs in Michigan in 2020

 #### Data Pipeline

 + [census_precinct_data.ipynb](data_pipeline/census_precinct_data.ipynb) is a Jupyter notebook used to convert ACS data from block group level to precinct level and prepare the feature variables. This notebook includes maps of the feature variables across Michigan.
 + [input_preprocessing.ipynb](data_pipeline/input_preprocessing.ipynb) is a Jupyter notebook used to convert ACS data from block group level to county level and prepare the feature variables. (Used for midpoint / baseline training.)
 + [join_vtd_precinct.ipynb](data_pipeline/join_vtd_precinct.ipynb) is a Jupyter notebook used to match Census-labeled "VTDs" (voter tabulation districts) to Michigan-label precincts.
 + [ylabel_data_prep.ipynb](data_pipeline/ylabel_data_prep.ipynb) is a Jupyter notebook used to match candidates from the DIME dataset to Michigan voting results and prepare weighted ideology scores and classifications from the matches.
 + [mapping.ipynb](data_pipeline/mapping.ipynb) is a Jupyter notebook used to map and otherwise analyze outputs from our models.

 #### Decision Tree

 + [decision-tree-basic.ipynb](decisiontree/decision-tree-basic.ipynb) is a Jupyter notebook used to train and test our decision tree and random forest models.
 + [decisiontree.py](decisiontree/decisiontree.py) is a script implementation.

 #### Logistic Regression

 + [ml_test.ipynb](mult_logreg/ml_test.ipynb) is a Jupyter notebook used to train and test our logistic regression models.
 + [mlr.py](mult_logreg/mlr.py) is a script implementation.

 #### Light GBM

 + [light.ipynb](lgbm/acs_aggregate_analysis.ipynb) is a Jupyter notebook used to train and test our Light GBM models.

 #### Writeups

 This folder contains the text of our midpoint and final writeups.

 #### Figures

 This folder contains maps of the demographic features (as well as a feature correlation matrix) and of several of our models' predictions, including expanding beyond our dataset to all of Michigan's precincts.