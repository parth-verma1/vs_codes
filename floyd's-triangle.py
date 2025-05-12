rows = int(input("Enter number of rows: "))
number = 1
i = 1
while i <= rows:
    j = 1
    while j <= i:
        print(number, end=' ')
        number += 1
        j += 1
    print()
    i += 1
