# Day 1: Python Variables Practice
# This file covers basic variable concepts we practiced on Day 1.

# 1. Integer variable
age = 30
print("My age is", age)

# 2. Float variable
height = 5.4
print("My height is", height)

# 3. String variable
name = "Aashi"
print("My name is", name)

# 4. Boolean variable
is_student = True
print("Am I a student?", is_student)

# 5. Type checking
print(type(age))      # <class 'int'>
print(type(height))   # <class 'float'>
print(type(name))     # <class 'str'>
print(type(is_student))  # <class 'bool'>

# 6. Taking input from user
user_name = input("Enter your name: ")
birth_year = int(input("Enter your birth year: "))
current_year = 2025
user_age = current_year - birth_year

print("Hello", user_name + ", your age is", user_age)

# 7. Simple addition example
num1 = 5
num2 = 5
print("Addition result:", num1 + num2)

# End of Day 1 practice
