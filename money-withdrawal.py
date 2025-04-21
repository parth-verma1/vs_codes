amount = int(input("enter the money you want to withdraw :"))
n1 = amount//500
n2 = (amount%500)//100
n3 = ((amount%500)%100)//50
n4 = (((amount%500)%100)%50)//10
n5 = ((((amount%500)%100)%50)%10)//5
n6 = (((((amount%500)%100)%50)%10)%5)//1
print("notes of 500 rupee:", n1)
print("notes of 100 rupee:", n2)
print("notes of 50 rupee:", n3)
print("notes of 10 rupee:", n4)
print("coins of 5 rupee:", n5)
print("coins of 1 rupee:", n6)