import sys
destination={'bangaluru':230,'mysore':300,'chikkamangaluru':140,'ballary':175,'kolluru':110}
print("welcome to e-bus booking")
print("loading the current location .......")
print("FROM :: Shivamogga")
m=0
tm=0

while True:
    travel =input("where to?\n::")
    if travel in destination:

        while True:
            m = int(input("how many members :: "))
            tm=tm+m
            for i in range (1,m+1):
                n = str(input("NAME :: "))
                a = int(input("AGE :: "))
                s = input("SEX :: ")
                print(n)
                print(a)
                print(s)
            print("missed someone")
            miss=input("::")
            if miss not in ("y","yes"):
                pay = tm * destination[travel]
                print("to pay ::",pay)
                sys.exit()

    elif travel not in destination:
        print("the destination is not available\n to get the available destination press '1'")
        p = int(input("::"))
        if p == 1:
            print(destination)






