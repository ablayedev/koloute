import requests


def recup_stations():
    stations = requests.get('http://localhost:8000/api/station/')
    return stations.json()

def main():
    stations=recup_stations()
    print('voici la liste des stations disponibles')
    i=1
    for station in stations:
        for key,value in station.items():
                if key =="nom_station":
                        print('{}){}'.format(i,station[key]))
                        i=i+1
    #user_station=input('choisissez votre station ')
    #print('Bienvenue sur votre station '+user_station)
    code = int(input('entrer votre code '))
    locations=requests.get('http://localhost:8000/api/location/').json()
    for location in locations:
            if code in location.values():
                    print("location box{}  pour {}{}".format(location['box'],location['njh'],location['jh']))
                    requests.post('http://localhost:8000/update_box/',{'id':location['box']})
                    break




if __name__ == "__main__":
    main()