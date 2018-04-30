#Takes the input of the node from the Mathattan map and generats the corresponding node values for the MAP Vectors


import random
import sys
import os
import numpy as np

sys.path.append('/home/pi/MAPPING')

##-------------------------------------------------------------------

def nodecreater(X0,Y0,X1,Y1,Xlength,Ylength):

#checks to correct the difference between coordinates in case the node inputs from the user are not in the desired orientation

        xratio=abs((X0-X1)/(float(Xlength)))
        
        yratio=abs((Y0-Y1)/(float(Ylength)))       
        
        #Distance values from a0 inches (x,y)
        a1=(14.929,6)
        a2=(32.321,6)
        a3=(62.179,6)
        a4=(79.571,6)
        b1=(6,14.929)
        b2=(41.250,14.929)
        b3=(53.250,14.929)
        b4=(88.5,14.929)
        c1=(6,46.071)
        c2=(41.250,46.071)
        c3=(53.250,46.071)
        c4=(88.5,46.071)
        d1=(14.929,55)
        d2=(32.321,55)
        d3=(62.179,55)
        d4=(79.571,55)
        e1=(14.929,67)
        e2=(32.321,67)
        e3=(62.179,67)
        e4=(79.571,67)
        f1=(6,75.929)
        f2=(41.250,75.929)
        f3=(53.250,75.929)
        f4=(88.5,75.929)
        g1=(6,92.071)
        g2=(41.250,92.071)
        g3=(53.250,92.071)
        g4=(88.5,92.071)
        h1=(14.929,101)
        h2=(32.321,101)
        h3=(62.179,101)
        h4=(75.183,101)
        i1=(6,109.929)
        i2=(41.250,109.929)
        i3=(53.250,109.929)
        i4=(80.667,109.929)
        j1=(6,126.071)
        j2=(41.250,126.071)
        j3=(53.250,126.071)
        j4=(76.649,126.071)
        k1=(14.929,135)
        k2=(32.321,135)
        k3=(62.179,135)
        k4=(65.940,135)

        cordname= np.array(['a1','a2','a3','a4','b1','b2','b3','b4','c1','c2','c3','c4','d1','d2','d3','d4','e1','e2','e3','e4','f1','f2','f3','f4','g1','g2','g3','g4','h1','h2','h3','h4','i1','i2','i3','i4','j1','j2','j3','j4','k1','k2','k3','k4'])
        cordname = np.reshape(cordname,[11,4])
        datainch=[a1,a2,a3,a4,b1,b2,b3,b4,c1,c2,c3,c4,d1,d2,d3,d4,e1,e2,e3,e4,f1,f2,f3,f4,g1,g2,g3,g4,h1,h2,h3,h4,i1,i2,i3,i4,j1,j2,j3,j4,k1,k2,k3,k4]
        
     
        i=0
        
        while (i<=43):
                
                t=datainch[i]
                t1=t[0]*xratio
                t2=t[1]*yratio
                datainch[i]=[t1,t2]
                i+=1

        cord=datainch

        A=cord[0:4]
        B=cord[4:8]
        C=cord[8:12]
        D=cord[12:16]
        E=cord[16:20]
        F=cord[20:24]
        G=cord[24:28]
        H=cord[28:32]
        I=cord[32:36]
        J=cord[36:40]
        K=cord[40:44]

        node_array = np.array([A,B,C,D,E,F,G,H,I,J,K])
        row_avg = np.average(node_array[:,:,1],1) # average y value of each row (a, b, etc)
        col_avg = np.average(node_array[:,:,0],0) # average x value of each col (1, 2, etc)

        node_data = np.dstack([cordname,node_array])

        if (i!=44):
                print("Error occured, Index did not reach end of array")
                print("i=%s",i)
        else: 
                return node_array, cordname, row_avg, col_avg, node_data
        
[node_array,cordname,row_avg,col_avg,node_data]=nodecreater(1,1,2,2,3,1)

##-------------------------------------------------------------------

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
    elif 170<ang(ang_cur)<190: #Left (road is down)
        close_row = np.array(np.where(row_avg < y_cur-2)).item(-1) #closest in negative y direction (correct for sidewalk)
        close_col = np.array(np.where(col_avg > x_cur)).item(0) #closest in negative x direction
    else: #Down (road is right)
        close_row = np.array(np.where(row_avg > y_cur)).item(0) #closest in pos y direction
        close_col = np.array(np.where(col_avg > x_cur)).item(0) #closest in pos x direction
        
    prev_node = cordname[close_row,close_col]
        
    return np.array([close_dist, close_node, prev_node])

##[close_dist, close_node, prev_node] = closest_node([5,0,0])

##-------------------------------------------------------------------

##Parses the directions into individual connections

def connections(directions):
    direc = np.array(directions)
    begs = direc[0:len(direc)-1]
    ends = direc[1:len(direc)]
    connec = np.array([begs,ends])
    return connec

##direc = np.array(['a','b','c','d','e'])
##connec = connections(direc)
##print connec
##print connec[:,0]

##-------------------------------------------------------------------

## Distance to specific locations

def distance(current_loc,target_loc):
    
    [x_cur,y_cur,ang_cur] = np.array(current_loc)
##    [x_tar,y_tar,ang_tar] = np.array(target_loc)
##    [x_tar,y_tar] = np.array(target_loc) 
    [x_tar,y_tar] = target_loc
    dist = np.linalg.norm(np.array([x_cur,y_cur]) - np.array([x_tar,y_tar])) # take the norm of the distance vector

    return dist

##-------------------------------------------------------------------

# fixes angles

def ang(cur_ang):
    if cur_ang < 0:
        cur_ang = 360 + cur_ang
    elif cur_ang > 360:
        cur_ang = cur_ang - (cur_ang/360)*360
    else:
        cur_ang = cur_ang
    return cur_ang


##-------------------------------------------------------------------

##Difference in angle

def ang_compare(current_loc,ang_des):
    ang_cur = ang(current_loc.item(2))
    ang_dif = abs(ang_cur-ang_des)
    return ang_dif

##-------------------------------------------------------------------

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

##-------------------------------------------------------------------

# returns coordinates for node name

def node2cord(node_name):
##    index = np.array(np.where(np.isin(node_data,node_name)))
    index = np.where(np.isin(node_data,node_name))
    cord = node_array[index[1:]]
    cord = cord[0]
    return cord

##-------------------------------------------------------------------
# STRAIGHT
# Finds target coordinate and steps forward until that is reached

def go_straight(target_loc):
    current_loc = gpsgo().item(0)
    cur_dist = distance(current_loc, target_loc)
    while cur_dist > 3:
        speakit('straight')
        listen()
        current_loc = gpsgo().item(0)
        cur_dist = distance(current_loc, target_loc)

##-------------------------------------------------------------------
# RIGHT
# Finds target angle and steps forward until that is reached
        
def go_right():
    current_loc = gpsgo().item(0)
    ang_des = ang(current_loc.item(2)-90)
    ang_dif = ang_compare(current_loc,ang_des)
    while ang_dif > 3:
        speakit('right')
        listen()
        current_loc = gpsgo().item(0)
        ang_dif = ang_compare(current_loc,ang_des)

##-------------------------------------------------------------------
# LEFT
# Finds target angle and steps forward until that is reached
        
def go_left():
    current_loc = gpsgo().item(0)
    ang_des = ang(current_loc.item(2)+90)
    ang_dif = ang_compare(current_loc,ang_des)
    while ang_dif > 3:
        speakit('left')
        listen()
        current_loc = gpsgo().item(0)
        ang_dif = ang_compare(current_loc,ang_des)

##-------------------------------------------------------------------

def go_left_tight():
    current_loc = gpsgo().item(0)
    ang_des = ang(current_loc.item(2)+90)
    ang_dif = ang_compare(current_loc,ang_des)
    while ang_dif > 3:
        speakit('left_tight')
        listen()
        current_loc = gpsgo().item(0)
        ang_dif = ang_compare(current_loc,ang_des)

##-------------------------------------------------------------------   

def listen():
    DEC = 0
    while DEC == 0
        dec = readarduino()
        if dec = 1:
            DEC = dec
            
##-------------------------------------------------------------------   



        
            
