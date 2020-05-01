import requests
from box import Box

# Euro foreign exchange reference rates
response = requests.get("https://api.exchangeratesapi.io/latest?symbols=CAD,GBP,PLN")
b = Box(response.json())
print("1 EUR is worth ", b.rates.CAD, " CAD")
print("1 EUR is worth ", b.rates.GBP, " GBP")
print("1 EUR is worth ", b.rates.PLN, " PLN")
