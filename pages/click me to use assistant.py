import requests

# Define the endpoint you're accessing
endpoint_url = "https://api.openai.com/v1/your_endpoint"

# Set your API key
api_key = "YOUR_API_KEY_HERE"

# Set the headers with the API key
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# Make a sample request to check authentication
response = requests.get(endpoint_url, headers=headers)

# Check the response status code
if response.status_code == 200:
    print("Authentication successful!")
    # Proceed with your code for making requests
    # ...
else:
    print("Authentication failed. Check your API key and headers.")
