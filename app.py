import requests

def get_exchange_rate(api_key, base_currency, target_currency):
    url = f"https://v6.exchangeratesapi.io/latest?base={base_currency}&symbols={target_currency}&access_key={api_key}"
    response = requests.get(url)
    data = response.json()
    return data

def display_exchange_rate(data, base_currency, target_currency):
    if "error" in data:
        print("Error fetching data:", data["error"])
    else:
        rate = data["rates"][target_currency]
        print(f"1 {base_currency} = {rate} {target_currency}")

def main():
    api_key = "YOUR_API_KEY"
    base_currency = input("Enter base currency (e.g., USD): ").upper()
    target_currency = input("Enter target currency (e.g., EUR): ").upper()
    exchange_data = get_exchange_rate(api_key, base_currency, target_currency)
    display_exchange_rate(exchange_data, base_currency, target_currency)

if __name__ == "__main__":
    main()
