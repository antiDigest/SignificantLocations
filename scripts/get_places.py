from functions import get_distance, get_folder
import os
import sqlite3
import pandas as pd
import numpy as np
import time, sys
import itertools
reload(sys)
sys.setdefaultencoding('utf-8')

def find_place(places, line):
    '''
    :param places:
    :param line:
    :return: Return true if the the distance between the 
    coordinates is within 15 meters from any coordinate in places
    '''
    if len(places) == 0:
        return False
    for place in places:
        if get_distance(place, line) < 15:
            return False
    return True

def places():    
    cur_path = os.getcwd()
    path = cur_path[:-7] + "Data/"
    os.chdir(path)
    
    conn = sqlite3.connect("/home/evamy/SignificantLocations/scripts/data.db")
    c = conn.cursor()

    c.execute('drop table if exists places')
    query = "CREATE TABLE IF NOT EXISTS places (\
        latitude float(5.10),longitude float(5.10), dated date, timed time)"
    c.execute(query)
    # places = []
    # query = "SELECT * FROM places"
    # places += [pd.read_sql(sql=query,con=conn)]

    places = []
    start = time.time()
    for fol in range(182):                        # 0-19 done
        folder = get_folder(fol)
        query = "SELECT * FROM master" + folder
        lines = pd.read_sql(query,con=conn,coerce_float=False, index_col=None)

        for line, place in itertools.combinations(ls,2):
            if not get_distance(place,line) < 15:
                places.append(line)

        print("Num Places: ", len(places))
        print("Num Lines", len(lines))

        df = pd.DataFrame(places)
        df.to_sql(name='places', con=conn, index=False, if_exists='append')

    end = time.time()
    print 'Time taken to execute the script :',end-start

    os.chdir(cur_path)
    
    conn.close()

def CreateMaster():
    cur_path = os.getcwd()

    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    
    start = time.time()
    for fol in range(25,182):
        # path = cur_path
        folder = get_folder(fol)
        folder += "/Trajectory/"
        path = "/home/evamy/SignificantLocations/Data/"
        path += folder
        os.chdir(path)
        files = os.listdir('.')
        
        print "Number of files in", folder, ":", len(files)

        c.execute('drop table if exists '+ "master"+folder[:3])
        query = "CREATE TABLE IF NOT EXISTS " + "master"+folder[:3] + " (\
            latitude float(5.10),longitude float(5.10), dated date, timed time)"
        c.execute(query)

        columns = ['latitude','longitude','dated','timed']
        i = 0
        for n in files:
            try:
                f = pd.read_csv(n,sep=',',names=['latitude','longitude','zero',\
                                'Altitude','days','dated','timed'], skiprows=6, dtype={\
                                'latitude':np.float64,'longitude':np.float64}, parse_dates=['dated'\
                                ,'timed'])
                df = pd.DataFrame(f,columns=columns)
                df.to_sql(name="master"+folder[:3], con=conn,index=False,if_exists='append')
            except ValueError:
                continue
        # print data
    end = time.time()
    print 'Total time taken :',end-start



if __name__ == '__main__':
    places()
