# Day 4: Python Practice
# Topic: for loop, while loop, range(), break, continue

# 1. for loop with range()
print("Numbers from 1 to 5")
for i in range(1, 6):
    print(i)

print("--------------------")

# 2. Print even numbers from 1 to 10
print("Even numbers from 1 to 10")
for num in range(1, 11):
    if num % 2 == 0:
        print(num)

print("--------------------")

# 3. while loop example
count = 1
print("Using while loop")
while count <= 5:
    print(count)
    count += 1

print("--------------------")

# 4. Sum of first n numbers
n = int(input("Enter a number: "))
sum = 0

for i in range(1, n + 1):
    sum += i

print("Sum is:", sum)

print("--------------------")

# 5. break example
print("Break example")
for i in range(1, 10):
    if i == 5:
        break
    print(i)

print("--------------------")

# 6. continue example
print("Continue example")
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

# End of Day 4 practice
