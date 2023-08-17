import requests

API_KEY = '5320a6ef-8f85-42c1-9136-6cb44b98a67a'

def get_airport_data(city):
    url = f"https://airlabs.co/api/v9/suggest?api_key={API_KEY}&q={city}"
    
    response = requests.get(url)
    data = response.json()
    for airport in data['response']['airports_by_cities']:
        print(f"Airport: {airport['name']}")
        print(f"Latitude: {airport['lat']}")
        print(f"Longitude: {airport['lng']}")
        
        LAT = float(str({airport['lat']})[1:-1])
        LNG = float(str({airport['lng']})[1:-1])
        
    
    url = f"https://airlabs.co/api/v9/nearby?lat={LAT}&lng={LNG}&distance=20&api_key=5320a6ef-8f85-42c1-9136-6cb44b98a67a"
    response = requests.get(url)
    data = response.json()
    for airport in data['response']['airports']:
        print(f"IATA Code: {airport['iata_code']}")
        
        IATA = float(str({airport['lat']})[1:-1])
    return IATA
    
    

city = input('Enter city name : ')
get_airport_data(city)
