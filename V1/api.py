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
        #pp.pprint(data['response'])
        port=""
        flag1=True
        flag2 = True
        def for1():
            global port
            global flag1
            for airport in data['response']['airports_by_cities']:
                try:
                    #print(airport) #debug
                    #input(" press Enter.") #debug
                    print(f"{c}. {airport['name']} - {airport['iata_code']} ({airport['country_code']})")
                    c += 1
                    port=data['response']['airports_by_cities'][ch-1]['iata_code']
                except KeyError as Ke:
                    flag1=False
                    pass

        def for2():
            global port
            global flag2
            for airport in data['response']['airports_by_countries']:
                try:
                    #print(airport) #debug
                    #input(" press Enter.") #debug
                    print(f"{c}. {airport['name']} - {airport['iata_code']} ({airport['country_code']})")
                    c += 1
                    port=data['response']['airports_by_countries'][ch-1]['iata_code']
                except KeyError as Ke:
                    flag2=False
                    pass
            
        ch = int(input('Select a airport : '))
        print()
        for1()
        for2()
        if flag1==True and flag2!=True:
            return port
        elif flag2==True and flag1!=True:
            return port
x = input("Enter destination : ")
haha = get_airport_data(x)
print(haha)