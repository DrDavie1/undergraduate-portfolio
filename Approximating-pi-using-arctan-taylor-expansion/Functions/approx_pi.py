from math import *
from Functions.MyArcTan import *

def equation_3(N):
    answer = MyArcTan(1/2,N) + MyArcTan(1/5,N) + MyArcTan(1/8,N)
    pi_approx = answer*4
    diffence = pi - pi_approx

    return pi_approx,diffence