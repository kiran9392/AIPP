def cm_to_inches(cm: float) -> float:
    """Convert centimeters to inches.

    1 inch == 2.54 centimeters.

    Args:
        cm: length in centimeters (int or float)

    Returns:
        length in inches as a float. 

    Raises:
        TypeError: if cm is not a number.
    """
    if not isinstance(cm, (int, float)):
        raise TypeError("cm must be a number (int or float)")
    return cm / 2.54


if __name__ == '__main__':
    # example from the prompt
    value_cm = 10
    inches = cm_to_inches(value_cm)
    # print formatted to 3 decimal places like the example
    print(f"{value_cm} cm = {inches:.3f} inches")

    # additional example 1
    value_cm = 25
    inches = cm_to_inches(value_cm)
    print(f"{value_cm} cm = {inches:.3f} inches")

    # additional example 2
    value_cm = 50
    inches = cm_to_inches(value_cm)
    print(f"{value_cm} cm = {inches:.3f} inches")

    # quick assertion (allowing rounding at 3 decimal places)
    assert round(cm_to_inches(10), 3) == 3.937
    print("All tests passed.")
