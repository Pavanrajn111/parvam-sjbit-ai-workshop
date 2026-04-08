def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def get_primes(limit):
    """Return a list of all prime numbers up to the given limit."""
    return [n for n in range(2, limit + 1) if is_prime(n)]


def print_primes(limit):
    """Print all prime numbers up to the given limit."""
    primes = get_primes(limit)
    print(f"Prime numbers up to {limit}:")
    print(", ".join(map(str, primes)))
    print(f"Total count: {len(primes)}")


# Example usage
print_primes(50)

# Result:
# Prime numbers up to 50:
# 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47
# Total count: 15