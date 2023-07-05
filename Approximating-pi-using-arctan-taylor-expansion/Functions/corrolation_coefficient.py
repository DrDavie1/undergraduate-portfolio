import numpy as np 

def cor_co(list1,list2):
    array1 = np.array(list1)
    array2 = np.array(list2)

    mean1 = array1.mean()
    mean2 = array2.mean()

    std1 = array1.std()
    std2 = array2.std()

    mean3 = (array1*array2).mean()

    covarience = mean3 - mean1*mean2

    correlation_coeffienct = covarience/(std1*std2)

    return correlation_coeffienct