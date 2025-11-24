"""
Q1.py

Provides a well-documented, robust factorial function and a small
demonstration/test harness.

The `factorial` function:
- Accepts non-negative integers and returns n! as an int.
- Raises `ValueError` for negative inputs and `TypeError` for non-integers.

Author: Coding assistant
"""

from typing import Any


def factorial(n: int) -> int:
    """
    Calculate the factorial of a non-negative integer n.

    Args:
        n (int): A non-negative integer whose factorial is to be computed.

    Returns:
        int: The factorial of `n` (n!).

    Raises:
        TypeError: If `n` is not an integer.
        ValueError: If `n` is negative.

    Notes:
        - By definition, 0! == 1.
        - The implementation uses an iterative loop to avoid recursion limits.
    """
    # Validate type
    if not isinstance(n, int):
        raise TypeError(f"factorial() expected int, got {type(n).__name__}")

    # Validate value
    if n < 0:
        raise ValueError("factorial() not defined for negative values")

    # 0! is defined as 1
    if n == 0:
        return 1

    # Iterative computation to avoid recursion depth issues
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def _demo_and_tests() -> None:
    """Run a few demonstration calls and simple tests for the factorial function."""
    tests = [0, 1, 5, 10]
    print("Factorial demonstrations:")
    for t in tests:
        print(f"{t}! = {factorial(t)}")

    # Test negative input handling
    try:
        factorial(-1)
    except ValueError as e:
        print("Correctly raised for negative input:", e)

    # Test non-integer handling
    try:
        factorial(3.5)  # type: ignore[arg-type]
    except TypeError as e:
        print("Correctly raised for non-integer input:", e)


if __name__ == "__main__":
    _demo_and_tests()
