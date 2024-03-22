age = int(input("Enter age:"))
student = input("Are you a student(yes/no):")
if age <= 12 and student == 'yes':
    print("You are eligible for movie ticket")
elif (age >= 13 and age <= 18) and student == 'yes':
    print("You are eligilble for movie tickets")
else:
    print("You are not eligible")
