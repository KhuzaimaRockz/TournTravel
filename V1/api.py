import requests
import pprint
pp = pprint.PrettyPrinter(indent=4)

API_KEY = '5320a6ef-8f85-42c1-9136-6cb44b98a67a'

def get_airport_data(city):
    url = f"https://airlabs.co/api/v9/suggest?api_key={API_KEY}&q={city}"
    response = requests.get(url)
    data = response.json()
    if len(data['response']['airports_by_cities']) == 1:
        IATA = data['response']['airports_by_cities'][0]['iata_code']
        return IATA
    else:  #make proper
        print()
        c = 1
        pp.pprint(data['response'])
        for airport in data['response']['airports_by_cities']:
            if airport['iata_code']:
                print(airport) #debug
                input(" press Enter.") #debug
                print(f"{c}. {airport['name']} - {airport['iata_code']} ({airport['country_code']})")
                c += 1
            else:
                print("Country doesnt exist.")
                break
        ch = int(input('Select a airport : '))
        print()
        IATA = data['response']['airports_by_cities'][ch-1]['iata_code']
        return IATA
get_airport_data('chennai')