import requests

def get_crypto_data(url):
    # Send HTTP GET request to the specified URL
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        data = response.json()  # Parse JSON response
        
        # Extract cryptocurrency name and price from the data
        crypto_name = data['data']['1']['name']  # Example: '1' may not be the correct key
        crypto_price = float(data['data']['1']['quotes']['USD']['price'])
        
        # Print cryptocurrency information
        print(f"Name: {crypto_name}")
        print(f"Price (USD): {crypto_price}")
    else:
        print(f"Failed to retrieve data from {url}")

# Crypto API URLs
btc_url = "https://api.alternative.me/v2/ticker/Bitcoin/?convert=USD"
eth_url = "https://api.alternative.me/v2/ticker/Ethereum/?convert=USD"

# Get Bitcoin information
print("Bitcoin Information:")
get_crypto_data(btc_url)

# Get Ethereum information
print("\nEthereum Information:")
get_crypto_data(eth_url)
