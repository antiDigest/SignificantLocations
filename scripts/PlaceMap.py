# PlaceRank
import numpy as np
import pandas as pd
import time, sys
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
reload(sys)
sys.setdefaultencoding('utf-8')

def write_to_file(fname, placeName, place):
    f = open(fname, "a")
    f.write(str(place) + ":" + str(placeName) + '\n')
    f.close()

def fetchData():
	print 'Fetching data...'
	start = time.time()
	data = pd.read_csv('../graphs/LL_graph.txt',sep='-\[|\]to\[|\]',names=['user','from','to','Nan'],\
		index_col=None,engine='python')
	size = data.shape[0]
	places = []
	for i in data['from']:
		place = [i.split(', ')[:2]]
		if not place in places:
			places += place

	for i in data['to']:
		place = [i.split(', ')[:2]]
		if not place in places:
			places += place			

	end = time.time()
	print "Time to fetch data :",end-start
	print 'locations fetched :',len(places)
	print 'users fetched :',len(data['user'])

	return data,places

def fetchPlaceName(place):
    geolocator = Nominatim()
    try:
        location = geolocator.reverse((str(place[0])+','+str(place[1])), language='en')
        address = location.address
    except GeocoderTimedOut:
        address = "Not Found"
        pass

    print address
    return address

def fetchAllNames(places):

	print 'Fetching Names of all the places ...'
	start = time.time()
	for place in places:
		write_to_file('../graphs/location_map.txt',fetchPlaceName(place),place)
		time.sleep(10)
	end = time.time()
	print 'Place Names mapped in :',end-start
	print 'All Names stored in file "../graphs/location_map.txt"'

	return
		
def PlaceMap():
	data,places = fetchData()

	fetchAllNames(places)
