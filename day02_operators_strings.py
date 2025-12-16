# Day 2: Python Practice
# Topic: Operators, String Operations, and Basic Logic

# 1. Arithmetic Operators
num1 = 10
num2 = 3

print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)
print("Floor Division:", num1 // num2)
print("Modulus:", num1 % num2)
print("Power:", num1 ** num2)

print("--------------------")

# 2. Comparison Operators
print(num1 > num2)   # True
print(num1 < num2)   # False
print(num1 == num2)  # False
print(num1 != num2)  # True

print("--------------------")

# 3. String Concatenation
first_name = "Aashi"
last_name = "Chauhan"
full_name = first_name + " " + last_name

print("Full Name:", full_name)

print("--------------------")

# 4. String Length
print("Length of name:", len(full_name))

# 5. String Methods
message = "python is fun"
print(message.upper())
print(message.capitalize())
print(message.replace("fun", "awesome"))

print("--------------------")

# 6. User Input with Strings
city = input("Enter your city: ")
fav_language = input("Enter your favorite programming language: ")

print("You live in", city, "and love", fav_language)

# End of Day 2 practice
