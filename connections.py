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
print connec[:,0].tolist()
print type(connec[:,0].tolist())

## Figures out what instructions to follow for the current node pair
right = [['a1','b1'],
         ['c1','d1'],
         ['e1','f1'],
         ['j1','k1'],
         ['b2','a2'],
         ['d2','c2'],
         ['f2','e2'],
         ['i2','h2'],
         ['k2','j2'],
         ['a3','b3'],
         ['c3','d3'],
         ['e3','f3'],
         ['h3','i3'],
         ['j3','k3'],
         ['b4','a4'],
         ['d4','c4'],
         ['f4','e4'],
         ['i4','h4'],
         ['k4','j4']]

left = [['d2','f3'],
        ['c3','e2'],
        ['e3','c2'],
        ['f2','d3']]

## g->h is short then long, h->g is long then short (check map)

left_tight = [['g3','h2'],
              ['h3','g2']] 


def instructions(connections):
    instruct_list = []
    i = 0
    while i < connections.shape[1]:
        node_pair = connections[:,i].tolist()
        if node_pair in right:
            instruction = 'right'
        elif node_pair in left:
            instruction = 'left'
        elif node_pair in left_tight:
            instruction = 'left_tight'
        else:
            instruction = 'straight'
        instruct_list.append(instruction)
        i = i+1
    return instruct_list
        

##print instructions(connec)
    


