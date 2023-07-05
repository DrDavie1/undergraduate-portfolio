def Input_N(Input_N):
    while (isinstance(Input_N,int) == False) or Input_N == 0:
        Input_N = input('Enter a value for N (positive integer): ')
        try:
            Input_N = int(Input_N)
            if Input_N < 0:
                print("N cannot be negative, the program will use it's absolute value")
            elif Input_N == 0:
                print("N cannot equal 0")
            Input_N = abs(Input_N)
        except:
            print("The inputed value of N is not an interger")

    return Input_N

