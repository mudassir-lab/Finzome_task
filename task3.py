import requests

url = "http://127.0.0.1:8000/calculate_volatility"
files = {'file': ('NIFTY_50.xlsx', open('C:/Users/AZIMUDDIN/Downloads/NIFTY_50.xlsx', 'rb'))}

response = requests.post(url, files=files)

print(response.text)