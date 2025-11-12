import hashlib

# -------------------------------
# Insecure Version (AI-generated)
# -------------------------------
def insecure_login():
    print("---- Insecure Login System ----")
    username = input("Enter username: ")
    password = input("Enter password: ")

    # ❌ Hardcoded credentials (security risk)
    if username == "admin" and password == "12345":
        print("✅ Login successful! (INSECURE)")
    else:
        print("❌ Invalid credentials!")

# -------------------------------
# Secure Version (Revised)
# -------------------------------
def secure_login():
    print("\n---- Secure Login System ----")
    # ✅ Securely stored hashed passwords (simulation of database)
    stored_users = {
        "admin": hashlib.sha256("Secure@123".encode()).hexdigest(),
        "user1": hashlib.sha256("Password@456".encode()).hexdigest()
    }

    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in stored_users:
        hashed_input = hashlib.sha256(password.encode()).hexdigest()
        if hashed_input == stored_users[username]:
            print("✅ Login successful! (SECURE)")
        else:
            print("❌ Incorrect password.")
    else:
        print("❌ Username not found.")


# -------------------------------
# Main Program Execution
# -------------------------------
print("Comparing Insecure vs Secure Login Systems\n")

# Run both versions sequentially
insecure_login()
secure_login()
