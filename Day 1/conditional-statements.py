# If, If-else, Nested If-else, Elif

# If Condition
num = 24
if num % 2 == 0:
    print(f"{num} is an even number")

# If - Else Statement
num = 25
if num % 3 == 0:
    print(f"{num} is a multiple of 3")
else:
    print(f"{num} is not a multiple of 3")

# Nested If-else
a = 5
b = 10
c = 7

if a > b:
    if a > c:
        print(f"{a} is greatest")
    else: 
        print(f"{c} is greatest")
else: 
    if b > c:
        print(f"{b} is greatest")
    else: 
        print(f"{c} is greatest")

# If - Else Ladder (Elif)
num = 25

if num % 2 == 0:
    print(f"{num} is a multiple of 2")
elif num % 3 == 0:
    print(f"{num} is a multiple of 3")
elif num % 5 == 0:
    print(f"{num} is a multiple of 5")
else:
    print(f"{num} is not a multiple of 2, 3 and 5")
    
# match case
weekday = 3
match weekday:
    case 1:
        print("Sunday")
    case 2:
        print("Monday")
    case 3:
        print("Tuesday")
    case 4:
        print("Wednesday")
    case 5:
        print("Thursday")
    case 6:
        print("Friday")
    case 7:
        print("Saturday")
    case _:
        print("It is not a week day")