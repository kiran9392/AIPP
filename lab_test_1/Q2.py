"""
Q2.py

Compute the mean of student marks and list students above the mean.

This file also includes example prompts (zero-shot, one-shot, few-shot) that
you could send to an AI assistant to solve the same problem, and a short
summary explaining the differences between those prompt styles.

Usage:
    python Q2.py

The script demonstrates the behavior on a small sample dataset.
"""

from typing import Dict, List, Tuple


def compute_mean(marks: List[float]) -> float:
    """Return the arithmetic mean of a list of numeric marks.

    Raises ValueError for empty input.
    """
    if not marks:
        raise ValueError("marks list must not be empty")
    return sum(marks) / len(marks)


def students_above_mean(student_marks: Dict[str, float]) -> Tuple[float, List[Tuple[str, float]]]:
    """Compute mean and return list of (student, mark) for those above mean.

    Returns a tuple (mean, above_mean_list). The above_mean_list preserves
    the insertion order of the input mapping.
    """
    marks = list(student_marks.values())
    mean = compute_mean(marks)
    above = [(name, mark) for name, mark in student_marks.items() if mark > mean]
    return mean, above


# Example prompts for guiding an AI assistant
ZERO_SHOT_PROMPT = (
    "Given a list of student names and their marks, compute the mean mark and "
    "return the list of students who scored strictly above the mean. Output the mean "
    "and each student's name with their mark. Do not include any extra commentary."
)

ONE_SHOT_PROMPT = (
    "Example:\nInput: [('Alice', 70), ('Bob', 80), ('Carol', 60)]\nOutput: mean = 70.0; students above mean = [('Bob', 80)]\n\nNow solve:\nGiven a list of student names and marks, compute the mean and list students above mean."
)

FEW_SHOT_PROMPT = (
    "Example 1:\nInput: [('A', 50), ('B', 70), ('C', 60)] -> mean = 60.0; above = [('B', 70)]\n\nExample 2:\nInput: [('X', 90), ('Y', 80), ('Z', 85)] -> mean = 85.0; above = [('X', 90)]\n\nNow solve for this input: provide mean and list of students above mean."
)


PROMPT_SUMMARY = (
    "Prompt summary:\n"
    "- Zero-shot: You give the task description only; the model must infer the format and edge-case handling.\n"
    "- One-shot: Provide a single example input->output to show desired format and behavior; useful to clarify expected output.\n"
    "- Few-shot: Provide multiple examples illustrating variations (edge cases, ordering, formatting) so the model generalizes better.\n"
)


def _demo() -> None:
    sample = {
        "Alice": 72,
        "Bob": 88,
        "Charlie": 65,
        "Diana": 90,
        "Eve": 58,
    }

    mean, above = students_above_mean(sample)
    print("Sample student marks:")
    for name, mark in sample.items():
        print(f"  {name}: {mark}")
    print()
    print(f"Mean mark: {mean:.2f}")
    print("Students above mean:")
    if above:
        for name, mark in above:
            print(f"  {name}: {mark}")
    else:
        print("  (none)")

    print("\n--- Prompt Examples ---\n")
    print("Zero-shot prompt:\n", ZERO_SHOT_PROMPT, sep="")
    print("\nOne-shot prompt:\n", ONE_SHOT_PROMPT, sep="")
    print("\nFew-shot prompt:\n", FEW_SHOT_PROMPT, sep="")
    print("\nSummary of prompt styles:\n", PROMPT_SUMMARY, sep="")


if __name__ == "__main__":
    _demo()
