def count_down(n):
    while n >= 0:
        print(n)
        n -= 1  # ✅ Decrement added to move toward loop termination

if __name__ == "__main__":
    count_down(5)  # Example usage