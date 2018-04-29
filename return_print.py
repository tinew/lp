import math
def move(x,y,step,angle):
    nx = x+step*math.cos(angle)
    ny = y+step*math.sin(angle)
    # return nx,ny
    print(nx,ny)

move(100,100,60,math.pi/6)
# print(x,y)

#注意与下面这种表示方式的区别

import math
def move1(x,y,step,angle):
    nx = x+step*math.cos(angle)
    ny = y+step*math.sin(angle)
    return nx,ny

x,y=move1(100,100,60,math.pi/6)
print(x,y)