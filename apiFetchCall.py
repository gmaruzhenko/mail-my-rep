import requests
import simplejson as json


# given coordinates will return a list of tuples of local gov reps [(name,email), ...]
def getReps (lat,long):
    array_of_representatives = []
    resp = requests.get('https://represent.opennorth.ca/representatives/?point='+ lat +'%2C'+ long)

    # Print the response parsed as JSON
    for rep in resp.json()['objects']:
        array_of_representatives.append((rep['name'],rep['email']))

    return array_of_representatives

#given an address returns coords tuple (lat,long)
def getGeo(address):
    coordinates=requests.get('https://nominatim.openstreetmap.org/search/'+ address +'?format=json&addressdetails=1&limit=1&polygon_svg=1')
    latitude = coordinates.json()[0]['lat']
    longitude = coordinates.json()[0]['lon']

    return (latitude,longitude)


if __name__ == '__main__':
    address = '3520%20W%20Broadway,%20Vancouver'
    lat, long = getGeo(address)
    print(lat)
    print(long)
