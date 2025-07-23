from abc import ABC, abstractmethod
class animal(ABC):
    def move(self):
        pass

class human(animal):
    def move(self):
        print("i can walk and run")
    
class snake(animal):
    def move(self):
        print("i can crawl.")

class dog(animal):
    def move(self):
        print("i can walk on all 4 feet")

class lion(animal):
    def move(self):
        print("i can walk on all 4 legs")

R = human()
R.move()

K = snake()
K.move()

R = dog()
R.move()

K = lion()
K.move()