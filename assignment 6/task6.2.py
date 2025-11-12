# Function 1: Using for loop
def print_multiples_for(num):
    print(f"First 10 multiples of {num} using for loop:")
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")
    print()  # blank line for separation
# Main program
num = int(input("Enter a number: "))
print_multiples_for(num)

