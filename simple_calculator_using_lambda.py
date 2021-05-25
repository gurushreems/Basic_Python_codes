from functools import reduce
import math
import sys
print("which operation you want to perform ?")
print("1:add/2:sub/3:mul/4:div/5:factorial/6:exponential/7:squaroot")       # for user referance
opt = int(input("option::"))  # input for choosing the method of operation
while opt != 6:        #opt != 6 is the condition so that if option 6 is choosen it will not go inside while loop.
    n = list(map(int, input("Enter values seperated by ','").split(",")))
    if opt == 1:
        sum1 = reduce(lambda a, b : a + b, n)
        print(f"sum of {n} is {sum1}")          #written in f string literals
        sys.exit()                              #print("{} = {}".format(n, sum1)) can also be written
    elif opt == 2:
        sub = reduce(lambda a, b : a - b , n)
        print(f"sub of {n} is {sub}")
        sys.exit()
    elif opt == 3:
        mul = reduce(lambda a, b : a * b , n)
        print(f"Multiplication of {n} is {mul}")
        sys.exit()
    elif opt == 4:
        div = reduce(lambda a, b: a / b, n)
        print(f"Division of {n} is {div}")
        sys.exit()

    elif opt == 5:
        factorial = list(map(lambda a:math.factorial(a), n))
        for x in range(0,len(n)):
            print(f"{n[x]} = {factorial[x]}")
        sys.exit()

    elif opt == 7:
        sqrt = list(map(lambda a:math.sqrt(a), n))
        for x in range(0,len(n)):
            print(f"{n[x]} = {sqrt[x]}")
        sys.exit()

if opt == 6:                                         #exponential is kept outside the while since
    value1 = int(input("base value ::"))             #it takes two values.
    value2 = int(input("power value ::"))
    exp = value1 ** value2
    print(exp)
    sys.exit()
