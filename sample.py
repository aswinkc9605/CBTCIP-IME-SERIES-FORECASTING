import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error

data=pd.read_csv("Alcohol_Sales.csv")
data['DATE']=pd.to_datetime(data['DATE'],format='%Y-%m-%d')
data.set_index('DATE',inplace=True)
print(data.head())

plt.figure(figsize=(10,6))
plt.plot(data.index,data['sales'],marker='o',linestyle='-')
plt.title('Monthly Alcohol Sales')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.grid(True)
plt.show()

model=ARIMA(data['sales'],order=(1,1,1))
model_fit=model.fit()
forecast=model_fit.forecast(steps=12)
actual_views=data['sales'].iloc[-12:].values
rmse=mean_squared_error(actual_views,forecast)**0.5
print(f'RMSE:{rmse}')

plt.figure(figsize=(10,6))
plt.plot(data.index[-12:],actual_views,label='Actual')
plt.plot(data.index[-12:],forecast,label='Forecast')
plt.title('ARIMA Forecast')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.legend()
plt.grid(True)
plt.show()
