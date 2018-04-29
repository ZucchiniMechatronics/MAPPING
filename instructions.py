## Figures out what instructions to follow for the current node pair

import numpy as np

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


def instructions(node_pair):
    if node_pair in right:
        instruction = 'right'
    elif node_pair in left:
        instruction = 'left'
    elif node_pair in left_tight:
        instruction = 'left_tight'
    else:
        instruction = 'straight'
    return instruction

instruction = instructions(['c3','d3'])
print instruction
