height = float(input("Enter your height in cms: "))
weight = float(input("enter you weight in kgs: "))
BMI = weight / (height/100)**2
print("your BMI is {0}".format(BMI))

if BMI <= 18.4:
    print("you are underweight")
elif BMI <= 24.9:
    print("you are healthy")
elif BMI <= 29.9:
    print("you are overweight")
elif BMI <= 34.9:
    print("you are severly overweight")
elif BMI <= 39.9:
    print("you are obese")
else:
    print("you are severly obese")