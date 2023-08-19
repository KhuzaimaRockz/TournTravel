import requests
API_KEY = '5320a6ef-8f85-42c1-9136-6cb44b98a67a'



city = input("Enter city test : ")

def search_city(city):  # Getting API response
    url = f"https://airlabs.co/api/v9/suggest?api_key={API_KEY}&q={city}"
    response = requests.get(url)
    data = response.json()
    return data

testdata = search_city(city)
airports = testdata['response']['airports']
air_list = []

print("Did u mean:")
for i, dict in enumerate(airports, start=1):
    print(f"{i} . ({dict['name']}, IATA: {dict['iata_code']})")
    air_list.append(dict['iata_code'])

choice = int(input("Enter choice: "))  # Get user input
mycity = air_list[choice-1]  # Subtract 1 because list indices start at 0
print(mycity)