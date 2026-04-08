# while loop
count = 1
while count <= 10:
    print(f"Count: {count}")
    count += 1

num = 1
print("Even numbers from 1 to 20:")
while num <= 20:
    if num % 2 == 0:
        print(num)
    num += 1

# For loop
numbers = [20, 40, 60, 80, 100]
for num in numbers:
    print(num)

total = 0
for num in numbers:
    total += num
print(f"Sum of given values: {total}")

product = 1
for num in numbers:
    product *= num
print(f"Product of given values: {product}")