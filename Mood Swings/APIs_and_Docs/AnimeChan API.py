import requests

# Base URL for AnimeChan API
API_URL = "https://animechan.xyz/api/random"

def fetch_random_quote():
    try:
        # Send a GET request to the AnimeChan API
        response = requests.get(API_URL)
        response.raise_for_status()  # Raise an error for bad HTTP responses (4xx, 5xx)
        
        # Parse the JSON response
        data = response.json()
        print(f"Anime: {data['anime']}")
        print(f"Character: {data['character']}")
        print(f"Quote: {data['quote']}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

# Test the function
if __name__ == "__main__":
    fetch_random_quote()

response = requests.get(api_url)
if response.status_code == 200:
    try:
        data = response.json()
    except ValueError:
        print("Invalid JSON received.")
else:
    print(f"Error: {response.status_code}")
