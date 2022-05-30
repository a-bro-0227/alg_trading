
# library bank -----
import pandas as pd
import numpy as np
import requests
import xlsxwriter
import math

# importing list of stocks ----

stocks = pd.read_csv("starter_files/sp_500_stocks.csv")
stocks

# IEX_CLOUD_API_TOKEN = "Tpk_059b97af715d417d9f49f50b51b1c448"

symbol = "AAPL"
# https://iexcloud.io/docs/api/
api_url = f"https://sandbox.iexapis.com/stable/stock/{symbol}/quote?token={IEX_CLOUD_API_TOKEN}"
api_url

data = requests.get(api_url)

data.status_code
