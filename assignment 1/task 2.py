def is_prime(n: int) -> bool:
    """
    Return True if n is prime, False otherwise.

    Deterministic for n < 2**64 using the base set:
    (2, 325, 9375, 28178, 450775, 9780504, 1795265022)

    Quick trial division by small primes is done first for speed.
    """
    if n < 2:
        return False
    small_primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29)
    for p in small_primes:
        if n % p == 0:
            return n == p

    # write n-1 = d * 2^s with d odd
    d = n - 1
    s = 0
    while d & 1 == 0:
        d >>= 1
        s += 1

    def check(a: int) -> bool:
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            return True
        for _ in range(s - 1):
            x = (x * x) % n
            if x == n - 1:
                return True
        return False

    bases = (2, 325, 9375, 28178, 450775, 9780504, 1795265022)
    for a in bases:
        if a % n == 0:
            continue
        if not check(a):
            return False
    return True
if __name__ == "__main__":
    print("Prime checker. Enter integers to test; type 'q' or press Enter on an empty line to quit.")
    while True:
        s = input("Enter an integer (or 'q' to quit): ").strip()
        if s == "" or s.lower() in ("q", "quit", "exit"):
            print("Goodbye.")
            break
        try:
            n = int(s)
        except ValueError:
            print("Invalid input — please enter a valid integer.")
            continue
        if is_prime(n):
            print(f"{n} is prime.")
        else:
            print(f"{n} is composite.")