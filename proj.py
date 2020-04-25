
import math

SCREEN_H = 720
SCREEN_W = 1280
ASPECT = 1280/720
FOV = 90
FOV_RAD = 1/math.tan(((FOV*0.5)/180) * 3.14159)
F_NEAR = 0.1
F_FAR = 1000

PROJ_MAT = [[ASPECT*FOV_RAD,0,0,0],
            [0,FOV_RAD,0,0],
            [0,0,F_FAR/(F_FAR-F_NEAR),1],
            [0,0,(-F_FAR * F_NEAR) / (F_FAR - F_NEAR),0]]


class triangle:
    def __init__(self,vecA,vecB,vecC):
        self.vectors=[vecA,vecB,vecC]

class mesh:
    def __init__(self,triangles):
        pass


