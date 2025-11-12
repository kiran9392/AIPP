import re


def is_palindrome(s: str) -> bool:
    """
    Check if a string is a palindrome, ignoring case and non-alphanumeric characters.

    Args:
        s: Input string

    Returns:
        True if palindrome, False otherwise
    """
    cleaned = re.sub(r'[^A-Za-z0-9]', '', s).lower()
    return cleaned == cleaned[::-1]


if __name__ == '__main__':
    examples = [
        "A man, a plan, a canal: Panama",
        "racecar",
        "hello",
        "",
        "12321",
        "Was it a car or a cat I saw?",
    ]
    for text in examples:
        print(f"'{text}' -> {is_palindrome(text)}")

