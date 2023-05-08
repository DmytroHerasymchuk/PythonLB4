import os
import requests
import math

url = "https://api.coincap.io/v2/assets?limit=10"

def getCurrencies(number_of_currencies):
    url = f"https://api.coincap.io/v2/assets?limit={number_of_currencies}"
    response = requests.get(url);
    return response.json()["data"]

next_page = True
while(next_page):
    print("Enter a number of currencies you want to see")
    user_input = input()
    if(user_input.isdigit() and int(user_input) > 0):
        os.system('cls')
        list_of_currencies = getCurrencies(user_input)
        for currency in list_of_currencies:
            name = currency["name"]
            symbol = currency["symbol"]
            price = round(float(currency["priceUsd"]),5)
            print(f"{name} {symbol} \n\t Price = {price} $\n")
    else:
        print("Enter a number!")
    

    
    


   



