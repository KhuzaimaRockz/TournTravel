import requests
API_KEY = '5320a6ef-8f85-42c1-9136-6cb44b98a67a'

import requests

city = input("Enter city test : ")

def search_city(city):  # Getting API response
    url = f"https://airlabs.co/api/v9/suggest?api_key={API_KEY}&q={city}"
    response = requests.get(url)
    data = response.json()
    return data['suggestions']

testdata = search_city(city)

print("Did u mean:")
for i, dict in enumerate(testdata, start=1):
    print(f"{i} . {dict['value']} ({dict['country']}, IATA: {dict['iata']})")

choice = int(input("Enter choice: "))  # Get user input
mycity = testdata[choice-1]['value']  # Subtract 1 because list indices start at 0
print(mycity)