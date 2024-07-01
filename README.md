# Alcohol Sales Forecasting

This project aims to forecast future trends or values of alcohol sales based on historical data using time series models like ARIMA. The dataset spans from January 1, 1992, to January 1, 2019, and includes monthly sales figures.

## Table of Contents

- [Introduction](#introduction)
- [Dataset](#dataset)
- [Installation](#installation)
- [Usage](#usage)
- [Exploratory Data Analysis](#exploratory-data-analysis)
- [Time Series Forecasting](#time-series-forecasting)
- [Evaluation](#evaluation)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project demonstrates the steps involved in forecasting alcohol sales using historical data. The key steps include data preparation, exploratory data analysis, model selection, forecasting, and evaluation.

## Dataset

The dataset contains the following columns:
- `DATE`: The date of the observation (monthly data).
- `sales`: Sales figures.

Example data:

```
DATE         sales
01-01-1992   3459
01-02-1992   3458
01-03-1992   4002
...
```

## Installation

To run the project, you need to install the following Python packages:

```bash
pip install pandas matplotlib statsmodels scikit-learn
```

## Usage


1. Run the Python script to perform the forecasting:

```bash
python sample.py
```

## Exploratory Data Analysis

Before fitting the model, it is crucial to visualize the data to understand its patterns, seasonality, and trends.

## Time Series Forecasting

In this project, we use the ARIMA model for forecasting. The ARIMA model parameters need to be tuned based on model diagnostics.

## Evaluation

The model's performance is evaluated using the Root Mean Squared Error (RMSE) metric.

## Contributing

Contributions are welcome! Please create a pull request or submit an issue to discuss any changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

