import requests

API_KEY = '5320a6ef-8f85-42c1-9136-6cb44b98a67a'

def get_airport_data(city):
    url = f"https://airlabs.co/api/v9/suggest?api_key={API_KEY}&q={city}"
    response = requests.get(url)
    data = response.json()
    if len(data['response']['airports_by_cities']) == 1:
        IATA = data['response']['airports_by_cities'][0]['iata_code']
        return IATA
    else:
        c = 1
        for airport in data['response']['airports_by_cities']:
            print(f"{c}. {airport['name']} - {airport['iata_code']} ({airport['country_code']})")
            c += 1
        ch = int(input('Select a airport : '))
        IATA = data['response']['airports_by_cities'][ch-1]['iata_code']
        return IATA
ch = input()