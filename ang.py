# fixes angle

def ang(cur_ang):
    if cur_ang < 0:
        cur_ang = 360 + cur_ang
    elif cur_ang => 360:
        cur_ang = cur_ang - (cur_ang/360)*360
    else:
        cur_ang = cur_ang
    return cur_ang

print ang(-25)
