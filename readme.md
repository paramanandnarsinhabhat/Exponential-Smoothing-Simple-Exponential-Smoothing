

# Simple Exponential Smoothing for Time Series Forecasting

This project applies Simple Exponential Smoothing (SES) to forecast time series data, implemented in Python using the `statsmodels` library.

## Overview

The SES model is a time series forecasting method that applies exponentially decreasing weights to past observations. This repository contains scripts for preprocessing time series data, applying the SES model, and evaluating forecast accuracy using the RMSE metric.

## Project Structure

```
EXPONENTIAL-SMOOTHING-SIMPLE-EXPONENTIAL-SMOOTHING/
│
├── data/
│   ├── train/
│   │   └── train_data.csv
│   └── valid/
│       └── valid_data.csv
│
├── myenv/
│   └── ... (virtual environment files)
│
├── notebook/
│   └── Exponential smoothing models.ipynb
│
├── scripts/
│   └── time_series_simple_exponential_smoothing.py
│
├── .gitignore
├── readme.md
└── requirements.txt
```

## Requirements

- `pandas`: Data manipulation and analysis.
- `numpy`: Numerical computations.
- `matplotlib`: Data visualization.
- `scikit-learn`: Model evaluation metrics.
- `statsmodels`: Time series models.

Install the required packages using:
```
pip install -r requirements.txt
```

## Usage

1. Preprocess the data by converting date strings to datetime objects and setting them as indices.
2. Visualize the training and validation data for insights.
3. Fit the SES model and forecast future values.
4. Evaluate the forecast's accuracy with RMSE.

Run the script with:
```
python scripts/time_series_simple_exponential_smoothing.py
```

## Contributions

Feel free to fork this project, submit pull requests, or report issues.

## License

This project is open-sourced under the MIT License.

