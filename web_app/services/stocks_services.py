# web_app/services/stocks_service.py

import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("ALPHAADVANTAGE_API_KEY")

symbol = "AAPL"
#symbol = input("Plesae choose a symbol like 'AAPL': ")
print("SYMBOL:", symbol)

request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}"
print(request_url)

response = requests.get(request_url)
print(type(response)) #> <class 'requests.models.Response'>
print(response.status_code) #> 200
print(type(response.text)) #> <class 'str'>

parsed_response = json.loads(response.text)
print(type(parsed_response)) #> <class 'dict'>

latest_close = parsed_response["Time Series (Daily)"]["2020-04-23"]["4. close"]
print("LATEST CLOSING PRICE:", latest_close)

