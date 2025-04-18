name = input("What is your name: ")
age = float(input("What is your age: "))
profession = input("What is your profession? ")
print("Nice to meet you {0}, so I see that you are {1} years old.".format(name, age))
print("So you are a", profession, end=' ')
print("That's nice!")
input("When is your birthday? ")
print("be sure to call me for your birthday party!")
day = input("how is your day going? ")
if day=='good':
    print("Oh thats good!")
elif day=='bad':
    print("Oh I hope it gets better.")
else:
    print("ohh")