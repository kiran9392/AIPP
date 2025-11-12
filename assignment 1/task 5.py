"""Find the largest number in a list (interactive).

This file provides a simple iterative implementation and an interactive
prompt so the user can enter numbers to find the largest.
"""

from typing import Iterable, TypeVar, List

T = TypeVar("T")


def largest_iterative(nums: Iterable[T]) -> T:
    """Return the largest element using a manual loop.

    Raises ValueError if nums is empty.
    """
    it = iter(nums)
    try:
        current = next(it)
    except StopIteration:
        raise ValueError("empty list")
    for x in it:
        if x > current:
            current = x
    return current


def largest_builtin(nums: Iterable[T]) -> T:
    """Return the largest element using Python's built-in max()."""
    return max(nums)


def _parse_number(s: str):
    """Parse a token as int if possible, otherwise float.

    Raises ValueError on invalid token.
    """
    try:
        return int(s)
    except ValueError:
        return float(s)


if __name__ == "__main__":
    print("Enter numbers separated by spaces or commas. Type 'q' to quit.")
    while True:
        line = input("Numbers: ").strip()
        if not line or line.lower() in ("q", "quit", "exit"):
            print("Goodbye.")
            break

        # Accept commas or spaces as separators
        tokens = [tok for part in line.split(',') for tok in part.split()]
        if not tokens:
            print("No numbers entered — try again.")
            continue

        try:
            nums: List[float] = [_parse_number(tok) for tok in tokens]
        except ValueError:
            print("One or more tokens were not valid numbers — try again.")
            continue

        try:
            print("Largest (built-in):", largest_builtin(nums))
            print("Largest (iterative):", largest_iterative(nums))
        except ValueError:
            print("Cannot determine largest of an empty list — try again.")