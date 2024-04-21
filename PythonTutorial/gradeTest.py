# if condition with nested if condition

score = input("What was your test score? ")
score = int(score)
if score >= 90:
    age = int(input("How old are you ?"))
    if age < 10:
        print("Your grade is A+")
    else:
        print("Your grade is A")
elif score >= 80:
    age = int(input("How old are you ?"))
    if age < 10:
        print("Your grade is B+")
    else:
        print("Your grade is B")
elif score >= 70:
    age = int(input("How old are you ?"))
    if age < 10:
        print("Your grade is C+")
    else:
        print("Your grade is C")
elif score >= 60:
    age = int(input("How old are you ?"))
    if age < 10:
        print("Your grade is D+")
    else:
        print("Your grade is D")
else:
    print("You failed")
