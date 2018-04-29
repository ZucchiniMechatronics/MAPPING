##Parses the directions into individual connections
import numpy as np

def connections(directions):
    direc = np.array(directions)
    begs = direc[0:len(direc)-1]
    ends = direc[1:len(direc)]
    connec = np.array([begs,ends])
    return connec

direc = np.array(['a','b','c','d','e'])
connec = connections(direc)
print connec
print connec[:,0]
