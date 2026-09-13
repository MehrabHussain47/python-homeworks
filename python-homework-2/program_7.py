# Voting eligibility

age = int(input("Enter your age: "))
is_citizen = True
if age >= 18 and is_citizen:
    print("Can vote")
else:
    print("Cannot vote")
