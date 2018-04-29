#Takes the input of the node from the Mathattan map and generats the corresponding node values for the MAP Vectors

import random
import sys
import os
import numpy as np





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

        if (i!=44):
                print("Error occured, Index did not reach end of array")
                print("i=%s",i)
        else: 
                return node_array, cordname, row_avg, col_avg


        
[node_array,cordname,row_avg,col_avg]=nodecreater(1,1,2,2,3,1)

##A=cord[0:4]
##B=cord[4:8]
##C=cord[8:12]
##D=cord[12:16]
##E=cord[16:20]
##F=cord[20:24]
##G=cord[24:28]
##H=cord[28:32]
##I=cord[32:36]
##J=cord[36:40]
##K=cord[40:44]
##
##nodearray = np.array([A,B,C,D,E,F,G,H,I,J,K])
##print node_array.shape[1]


#STORES THE VALUES X,Y IN PIXELS TO EACH CORRESPONDING NODE
##A1=A[0]
##A2=A[1]
##A3=A[2]
##A4=A[3]
##B1=B[0]
##B2=B[1]
##B3=B[2]
##B4=B[3]
##C1=C[0]
##C2=C[1]
##C3=C[2]
##C4=C[3]
##D1=D[0]
##D2=D[1]
##D3=D[2]
##D4=D[3]
##E1=E[0]
##E2=E[1]
##E3=E[2]
##E4=E[3]
##F1=F[0]
##F2=F[1]
##F3=F[2]
##F4=F[3]
##G1=G[0]
##G2=G[1]
##G3=G[2]
##G4=G[3]
##H1=H[0]
##H2=H[1]
##H3=H[2]
##H4=H[3]
##I1=I[0]
##I2=I[1]
##I3=I[2]
##I4=I[3]
##J1=J[0]
##J2=J[1]
##J3=J[2]
##J4=J[3]
##K1=K[0]
##K2=K[1]
##K3=K[2]
##K4=K[3]
