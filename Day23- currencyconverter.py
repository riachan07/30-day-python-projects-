import json
print("This is a currency converter program.")
with open('rates.json') as file:
    rates=json.load(file)

from_currency=input("Enter the currency you want to convert from (e.g., USD, EUR): ").upper()
to_currency=input("Enter the currency you want to convert to (e.g., USD, EUR): ").upper()
amount=float(input("Enter the amount you want to convert: "))
if from_currency in rates and to_currency in rates:
    dollar =amount/rates[from_currency]
    converted_amount=dollar*rates[to_currency]
    print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}.")
else:
    print("Invalid currency code. Please check the rates.json file for valid currency codes.")


""" rates.json txt file
{
    "USD": 1.0,
    "INR": 86.2,
    "EUR": 0.92,
    "GBP": 0.79,
    "JPY": 147.6,
    "AUD": 1.53,
    "CAD": 1.37,
    "CNY": 7.18
} """ 
