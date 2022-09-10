#This is a currency convertor
import os
import requests
import json

os.system('cls' if os.name =='nt' else 'clear')

fromCurrency=input('Enter the currency to change From: ').upper()
toCurrency=input('Enter the currency you want to change To: ').upper()
amountCurrency=input('Enter the amount: ').upper()

url=f'https://api.apilayer.com/exchangerates_data/convert?to={toCurrency}&from={fromCurrency}&amount={amountCurrency}'

payload = {}
headers= {
  "apikey": "etyNHsQBAiXRTR2irf0ARTV7cNXzf3L0"
}

response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code
#result = response.text

#Convert the result from json to Dictionary
resultDict=json.loads(response.text)
#print(resultDict)

finalResult=resultDict['result']
print(f'{amountCurrency} {fromCurrency} is equal to {finalResult} {toCurrency}!')

