string = input("please enter a string: ")
string2 = ('')
for i in string:
    string2 = i + string2

print("\nThe original string: {0}".format(string))
print("The reversed string: {0}".format(string2))