# Seatwork 1
name = input("What is your name?")
age = input("How old are you?")
favorite_color = input("What is your favorite color?")
city = input("Which city do you live in?")

print("Hello my name is", name, " I am ", age, "years old and my favorite color is", favorite_color, "and I live at", city)
 

# Seatwork 2
name = input("What is your name?")
gender = input("What is your gender?")
section = input("What is your section?")
phone_brand = input("What is your phone brand?")

print(f"Hello, {name} your gender is {gender} from {section} and your phone brand is {phone_brand}!")


# Laboratory 1
name = input("What is your name?")
age = input("How old are you?")
grade1 = input("Enter your grade in subject1?")
grade2 = input("Enter your grade in subject2?")
grade3 = input("Enter your grade in subject3?")

average = (int(grade1) + int(grade2) + int(grade3)) / 3
if average >= 75:
    remarks = "Passed"
else:
    remarks = "Failed"
    
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Your average grade is: {average}")
print(f"Remarks: {remarks}")
