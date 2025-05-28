import random

playing = True
number = str(random.randint(10, 20))

print("generating a number from 10 to 20, and u have to guess a digit at a time.")
print("The game ends when you get 1 zero")

while playing:
    guess = input("Give your best guess! \n")
    
    if number == guess:
        print("You win the game")
        print("The number was", number)
        break
    else:
        print("Your guess isn't right, try again. \n")
