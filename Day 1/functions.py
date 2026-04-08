# Three parts of function:
# 1) Function Declaration
# 2) Function Definition
# 3) Function Call

# Function Declaration
def greet():
    pass

# Function Definition
def greet():
    print("Good Afternoon")

# Function Call
greet()

# name is a parameter
def greetWithName(name):
    print(f"Good Afternoon, {name}!")

# Akshay & Jagadeesh are arguments
greetWithName("Akshay")
greetWithName("Jagadeesh")

# default parameter, company is a default parameter
def printInfo(name, company="ParvaM"):
    print(f"My name is {name}, I'm working at {company}")

printInfo("Akshay")
printInfo("Ajay", "Amazon")

# positional arguments (*args)
def sumOfNumbers(*args):
    total = 0
    for num in args:
        total += num
    print(f"Sum of given numbers: {total}")

sumOfNumbers(2, 5)
sumOfNumbers(2, 5, 8, 10)
sumOfNumbers(2, 5, 8, 10, 15, 17, 20)

# keyword arguments (**kwargs)