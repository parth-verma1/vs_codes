class india():
    def capital(self):
        print("New Delhi is the capital of India")

    def language(self):
        print("Hindi is the most spoken in india")

    def type(self):
        print("India is a developing country")

class USA():
    def capital(self):
        print("washington dc is the capital of USA")

    def language(self):
        print("english is the most spoken language of USA")

    def type(self):
        print("usa is a developed country")

obj_ind = india()
obj_usa = USA()

for country in (obj_ind, obj_usa):
    country.capital()
    country.language()
    country.type()
