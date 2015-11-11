# PlaceRank
import numpy as np
import pandas as pd
import time, sys
reload(sys)
sys.setdefaultencoding('utf-8')

def fetchData():
	print 'Fetching data...'
	start = time.time()
	data = pd.read_csv('../graphs/LL_graph.txt',sep='-\[|\]to\[|\]',names=['user','from',\
		'to','Nan'],index_col=None,engine='python')
	size = data.shape[0]
	end = time.time()
	print "Time to fetch data :",end-start
	print 'users fetched :',len(data['user'])

	return data

def fetchPlaces():
	print 'Fetching mapped places...'
	start = time.time()
	places = pd.read_csv('../graphs/location_map.txt',sep=':',names=['Coordinates','Address'],\
		index_col=None)

	placedict = {}
	for place in places:
		placedict[place['Coordinates']] = place['Address']

	print placedict

	end = time.time()
	print 'Places Fetched in :',end-start
	print 'No. of places fetched :',places.shape[0]
	
	return placedict

def PlaceRank():
	data = fetchData()
	places = fetchPlaces()

	
	
