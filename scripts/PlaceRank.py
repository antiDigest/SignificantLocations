# PlaceRank

import numpy as np
import pandas as pd

# print len(edges), len(nodes)

def PlaceRank():
	data = pd.read_csv('../graphs/LL_graph.txt',sep='-\[|\]to\[|\]',names=['user','from','to','Nan'],\
		index_col=None,engine='python')
	size = data.shape[0]
	
		
if __name__ == '__main__':
	PlaceRank()
