prime_num = []

n = int(input("Enter the num ::"))
for i in range(1, n+1):
    if n % i == 0:
        prime_num.append(i)

print(prime_num)
if len(prime_num) == 2:
    print("{} is a Prime Number".format(n))
else :
    print("{} is Not a Prime Number".format(n))