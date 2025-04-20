def is_prime(num):
    """
    This function checks if a number is prime.
    Args:  num: The number to check.
    Returns:  True if the number is prime, False otherwise.
    """
    if num <= 1:
        return False
    for i in range(2, int(num//2) + 1):
        if num % i == 0:
            return False
    return True


def print_prime_numbers(lower, upper):
    """
    This function prints prime numbers between a lower and upper bound.
    Args: lower: The lower bound of the range (inclusive).
          upper: The upper bound of the range (inclusive).
    """
    print("Prime numbers between", lower, "and", upper, "are:")
    for num in range(lower, upper + 1):
        if is_prime(num):
            print(num, end=" ")


# Get user input for lower and upper bounds
lower = int(input("Enter the lower limit: "))
upper = int(input("Enter the upper limit: "))

# Print prime numbers between the given bounds
print_prime_numbers(lower, upper)
