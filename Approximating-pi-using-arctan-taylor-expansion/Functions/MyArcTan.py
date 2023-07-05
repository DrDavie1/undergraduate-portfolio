from math import *

def MyArcTan(x,N):
    answer = 0

    if abs(x) > 1:
        for i in range(0,N+1):
            answer += (((-1)**i)/(2*i + 1))*(1/x)**(2*i + 1)
        
        if x > 0:
            answer = pi/2 - answer 
        
        elif x < 0:
            answer = - pi/2 - answer

    else:
        for i in range(0,N+1):
            answer += (((-1)**i)/(2*i + 1))*(x)**(2*i + 1)

    return answer
