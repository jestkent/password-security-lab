from auth import verify_password
import time

# File where users are stored
USERS_FILE = "users.txt"

# This is a SMALL and SAFE password list
# Real attackers use millions of passwords
TOY_DICTIONARY = [
    "123456",
    "password",
    "admin",
    "qwerty",
    "letmein",
    "iloveyou",
    "kent123",
    "robotics",
]


# Load all users into a dictionary
def load_users():
    users = {}

    with open(USERS_FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            # Split username and hashed password
            username, stored_password = line.split(",", 1)
            users[username] = stored_password

    return users


# This function tries to guess a user's password
def dictionary_attack(target_username: str):
    users = load_users()

    # Check if the target user exists
    if target_username not in users:
        print("Target user not found.")
        return

    # Get the stored hashed password
    stored_password = users[target_username]

    print("\nStarting dictionary attack")
    print(f"Target user: {target_username}")
    print(f"Total guesses: {len(TOY_DICTIONARY)}\n")

    start_time = time.time()

    # Try each password from the dictionary
    for attempt, guess in enumerate(TOY_DICTIONARY, start=1):
        print(f"[{attempt}] Trying password: {guess}")

        # Use the same verification method as login
        if verify_password(stored_password, guess):
            end_time = time.time()
            print("\n[SUCCESS] Password cracked!")
            print(f"Password: {guess}")
            print(f"Attempts: {attempt}")
            print(f"Time taken: {end_time - start_time:.2f} seconds")
            return

    # If nothing matched
    end_time = time.time()
    print("\n[FAILED] Password not found.")
    print(f"Time taken: {end_time - start_time:.2f} seconds")


# Run the attack when this file is executed
if __name__ == "__main__":
    username = input("Enter username to test (your own): ").strip()
    dictionary_attack(username)
