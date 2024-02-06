import json
import urllib3

# Disable warnings from urllib3
urllib3.disable_warnings()

# URL to the raw JSON file on GitHub
url = 'https://raw.githubusercontent.com/web3projectlinks/web3projectlinks/main/src/app/database/ethereum.json'

# Create a PoolManager instance
http = urllib3.PoolManager()

# Send a GET request to fetch the JSON data
response = http.request('GET', url)

# Decode the response data
myData = response.data.decode('utf-8')

# Parse the JSON data
parsedJson = json.loads(myData)

# List to store extracted URLs
extracted_urls = []

# Function to recursively extract URLs from JSON data
def extract_urls(data):
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, str) and value.startswith("http"):
                extracted_urls.append(value)
            elif isinstance(value, (dict, list)):
                extract_urls(value)
    elif isinstance(data, list):
        for item in data:
            extract_urls(item)

# Extract URLs from the parsed JSON data
extract_urls(parsedJson)

# Remove duplicate URLs
extracted_urls = list(set(extracted_urls))

# Write the extracted URLs into polygon.json
with open('polygon.json', 'w') as file:
    json.dump(extracted_urls, file, indent=4)

print("URLs have been extracted and saved into polygon.json file.")
