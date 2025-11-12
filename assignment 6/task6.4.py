# Function to calculate sum of first n numbers using a FOR loop
def sum_to_n_for(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


# Function to calculate sum of first n numbers using a WHILE loop
def sum_to_n_while(n):
    total = 0
    i = 1
    while i <= n:
        total += i
        i += 1
    return total


# Example usage
n = 5
print("Sum using for loop:", sum_to_n_for(n))
print("Sum using while loop:", sum_to_n_while(n))
