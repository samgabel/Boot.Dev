# Given a number find the prime factors of said number (ex: 24 -> [2, 2, 2, 3])
# This problem has been determined to be in NP (not in NP-complete)

# Time Complexity:
# Note: it may look like the Big O is O(sqrt(n)), but when we talk about this problem we are concerned with the length of n in bits

# Time Complexity in bits:
# O(sqrt(2^s)) -> exponential



import math

def prime_factors(n):
    prime_factors = []
    # We keep dividing our input by 2 until it cannot be cleanly divisible by 2 anymore (odd number)
    while n % 2 == 0:
        n /= 2
        # Keep track of each divide in a list
        prime_factors.append(2)
    # Starting from 3 till the sqrt(n), we want to try to divide our odd number input
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            n /= i
            # Append all odd numbers that cleanly divide our input
            prime_factors.append(i)
    # If our input is still greater than 2 after all the previous operations, then we append whatever is left
    if n > 2:
        prime_factors.append(int(n))
    return prime_factors



# -----------------------------------------------


print(prime_factors(801945405608))
