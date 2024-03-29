import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 

from sklearn.metrics import mean_squared_error
from math import sqrt
from statistics import mean 
from statsmodels.tsa.api import SimpleExpSmoothing

import warnings
warnings.filterwarnings("ignore")

train_data = pd.read_csv("/Users/paramanandbhat/Downloads/5_-_exponential_smoothing_models/data/train_data.csv")
valid_data = pd.read_csv("/Users/paramanandbhat/Downloads/5_-_exponential_smoothing_models/data/valid_data.csv")

print(train_data.shape)
print(train_data.head())

print(valid_data.shape)
print(valid_data.head())


#Required Preprocessing
train_data.timestamp = pd.to_datetime(train_data['Date'],format='%Y-%m-%d')
train_data.index = train_data.timestamp

valid_data.timestamp = pd.to_datetime(valid_data['Date'],format='%Y-%m-%d')
valid_data.index = valid_data.timestamp

plt.figure(figsize=(12,8))

plt.plot(train_data.index, train_data['count'], label='train_data')
plt.plot(valid_data.index,valid_data['count'], label='valid')
plt.legend(loc='best')
plt.title("Train and Validation Data")
plt.show()

model = SimpleExpSmoothing(np.asarray(train_data['count']))
# After fitting the model
model_fit = model.fit(smoothing_level=0.7, optimized=False)

# Forecasting future values
forecast = model_fit.forecast(steps=len(valid_data))
valid_data['SES'] = forecast



print(model.params)
plt.figure(figsize=(12,8))

plt.plot(train_data.index, train_data['count'], label='train_data')
plt.plot(valid_data.index,valid_data['count'], label='valid')
plt.plot(valid_data.index,valid_data['SES'], label='SES Forecast')
plt.legend(loc='best')
plt.title("Simple Exponential Smoothing Method")
plt.show()

# calculating RMSE 
rmse = sqrt(mean_squared_error(valid_data['count'], valid_data['SES']))
print('The RMSE value for Simple Exponential Smoothing Method is', rmse)