from auth import hash_password, verify_password

# File where users and their hashed passwords are stored
USERS_FILE = "users.txt"


# This function creates a new user
def register_user():
    # Ask the user for a username and password
    username = input("Create username: ").strip()
    password = input("Create password: ").strip()

    # Prevent empty usernames or passwords
    if not username or not password:
        print("Username and password cannot be empty.")
        return

    # Convert the password into a secure hashed version
    hashed_password = hash_password(password)

    # Save username and hashed password to the file
    with open(USERS_FILE, "a", encoding="utf-8") as f:
        f.write(f"{username},{hashed_password}\n")

    print("User registered successfully.")
    print("Password was NOT saved as plain text.")


# This function checks login credentials
def login_user():
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    try:
        # Open the users file
        with open(USERS_FILE, "r", encoding="utf-8") as f:
            for line in f:
                # Remove extra spaces or line breaks
                line = line.strip()
                if not line:
                    continue

                # Split username and stored password hash
                saved_user, stored_password = line.split(",", 1)

                # If usernames match, verify password
                if saved_user == username:
                    if verify_password(stored_password, password):
                        print("Login successful.")
                    else:
                        print("Wrong password.")
                    return

        # If username was never found
        print("User not found.")

    except FileNotFoundError:
        print("No users exist yet. Please register first.")


# Main menu loop
def main():
    while True:
        print("\n1) Register")
        print("2) Login")
        print("3) Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            register_user()
        elif choice == "2":
            login_user()
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid option.")


# This ensures the program only runs when executed directly
if __name__ == "__main__":
    main()
