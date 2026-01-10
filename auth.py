import hashlib
import os

# This function takes a normal password and turns it into a secure version
def hash_password(password: str) -> str:
    # A salt is random data added to a password before hashing
    # This prevents attackers from using precomputed tables
    salt = os.urandom(16)

    # PBKDF2 is a secure hashing method
    # It repeats hashing many times to slow down attackers
    hashed = hashlib.pbkdf2_hmac(
        "sha256",                 # Hash algorithm
        password.encode("utf-8"), # Convert password text into bytes
        salt,                     # Add the random salt
        100000                    # Number of iterations (higher = slower = safer)
    )

    # We store both salt and hash together
    # They are converted to readable text using hex
    # Format: salt:hash
    return f"{salt.hex()}:{hashed.hex()}"


# This function checks if a password is correct
def verify_password(stored: str, password: str) -> bool:
    # Split the stored value into salt and hash
    salt_hex, stored_hash_hex = stored.split(":", 1)

    # Hash the entered password using the same salt and settings
    new_hash = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        bytes.fromhex(salt_hex),
        100000
    )

    # Compare the newly created hash with the stored hash
    # If they match, the password is correct
    return new_hash.hex() == stored_hash_hex
