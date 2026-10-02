import requests

amount = float(input("Enter amount: "))
from_currency = input("From currency (USD/INR/EUR): ").upper()
to_currency = input("To currency (USD/INR/EUR): ").upper()

url = f"https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}"

response = requests.get(url)
data = response.json()

if "rates" in data:
    result = data["rates"][to_currency]

    print("\n----- Currency Converter -----")
    print("Amount:", amount, from_currency)
    print("Converted:", result, to_currency)
else:
    print("Invalid currency or conversion failed.")