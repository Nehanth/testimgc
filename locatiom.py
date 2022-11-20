import googlemaps
import pandas as pd
import requests
import json

API_KEY = 'AIzaSyBl1Baq99DdgTQQ_yrfwrT_DmB3jAW8Qmw'


##location needs to be the google search, ie 'neurologists near me'

def getDocs(location):
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"

    # query = location

    r = requests.get(url + 'query=' + location +
                     '&key=' + API_KEY)

    x = r.json()

    y = x['results']

    # keep looping upto length of y
    hospitalNames = []
    for i in range(len(y)):
        # Print value corresponding to the
        # 'name' key at the ith index of y
        hospitalNames.append((y[i]['name']))

    return (hospitalNames)