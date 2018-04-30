## compare the angle to what it should be
import numpy as np

def ang_compare(current_loc,ang_des):
    ang_cur = current_loc.item(2)
    ang_dif = abs(ang_cur-ang_des)
    return ang_dif
print ang_compare(np.array([0,0,5]),90)


    
