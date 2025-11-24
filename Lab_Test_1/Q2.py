import math

def fact(n):
    # check
    if n < 0:
        return 'Invalid' # error
    # start
    res = 1
    # loop
    for i in range(1, n + 1):
        # multiply
        res *= i
    # done
    return res

def calculate_factorial(n: int) -> int | str:
    """
    Calculates the factorial (n!) of a non-negative integer.

    The factorial of an integer n is the product of all positive integers 
    less than or equal to n.

    Parameters
    ----------
    n : int
        The non-negative integer for which to calculate the factorial.

    Returns
    -------
    int or str
        The factorial of the number as an integer. Returns the string 
        'Invalid' if the input n is negative.
    """
    
    # Handle the edge case for negative input as defined by the original function's logic.
    if n < 0:
        return 'Invalid'

    # Handle the base case: Factorial of 0 is 1.
    if n == 0:
        return 1
        
    result = 1
    # Iterate from 1 up to and including n to calculate the product.
    for i in range(1, n + 1):
        result *= i
        
    return result

# --- Code to execute the function and produce output ---

print("--- Factorial Calculation Tests ---")

# Test 1: Positive integer (5!)
num_1 = 5
result_1 = calculate_factorial(num_1)
print(f"The factorial of {num_1} is: {result_1}")  # Expected: 120

# Test 2: Base case (0!)
num_2 = 0
result_2 = calculate_factorial(num_2)
print(f"The factorial of {num_2} is: {result_2}")  # Expected: 1

# Test 3: Negative input (Error case)
num_3 = -2
result_3 = calculate_factorial(num_3)
print(f"The factorial of {num_3} is: {result_3}")  # Expected: Invalid
