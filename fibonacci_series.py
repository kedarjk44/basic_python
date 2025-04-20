def fibonacci_iterative(n):
    """
    This function generates the Fibonacci sequence up to a given number (n) using iteration.
    Args: n: The number of terms in the Fibonacci sequence.
    Returns: A list containing the Fibonacci sequence up to n.
    """
    if n < 0:
        print("Invalid input. Please enter a non-negative number.")
        return

    # Initialize first two Fibonacci numbers
    a, b = 0, 1
    fibonacci_sequence = []

    # Generate Fibonacci sequence up to n
    for i in range(n):
        fibonacci_sequence.append(a)
        a, b = b, a + b

    return fibonacci_sequence


# Example usage
num_terms = int(input("Enter the number of terms in the Fibonacci sequence: "))
fibonacci_series = fibonacci_iterative(num_terms)
print("Fibonacci Series:", fibonacci_series)
