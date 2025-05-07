num = int(input("enter a number: "))
l = len(str(num))
sum=0
temp=num 
while temp>0:
    digit = temp % 10
    sum+=digit**l
    temp //= 10
if num == sum:
    print(num," is an armstrong number.")
else:
    print(num," is not an armstrong number")

count = 0
temp = num
while temp>0:
    digit = temp%10
    temp = temp//10
    count = count + 1
print("number of digits in {0}: {1}".format(num, count))
