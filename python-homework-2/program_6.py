# Grade from marks

name = input("Enter your name: ")
marks = float(input("Enter your marks (0-100): "))
if marks < 0 or marks > 100:
    print("Invalid marks")
elif marks >= 80 and marks < 100:
    print("Hello ",name," your grade is: A+")
elif marks >= 70 and marks < 80:
    print("Hello ",name," your grade is: A")
elif marks >= 60 and marks < 70:
    print("Hello ",name," your grade is: A-")
elif marks >= 50 and marks < 60:
    print("Hello ",name," your grade is: B")
elif marks >= 40 and marks < 50:
    print("Hello ",name," your grade is: C")
else:
    print("Hello ",name," your grade is: F")
