import math
print("add: Addition\nsub: Substraction\nmul: Multiplication")
print("div: Division\nexp: Exponantial\nsqrt: SquareRoot\nfact: factorial")
print("when done, press anything otherthan numbers!")
choose = input("which method do you want?")
result = 0

if choose == "add":
    while True:
        try:
            input1 = float(input("value:"))
            result += input1
            print(float(result))
        except ValueError:
            print("value should be integer!")
            break

if choose == "sub":
    while True:
        try:
            input1 = float(input("value1:"))
            input2 = float(input("value2:"))
            result = input1 - input2
            print(result)
        except ValueError:
            print("value should be integer!")
            break
if choose == "mul":
    while True:
        try:
            input1 = float(input("value1:"))
            input2 = float(input("value2:"))
            result = input1 * input2
            print(result)
        except ValueError:
            print("value should be integer!")
            break
if choose == "div":
    while True:
        try:
            input1 = float(input("value1:"))
            input2 = float(input("value2:"))
            result = input1 / input2
            print(result)
        except ValueError:
            print("value should be integer!")
            break
if choose == "exp":
    while True:
        try:
            input1 = float(input("value1:"))
            input2 = float(input("value2:"))
            result = input1 ** input2
            print(result)
        except ValueError:
            print("value should be integer!")
            break
if choose == "sqrt":
    while True:
        try:
            input1 = float(input("value1:"))
            result = math.sqrt(input1)
            print(result)
        except ValueError:
            print("value should be integer!")
            break
if choose == "fact":
    while True:
        try:
            input1 = int(input("value1:"))
            result = math.factorial(input1)
            print(result)
        except ValueError:
            print("value should be integer!")
            break
