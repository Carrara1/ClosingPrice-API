import requests
import json
import os

def get_stock_data(symbol, api_key):

#   Esta função obtém o preço de fechamento de uma ação específica.
#   Args:
#       símbolo (str): Símbolo da ação (ex: PBR, VALE, BBD)
#       chave_api (str): Chave de API do Alpha Vantage

#     # URL base da API do Alpha Vantage
    base_url = "https://www.alphavantage.co/query"
    function = "TIME_SERIES_DAILY"
    datatype = "json"

  # Parâmetros da requisição
    params = {
        "function": function,
        "symbol": symbol,
        "apikey": api_key,
        "datatype": datatype
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    latest_trading_day = max(data["Time Series (Daily)"].keys())

    closing_price = data["Time Series (Daily)"][latest_trading_day]["4. close"]



    return closing_price
# Busca a chave da API do ambiente (variável de ambiente)
api_key = os.getenv('MY_API_KEY')
symbols = ["PBR", "VALE", "BBD"]

for symbol in symbols:
    closing_price = get_stock_data(symbol, api_key)
    print(f"The closing price of {symbol} on the most recent trading day was {closing_price}.")
