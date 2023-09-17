import requests
import pprint
pp = pprint.PrettyPrinter(indent=4)

API_KEY = '5320a6ef-8f85-42c1-9136-6cb44b98a67a'

# def get_airport_data(city):
#     url = f"https://airlabs.co/api/v9/suggest?api_key={API_KEY}&q={city}"
#     response = requests.get(url)
#     data = response.json()
#     if len(data['response']['airports_by_cities']) == 1:
#         IATA = data['response']['airports_by_cities'][0]['iata_code']
#         return IATA
#     else:  #make proper
#         print()
#         c = 1
#         #pp.pprint(data['response'])

def get_airport_data(city):
    url = f"https://airlabs.co/api/v9/suggest?api_key={API_KEY}&q={city}"
    response = requests.get(url)
    data = response.json()
    airports = data['response']['airports_by_cities'] + data['response']['airports_by_countries']
    if len(airports) == 1:
        return airports[0]['iata_code']
    else:
        for i, airport in enumerate(airports, start=1):
            try:
                print(f"{i}. {airport['name']} ({airport['iata_code']})")
            except KeyError as Ke:
                pass

    ch = int(input('Select an airport : '))
    return airports[ch-1]['iata_code']
    


# x = input("Enter destination : ")
# haha = get_airport_data(x)
# print(haha)