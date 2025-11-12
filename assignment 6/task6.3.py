# Function 1: Using nested if-elif-else
def classify_age(age):
    if age >= 0:
        if age < 13:
            print("You are a Child.")
        elif age < 20:
            print("You are a Teenager.")
        elif age < 60:
            print("You are an Adult.")
        else:
            print("You are a Senior Citizen.")
    else:
        print("Invalid age entered!")

# Main Program
age = int(input("Enter your age: "))


classify_age(age)


