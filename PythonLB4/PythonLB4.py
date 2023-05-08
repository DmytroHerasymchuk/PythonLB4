import os
import requests
import msvcrt
import sys

class url_currencies_getter:
    urlBase = "https://api.coincap.io/v2/assets?limit="

    def start(self):
        while(True):
            os.system('cls')

            inputValue = input("Enter a number of currencies you want to see: ")

            if(inputValue == "exit"): sys.exit()

            if(inputValue.isdigit() and int(inputValue) > 0):
                os.system('cls')
                list_of_currencies = self.getCurrencies(inputValue)

                for currency in list_of_currencies:
                    name = currency["name"]
                    symbol = currency["symbol"]
                    price = round(float(currency["priceUsd"]),5)
                    print(f"{name} {symbol} \n\t Price = {price} $\n")
            else:
                print("You must enter a number!")
            
            print("\nEnter any button")
            msvcrt.getch()

    def getCurrencies(self, number_of_currencies):
        url = f"{self.urlBase}{number_of_currencies}"
        response = requests.get(url);
        return response.json()["data"]

def main():
    start_class = url_currencies_getter()
    start_class.start()

main()

    
    


   



