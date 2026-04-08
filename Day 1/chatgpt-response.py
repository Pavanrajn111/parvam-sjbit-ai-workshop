# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Function to print prime numbers in a given range
def print_primes(start, end):
    print("Prime numbers between", start, "and", end, "are:")
    for num in range(start, end + 1):
        if is_prime(num):
            print(num, end=" ")

# Example usage
start = int(input("Enter start number: "))
end = int(input("Enter end number: "))

print_primes(start, end)

# Result
# Enter start number: 50
# Enter end number: 100
# Prime numbers between 50 and 100 are:
# 53 59 61 67 71 73 79 83 89 97