def is_prime(num):
    """
    Function to check if a number is prime
    Returns True if prime, False otherwise
    """
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    
    # Check for factors from 3 to sqrt(num)
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def print_primes(n):
    """
    Function to print all prime numbers up to n
    """
    print(f"Prime numbers up to {n}:")
    for i in range(2, n + 1):
        if is_prime(i):
            print(i, end=" ")
    print()  # New line at the end

def get_primes_list(limit):
    """
    Function to return a list of prime numbers up to the given limit
    """
    primes = []
    for i in range(2, limit + 1):
        if is_prime(i):
            primes.append(i)
    return primes

# Example usage
if __name__ == "__main__":
    # Example 1: Print primes up to 50
    print_primes(50)
    
    # Example 2: Get and print prime numbers as a list
    limit = 100
    prime_list = get_primes_list(limit)
    print(f"\nPrime numbers up to {limit}:")
    print(prime_list)
    
    # Example 3: Check if a specific number is prime
    number = 17
    if is_prime(number):
        print(f"\n{number} is a prime number")
    else:
        print(f"\n{number} is not a prime number")
    
    # Example 4: Print primes in a custom range
    start, end = 10, 50
    print(f"\nPrime numbers between {start} and {end}:")
    for num in range(start, end + 1):
        if is_prime(num):
            print(num, end=" ")
    print()

# Result:
# Prime numbers up to 50:
# 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 

# Prime numbers up to 100:
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

# 17 is a prime number

# Prime numbers between 10 and 50:
# 11 13 17 19 23 29 31 37 41 43 47