import requests
import json

# Define the API endpoint
url = 'https://airlabs.co/api/v7/schedules?api_key=your_api_key'

# Send a GET request to the API endpoint
response = requests.get(url)

# If the GET request is successful, the status code will be 200
   # Parse the response as JSON
data = json.loads(response.text)

# Check if the key is present in the response
if 'your_key' in data:
    # Access the value of the key
    for flight in data['your_key']:
        print(f"Flight from {flight['departure_airport']} to {flight['arrival_airport']} on {flight['flight_date']}")
else:
    print("Key not found in the response")
