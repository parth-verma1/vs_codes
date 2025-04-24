a = float(input("enter a number: "))
b = float(input("eneter another number: "))
c = float(input("enter one more number: "))
if a>b:
    if a>c:
        if b>c:
            print("{0} is the greatest number".format(a))
            print("{0} is the smallest number".format(c))
        else:
            print("{0} is the greatest number".format(a))
            print("{0} is the smallest number".format(b))
    else:
        print("{0} is the greatest number".format(c))
        print("{0} is the smallest number".format(b))
else:
    if b>c:
        if a>c:
            print("{0} is the greatest number".format(b))
            print("{0} is the smallest number".format(c))
        else:
            print("{0} is the greatest number".format(b))
            print("{0} is the smallest number".format(a))
    else:
        print("{0} is the greatest number".format(c))
        print("{0} is the smallest number".format(a))
