## node to cord

import numpy as np

def node2cord(node_name):
    index = np.where(np.isin(node_data,node_name))
    cord = node_array[index[1,2]]
    return cord
