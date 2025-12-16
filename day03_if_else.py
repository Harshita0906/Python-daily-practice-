# Day 3: Python Practice
# Topic: if, elif, else conditions

# 1. Simple if-else example
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

print("--------------------")

# 2. if-elif-else example (grading system)
marks = int(input("Enter your marks (0-100): "))

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: D")

print("--------------------")

# 3. Even or Odd number check
number = int(input("Enter a number: "))

if number % 2 == 0:
    print(number, "is an Even number")
else:
    print(number, "is an Odd number")

print("--------------------")

# 4. Login check example
username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print("Login successful")
else:
    print("Invalid credentials")

# End of Day 3 practice
