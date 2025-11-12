def divide(a, b):
    try:
        result = a / b
        print(f"Result of {a} / {b} = {result}")
    except ZeroDivisionError:
        print(f"Error: Division by zero is not allowed for {a} / {b}.")

# Example test cases  
divide(5, 0)    # ❌ Division by zero handled safely
divide(9, 3)    # ✅ Valid division
