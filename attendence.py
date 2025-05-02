medical_cause = input("did you have a medical cause, yes or no: ")
atten = int(input("enter the attendence of the student: "))

if medical_cause == 'yes':
    print("You are allowed")
else:
    if atten>=75:
        print("allowed")
    else:
        print("not allowed")