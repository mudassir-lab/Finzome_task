import pandas as pd 
import numpy as np 

data = pd.read_excel('C:/Users/AZIMUDDIN/Downloads/NIFTY_50.xlsx')
# print(data.columns)

# Adding daily returns in dataframe
data['Daily Returns'] = (data['Close '] / data['Close '].shift(1)) - 1
# print(data)

# Calculate daily volatility
daily_volatility = data['Daily Returns'].std()

# Calculate annualized volatility
length_of_data = len(data)
annualized_volatility = daily_volatility * np.sqrt(length_of_data)


print(f'Daily Volatility: {daily_volatility:.3f}')
print(f'Annualized Volatility: {annualized_volatility:.3f}')