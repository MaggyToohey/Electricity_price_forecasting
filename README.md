# Electricity Price Forecasting

Capstone project for the Udacity Nanodegree.

## Overview

Linear learner model for the prediction of the day ahead price of electricity, given the forecasted load and wind generation for the same region. The model used is the Linear Learner algorithm from Amazon SageMaker, more information on the Linear Learner algortihm available here: https://docs.aws.amazon.com/sagemaker/latest/dg/linear-learner.html. 

The project was implemented on a Jupyter notebook running on an SageMaker notebook instance. The model implemented here is benchmarked against an industry standard linear prediction model, LEAR (Linear Estimated Auto-Regulated) model, on the same dataset. The accuracy of the model and the bencmark model is calculated using the MAPE, MAE and RMSE metrics.

## Data

The data used is historical day ahead price, load and wind generation forecast for the Nordic countries, from the NordPool group. NordPool is the largest electricity market in Europe, and this dataset contains 6 years of data in hourly increments. The data is freely available from the NoidPool website: https://www.nordpoolgroup.com/historical-market-data/. The data is described in more detail here: https://sandbox.zenodo.org/record/632147. The first four years of data were used for training, and the final 2 years of the set for testing.

## Requirements

### 1. Amazon SageMaker

The model is based on Amazon SageMaker's Linear Learner algorithm, and the implementation was carried out on a SageMaker notebook instance, running a Python3 kernel.

### 2. EPF Toolbox

The EPF Toolbox [1] has been created specifically as a platform for evaluating deep learning and linear forecasting algorithms. This toolbox is available from git. The toolbox has been used in this project for benchmarking and model validation.

#### Installing EPF Toolbox
1. Inside a SageMaker notebook instance, clone the epftoolbox repo `git clone https://github.com/jeslago/epftoolbox.git`
2. From the terminal, activate the environment that the Jupyter notebook runs in using `conda activate <env>`
3. Change directory into the epftoolbox dir
4. Install the toolbox using `pip install .`
5. Deactivate the conda environment using `conda deactivate`

## References
1. Jesus Lago, Grzegorz Marcjasz, Bart De Schutter, Rafał Weron. "Forecasting day-ahead 
electricity prices: A review of state-of-the-art algorithms, best practices and an 
open-access benchmark". *Renewable and Sustainable Energy Reviews* (2020). Under Review.
