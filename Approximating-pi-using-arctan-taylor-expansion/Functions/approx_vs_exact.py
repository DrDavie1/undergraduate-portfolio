from math import *
from Functions.MyArcTan import *
import pandas as pd
import numpy as np

def approx_vs_exact(N,Ns,Averages,x_start,x_end):

    approximated_values = []
    actual_values = []
    differences = []

    for i in range(int(x_start*10),int(x_end*10)):
        x = i/10
        arctan_approx = MyArcTan(x,N)
        arctan_exact = atan(x)
        difference = arctan_approx - arctan_exact

        approximated_values.append(arctan_approx)
        actual_values.append(arctan_exact)
        differences.append(difference)


    data = {'Approximated Value': approximated_values,'Exact Value': actual_values,'Difference':differences}
    dataframe = pd.DataFrame(data=data)


    differences = np.array(differences)
    average_difference = abs(differences.mean())

    Ns.append(N)
    Averages.append(average_difference)

    return dataframe