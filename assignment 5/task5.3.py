# Recursive function to calculate the nth Fibonacci number

def fibonacci(n):
    """
    This function returns the nth Fibonacci number using recursion.
    The Fibonacci sequence is defined as:
    F(0) = 0, F(1) = 1, and F(n) = F(n-1) + F(n-2) for n > 1
    """
    
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        # Recursive case: sum of previous two Fibonacci numbers
        return fibonacci(n - 1) + fibonacci(n - 2)

# Example usage
num = int(input("Enter the value of n: "))
print(f"The {num}th Fibonacci number is:", fibonacci(num))
