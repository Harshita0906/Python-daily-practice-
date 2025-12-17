# Day 5: Python Practice
# Topic: Lists and Tuples (Basics)

# 1. Creating a list
fruits = ["apple", "banana", "mango", "orange"]
print("Fruits list:", fruits)

# 2. Accessing list elements (indexing)
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

print("--------------------")

# 3. Modifying list elements
fruits[1] = "grapes"
print("Updated fruits list:", fruits)

print("--------------------")

# 4. Adding elements to a list
fruits.append("pineapple")
print("After append:", fruits)

fruits.insert(1, "kiwi")
print("After insert:", fruits)

print("--------------------")

# 5. Removing elements from a list
fruits.remove("apple")
print("After remove:", fruits)

last_item = fruits.pop()
print("Popped item:", last_item)
print("List after pop:", fruits)

print("--------------------")

# 6. Looping through a list
print("Looping through fruits:")
for fruit in fruits:
    print(fruit)

print("--------------------")

# 7. Length of list
print("Number of fruits:", len(fruits))

print("--------------------")

# 8. Creating a tuple (immutable)
colors = ("red", "blue", "green")
print("Colors tuple:", colors)

# 9. Accessing tuple elements
print("First color:", colors[0])

# 10. Tuple cannot be modified (immutable)
# colors[0] = "yellow"  # This will cause an error

# End of Day 5 practice

