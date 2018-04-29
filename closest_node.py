import sys
sys.path.append('/home/pi/MAPPING')

import numpy as np
import node_generator


## Function returns the name and distance to closest node from current
def closest_node(current_loc):
    
    [x_cur,y_cur,ang_cur] = np.array(current_loc)
    
    node_locs = node_generator.node_array
    cordname = node_generator.cordname
    dist = np.zeros(node_locs.shape[0:2])

    row_avg = node_generator.row_avg
    col_avg = node_generator.col_avg

    #Find distance between current loc and closest node and name of
    for i in range(node_locs.shape[0]): #for every row 
        for j in range(node_locs.shape[1]): # for every column
            dist[i,j] = np.linalg.norm([x_cur,y_cur] - node_locs[i,j]) # take the norm of the distance vector

    min_index = np.unravel_index(np.argmin(dist),node_locs.shape[0:2]) # index of minimum value (convert from 'flat' index)

    close_dist = dist[min_index]
    close_node = cordname[min_index]

    #Check direction, find row and column nearest then backtrack to prev node
    if -10<ang_cur<10: #Right (road is up)
        #find out what row is associated (closest in positive y direction)
        close_row = np.array(np.where(row_avg > y_cur+2)).item(0)
        #find out what column is previous (closest in negative x direction)
        close_col = np.array(np.where(col_avg < x_cur)).item(-1)
    elif 80<ang_cur<100: #Up (road is left)
        close_row = np.array(np.where(row_avg < y_cur)).item(-1) #closest in negative y direction
        close_col = np.array(np.where(col_avg < x_cur)).item(-1) #closest in negative x direction
    elif 170<ang_cur<190: #Left (road is down)
        close_row = np.array(np.where(row_avg < y_cur-2)).item(-1) #closest in negative y direction (correct for sidewalk)
        close_col = np.array(np.where(col_avg > x_cur)).item(0) #closest in negative x direction
    else: #Down (road is right)
        close_row = np.array(np.where(row_avg > y_cur)).item(0) #closest in pos y direction
        close_col = np.array(np.where(col_avg > x_cur)).item(0) #closest in pos x direction
        
    prev_node = cordname[close_row,close_col]
        
    return np.array([close_dist, close_node, prev_node])

##[close_dist, close_node, prev_node] = closest_node([5,0,0])
