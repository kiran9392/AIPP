"""
Few-Shot Prompting Example: Generating File Processing Functions

This script demonstrates how to use few-shot prompting to generate
a function that reads a text file and returns the number of lines,
by learning from examples of similar file-processing functions.
"""


# ============================================================================
# FEW-SHOT PROMPTS: Example Functions (Training Examples)
# ============================================================================

# Example 1: Count words in a text file
def count_words(filename):
    """Return the total number of words in a text file."""
    with open(filename, "r", encoding="utf-8") as file:
        text = file.read()
        return len(text.split())


# Example 2: Count characters in a text file
def count_characters(filename):
    """Return the total number of characters in a text file."""
    with open(filename, "r", encoding="utf-8") as file:
        text = file.read()
        return len(text)


# ============================================================================
# AI-GUIDED LOGIC: Generated Function Based on Few-Shot Examples
# ============================================================================
# Following the pattern from the examples above:
# 1. Open file with context manager (with open(...))
# 2. Read file content appropriately
# 3. Process/analyze the content
# 4. Return the result

def count_lines(filename):
    """
    Return the number of lines in a text file.
    
    Generated using few-shot prompting:
    - Pattern from Example 1 & 2: Use context manager to open file
    - Pattern from Example 1 & 2: Read file content
    - New logic: Count lines instead of words/characters
    - Pattern from Example 1 & 2: Return the count
    """
    with open(filename, "r", encoding="utf-8") as file:
        # Method 1: Using readlines() - reads all lines into a list
        lines = file.readlines()
        return len(lines)
        
        # Alternative Method 2: Using generator (memory efficient)
        # return sum(1 for line in file)


# ============================================================================
# TESTING AND EXAMPLES
# ============================================================================

def demonstrate_examples():
    """Display example outputs showing expected results."""
    examples = {
        "data.txt": 5,
        "notes.txt": 3,
        "sample.txt": 10,
    }
    
    print("\n" + "="*60)
    print("Few-Shot Prompting Examples:")
    print("="*60)
    
    for filename, expected_lines in examples.items():
        print(f"{filename} → {expected_lines} lines")
    
    print("\n" + "="*60)
    print("Function Pattern Analysis:")
    print("="*60)
    print("Example 1 (count_words):  open → read → split → len")
    print("Example 2 (count_chars):  open → read → len")
    print("Generated (count_lines):  open → readlines → len")
    print("="*60)


def main():
    """Main function to interact with user and demonstrate few-shot prompting."""
    
    print("\n" + "="*60)
    print("Few-Shot Prompting: File Line Counter")
    print("="*60)
    print("\nThis function was generated using few-shot prompting:")
    print("- Learned from examples: count_words(), count_characters()")
    print("- Applied similar patterns to create: count_lines()")
    print("="*60)
    
    # Get user input
    filename_input = input("\nEnter the filename to count lines: ").strip()
    
    if not filename_input:
        print("Error: No filename provided.")
        return
    
    # Process file using the generated function
    try:
        total_lines = count_lines(filename_input)
        print(f"\n✓ Result: {filename_input} → {total_lines} line(s)")
        
        # Show comparison with other functions
        print("\n" + "-"*60)
        print("Comparison with other file-processing functions:")
        print("-"*60)
        
        try:
            words = count_words(filename_input)
            chars = count_characters(filename_input)
            print(f"Words:      {words}")
            print(f"Characters: {chars}")
            print(f"Lines:      {total_lines}")
        except Exception as e:
            print(f"Could not compare with other functions: {e}")
            
    except FileNotFoundError:
        print(f"\n✗ Error: File '{filename_input}' not found.")
        print("\nPlease ensure the file exists in the current directory.")
    except Exception as e:
        print(f"\n✗ Error: {e}")
    
    # Display examples
    demonstrate_examples()


if __name__ == "__main__":
    main()
