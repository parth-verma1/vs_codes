n = int(input("enter value of n: "))
print("numbers from {0} to {1} are: ".format(n,1))
for i in range(n,0,-1):
    print(i)
for i in range(n,0,-2):
    print(i)
for i in range(0,n,2):
    print(i)