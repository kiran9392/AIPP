"""
Task 4.4: Compare Zero-Shot vs Few-Shot Prompts for Vowel Counting Function
============================================================================
"""

# ============================================================================
# PROMPTS
# ============================================================================

ZERO_SHOT_PROMPT = """
Write a Python function to count vowels in a string.
"""

FEW_SHOT_PROMPT = """
Write a Python function to count vowels in a string.

Examples:
- "hello" -> 2
- "AI" -> 2
- "Ramesh" -> 2
"""

print("=" * 70)
print("PROMPT COMPARISON")
print("=" * 70)
print("\nZERO-SHOT PROMPT:")
print(ZERO_SHOT_PROMPT)
print("\nFEW-SHOT PROMPT:")
print(FEW_SHOT_PROMPT)
print("=" * 70)


# ============================================================================
# FUNCTION IMPLEMENTATIONS
# ============================================================================

# Zero-Shot Approach: Function created from instruction only
def count_vowels_zero_shot(s):
    """
    Counts vowels in a string (zero-shot implementation).
    Based only on the instruction without examples.
    """
    vowels = "aeiouAEIOU"
    count = 0
    for ch in s:
        if ch in vowels:
            count += 1
    return count


# Few-Shot Approach: Function created with examples
def count_vowels_few_shot(s):
    """
    Counts vowels in a string (few-shot implementation).
    Learns pattern from provided examples.
    """
    vowels = "aeiouAEIOU"
    return sum(1 for ch in s if ch in vowels)


# ============================================================================
# TEST CASES
# ============================================================================

test_cases = [
    ("hello", 2),
    ("AI", 2),
    ("Ramesh", 2)
]

print("\n" + "=" * 70)
print("FUNCTIONAL OUTPUT")
print("=" * 70)

print("\nZero-Shot Function Results:")
print("-" * 70)
for word, expected in test_cases:
    result = count_vowels_zero_shot(word)
    status = "OK" if result == expected else "X"
    print(f"{status} {word:10} -> {result:2} (Expected: {expected})")

print("\nFew-Shot Function Results:")
print("-" * 70)
for word, expected in test_cases:
    result = count_vowels_few_shot(word)
    status = "OK" if result == expected else "X"
    print(f"{status} {word:10} -> {result:2} (Expected: {expected})")


# Additional test cases for comprehensive testing
additional_tests = [
    ("programming", 3),
    ("aeiou", 5),
    ("bcdfg", 0),
    ("Hello World", 3),
    ("", 0)
]

print("\n" + "=" * 70)
print("ADDITIONAL TEST CASES")
print("=" * 70)
print("\nZero-Shot Function:")
print("-" * 70)
for word, expected in additional_tests:
    result = count_vowels_zero_shot(word)
    status = "OK" if result == expected else "X"
    print(f"{status} '{word:15}' -> {result:2} (Expected: {expected})")

print("\nFew-Shot Function:")
print("-" * 70)
for word, expected in additional_tests:
    result = count_vowels_few_shot(word)
    status = "OK" if result == expected else "X"
    print(f"{status} '{word:15}' -> {result:2} (Expected: {expected})")


# ============================================================================
# COMPARATIVE REFLECTION
# ============================================================================

print("\n" + "=" * 70)
print("COMPARATIVE REFLECTION")
print("=" * 70)

reflection = """
ZERO-SHOT APPROACH:
-------------------
- Prompt: Only provides the task description without examples
- Advantages:
  * More general and flexible
  * Can lead to creative solutions
  * Faster to write prompts
  * Good for well-defined tasks
- Limitations:
  * May misinterpret requirements
  * Could miss edge cases
  * No pattern guidance
  * Potential ambiguity in interpretation

FEW-SHOT APPROACH:
------------------
- Prompt: Provides task description + concrete examples
- Advantages:
  * Clear pattern demonstration
  * Better understanding of expected format
  * Handles edge cases better (if examples show them)
  * Reduces ambiguity
  * More likely to match expected behavior
- Limitations:
  * Requires good example selection
  * May overfit to example patterns
  * Longer prompts
  * Examples might not cover all cases

OBSERVATIONS:
-------------
1. Both approaches produce functionally equivalent code for this task
2. Few-shot provides clearer context about expected input/output format
3. Zero-shot relies more on the model's prior knowledge
4. For simple tasks like this, both work well, but few-shot reduces ambiguity
5. Few-shot examples help validate understanding before implementation
6. The examples show the format: "input" -> output, which guides output structure

CONCLUSION:
-----------
For this vowel counting task, both prompts work effectively. However, the few-shot
approach provides:
- Better clarity on expected output format
- Validation through examples
- Reduced chance of misunderstanding
- Pattern recognition that can help with edge cases

The zero-shot approach relies on the model's understanding of what "vowels" means
and how to count them, which works well for such a standard task.
"""

print(reflection)
print("=" * 70)
