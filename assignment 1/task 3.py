# Function to reverse a string
def reverse_string(s: str) -> str:
    """
    Return the reverse of the input string `s`.
    Examples:
        reverse_string("abc") -> "cba"
        reverse_string("")    -> ""
    """
    # Simple and efficient slice-based reverse
    return s[::-1]

# Example usage:
if __name__ == "__main__":
    print(reverse_string("hello"))  # prints: olleh
    print(reverse_string("A man, a plan"))  # prints: nalp a ,nam A