import os

def write_to_file(fname, x, uid):
    f = open(fname, "a")
    for i in x:
        f.write(str(uid) + str(i))
    # f.write("\n")
    f.close()


def begin(folder = "000"):
    path = os.getcwd() 
    path = path[:-7]
    path += "gps data/"
    os.chdir(path + folder + "/Trajectory/coord/")
    nof = len(os.listdir(path + folder + "/Trajectory/coord/"))
    # filename = str(fno) + ".txt"
    f = open("LL_edges.txt", "r")
    
    LL_edges = []

    for i in f:
        LL_edges += [i];

    write_to_file("../../../../graphs/LL_graph.txt", LL_edges, folder)
    # write_to_file("final.txt", final, fno)

def go():
    path = os.getcwd()
    for i in range(0,10):
        fname = "00" + str(i)
        begin(fname)
        os.chdir(path)
    begin('010')
    os.chdir(path)

if __name__ == "__main__":
    go()