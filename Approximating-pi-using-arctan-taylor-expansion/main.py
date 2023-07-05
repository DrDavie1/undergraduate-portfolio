from math import *
import pandas as pd
import numpy as np 
from re import A
import matplotlib.pyplot as plt
from Functions.approx_vs_exact import *
from Functions.MyArcTan import *
from Functions.corrolation_coefficient import *
from Functions.Input_pos_interger import *
from Functions.approx_pi import *

MyInput = '0'
sectionb_N = []
sectionb_average = []

while MyInput != 'q':
    MyInput = input('Enter a choice, "a", "b", "c", "d" or "q" to quit: ')
    print('You entered the choice: ',MyInput)

# ___________________SECTION A___________________

    if MyInput == 'a':
        print('You have chosen part (a)')
        Input_x = input('Enter a value for x (floating point number): ')
        try:
            x = float(Input_x)
        except:
            print("you need to input a floating point number example: 1")
            x = 1.0
        a_Input_N = input('Enter a value for N (positive integer): ')
        N = int(a_Input_N)
        print('Approximate value: ',MyArcTan(x,N))
        print('Correct Value:' ,atan(x))


# ___________________SECTION B___________________

    elif MyInput == 'b':

        print('You have chosen part (b)')

        choice = input("would you like to loop through N = 1 - 20 ('A') or choose a specific value of N ('B'): ")
        if choice == "A":
            for i in range(1,20+1):
                dataframe = approx_vs_exact(i,sectionb_N,sectionb_average,-2,2)

                if i == 10:
                    print("================================================")
                    print("EXAMPLE DATA (N=10)")
                    print("================================================")
                    print(dataframe)


        else:
            b_Input_N = 'start'
            b_Input_N = Input_N(b_Input_N)

            dataframe = approx_vs_exact(b_Input_N,sectionb_N,sectionb_average,-2,2)
            print("================================================")
            print(f"DATA WHERE N={b_Input_N}")
            print("================================================")
            print(dataframe)
            

        
        b_data = {'N':sectionb_N,'Average Difference':sectionb_average}

        b_dataframe = pd.DataFrame(b_data)
        print("")
        print("================================================")
        print("FINAL VALUES OBTAINED FROM SECTION B")
        print("================================================")
        print(b_dataframe)

        print("Corrolation between N and Average difference",cor_co(sectionb_N,sectionb_average))
        print("Interesting to see how corrolation decreases as N tends towards infinity since this is an exponetial relationship")

        if len(sectionb_N) > 10:
            choice = input("would you like to plot this data? ('yes' or 'no'): ")
            if choice == 'yes':
                plt.plot(sectionb_N,sectionb_average,color="purple")
                plt.title("Approximated arctan(x)")
                plt.xlabel("N")
                plt.ylabel("Average Difference")
                plt.show()


# ___________________SECTION C___________________

    elif MyInput == 'c':
        print('you have chosen part (c)')
        
        sectionc_N = []
        sectionc_difference = []
        sectionc_approx = []
        sectionc_exact = []

        c_Input_N = 'start'
        c_Input_N = Input_N(c_Input_N)

        

        for n in range(1,c_Input_N):
            dataframe = approx_vs_exact(n,sectionc_N,sectionc_difference,1,1.1)

            sectionc_approx.append(float(dataframe['Approximated Value']))
            sectionc_exact.append(float(dataframe['Exact Value']))

        sectionc_difference = np.array(sectionc_difference) * 4
        sectionc_approx = np.array(sectionc_approx) * 4
        sectionc_exact = np.array(sectionc_exact) * 4
        
        print("================================================")
        print("APPROXIMATING PI")
        print("================================================")
        print(pd.DataFrame(data={'N':sectionc_N,'Approximated Value':sectionc_approx,'Exact Value':sectionc_exact,'Difference':sectionc_difference}))

        print("Corrolation between N and Difference",cor_co(sectionc_N,sectionc_difference))
        print("Interesting to see how corrolation decreases as N tends towards infinity since this is an exponetial relationship")

        choice = input("would you like to plot this data? ('yes' or 'no'): ")
        if choice == 'yes':
            plt.plot(sectionc_N,sectionc_difference,color="purple")
            plt.title("Approximating PI")
            plt.xlabel("N")
            plt.ylabel("Difference")
            plt.show()

# ___________________SECTION D___________________

    elif MyInput == 'd':
        d_pi_approx = []
        d_pi_difference = []
        d_N_list = []

        print('you have chosen part (d)')
        N_d = 1

        pi_12dp = "{:.12f}".format(pi)
        pi_d = 0

        while pi_12dp != pi_d:
            N_d += 1
            pi_d,difference_d = equation_3(N_d)
            pi_d = "{:.12f}".format(pi_d)
            d_pi_approx.append(pi_d)
            d_pi_difference.append(difference_d)
            d_N_list.append(N_d)

        

        df_d = pd.DataFrame(data={'N':d_N_list,'Approximated Pi':d_pi_approx,'Difference':d_pi_difference})
        print("================================================")
        print(f"THE LOWEST VALUE OF N TO CACULATE PI TO 12.D.P is : {N_d}")
        print("================================================")
        print(df_d)

    elif MyInput != 'q':
        print('This is not a valid choice')


print('You have chosen to finish - goodbye.')