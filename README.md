# COMS W4995 Applied ML Team 22 Final Project: MALWARE DETECTION ON WINDOWS MACHINES USING MACHINE LEARNING APPROACHES

This project investigates machine learning approaches to detect the presence of malware on Windows machines. 

Data Source: https://www.kaggle.com/competitions/microsoft-malware-prediction/data

## Required Packages

- Pandas
- Scikit-Learn
- Matplotlib
- Seaborn
- Numpy
- Tensorflow
- Keras-tuner

## Execution Instructions

### Data Preparation

Note: you may choose to skip the following steps and use the `dev_small.csv` that we included in our submission. 

1. Download the dataset from Kaggle using the link above. Then, place the `train.csv` file under the `data/` directory in this project. 
2. From the project's root directory (`aml_project_team_22/`), execute the sampling script using `python3 sampling.py` This will generate the small dataset that's used throughtout later parts in the project.

### Explorative Data Analysis

We've created the following Jupyter Notebooks for performing Explorative Data Analysis (located under the `EDA` directory):

- `ead_final.ipynb`: This notebook contains all content for the Explorative Data Analysis process, from data cleaning to the final model selection. We only included a subset of visualization graphs in this notebook for clarity.

- `data_visualization.ipynb`: This notebook contains all figures we created for the data visualization process. It also includes addition analysis on the feature characteristics.

These notebooks are parallel and can be executed in any order.

### Model Training

We trained 4 different models and investigated their performance on performing classification on the dataset. Each of the following notebooks (located under the `models` directory) represents a model we trained:

- `knn.ipynb`
- `random_forest.ipynb`
- `xgboost.ipynb`
- `neural_network.ipynb`

These notebooks are parallel and can be executed in any order.