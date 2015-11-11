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
    :return: Return true if the the distance between the coordinates is within 5 meters from any coordinate in places
    '''
    if len(places) == 0:
        return False
    low = 0
    high = len(places)
    while low <= high:
        mid = int((low + high)/2)
        if get_distance(places[mid], line) <= 5:
            return False
        else:
            high = mid - 1
    return True

def get_places():
    cur_path = os.getcwd()
    path = cur_path[:-7] + "Data/"
    os.chdir(path)
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    places = []
    query = "SELECT * FROM places"
    for line in c.execute(query):
        line = list(line[1:5])
        if len(places) == 0:
            line.append(0)
        else:
            line.append(get_distance(line, places[0]))
            places.append(line)

    for u in range(0, 182):
        user = get_folder(u)
        query = "SELECT * FROM master" + user
        lines = []
        now = time.time()
        for line in c.execute(query):
            line = list(line[1:])
            if len(places) == 0:
                line.append(0)
            else:
                line.append(get_distance(line, places[0]))
            lines.append(line)
        for line in lines:
            if line not in places:
                if not find_place(places, line):
                    if line[4] == 0 and len(places) != 0:
                        line[4] = get_distance(line, places[0])
                    places.append(line)
                    # print(line)
            if time.time() - now > 60:
                print("Processing user: ", user)
                print("Line: ", line)
                now = time.time()
        print("User: ", user)
        print("Num Places: ", len(places))
        print("Num Lines", len(lines))

        places.sort(key=lambda place: place[4])

        query = "DELETE FROM places"
        c.execute(query)
        query = "DELETE FROM sqlite_sequence WHERE NAME = 'places'"
        c.execute(query)

        for place in places:
            c.execute("INSERT INTO places(latitude, longitude, dated, timed) VALUES \
                (?, ?, ?, ?)", place[0:4])
        print 'Entered',user
        conn.commit()
    conn.close()
    os.chdir(cur_path)

def master():
    cur_path = os.getcwd()
    path = cur_path[:-7] + "Data/"
    os.chdir(path)
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    for fol in range(153, 182):
        folder = get_folder(fol)
        path = "/home/evamy/SignificantLocations/Data/"
        path += folder
        os.chdir(path)
        table_name = "master" + folder
        c.execute("DROP TABLE IF EXISTS "+table_name)
        query = "CREATE TABLE IF NOT EXISTS " + table_name + ''' (id integer primary key\
                autoincrement not null,latitude real not null, longitude real not null,\
                dated date not null, timed time not null)'''
        c.execute(query)
        with open("master.csv", "r") as f:
            for line in f:
                line = line.split(",")
                # print line, folder
                c.execute("INSERT INTO " + table_name + "(latitude, longitude, dated, timed)\
                    values (?, ?, ?, ?)", line)
                # print(line)
        print "in folder :",folder
    conn.commit()
    conn.close()
    os.chdir(cur_path)

def place():
    cur_path = os.getcwd()
    path = cur_path[:-7] + "Data/"
    os.chdir(path)
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS places")
    query = '''CREATE TABLE IF NOT EXISTS places (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                latitude REAL NOT NULL, longitude REAL NOT NULL, dated DATE NOT NULL,
                timed TIME NOT NULL, weight INTEGER NOT NULL DEFAULT 0)
            '''
    c.execute(query)
    conn.commit()
    conn.close()
    print 'Created table places !'
    os.chdir(cur_path)

def create_master():
    cur_path = os.getcwd()
    for fol in range(0, 182):
        folder = get_folder(fol)
        folder += "/Trajectory/"
        path = "/home/evamy/SignificantLocations/Data/"
        path += folder
        os.chdir(path)
        files = os.listdir('.')
        total_content = ""
        print("Number of files in",folder,":", len(files))
        for n in files:
            with open(str(n), 'r') as f:
                for i in range(0, 6):
                    f.readline()

                for line in f:
                    line = line.split(',')
                    line = line[:2] + line[5:]
                    content = ','.join(line)
                    total_content += content
        folder = get_folder(fol)
        path = "/home/evamy/SignificantLocations/Data/"
        path += folder
        os.chdir(path)
        with open("master.csv", 'w') as f:
            f.write(total_content)
        print("Total records written :", len(total_content))
    os.chdir(cur_path)

def rename():
    cur_path = os.getcwd()
    for f in range(0, 182):
        folder = get_folder(f)
        folder += "/Trajectory/"
        path = "/home/evamy/SignificantLocations/Data/"
        path += folder
        os.chdir(path)
        files = os.listdir('.')
        files.sort()
        j = 1
        for i in files:
            os.rename(i, str(j)+".plt")
            j += 1
        print("File rename complete in folder {0}. Number of files renamed: {1}".format(folder, len(files)))
    os.chdir(cur_path)

if __name__ == '__main__':
    # rename()
    # create_master()
    # master()
    place()
    get_places()
