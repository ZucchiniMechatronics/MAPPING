## Distance to specific node
import numpy as np

def distance(current_loc,target_loc):
    
    [x_cur,y_cur,ang_cur] = np.array(current_loc)
    [x_tar,y_tar] = np.array(target_loc)    
    
    dist = np.linalg.norm(np.array([x_cur,y_cur]) - np.array([x_tar,y_tar])) # take the norm of the distance vector

    return dist
