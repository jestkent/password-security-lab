Password Security & Brute Force Demo (Beginner Cybersecurity Project)
Overview

This project is a beginner friendly cybersecurity lab that demonstrates how passwords are securely stored and how weak passwords can still be cracked using a brute force dictionary attack.

It is designed for learning purposes only and runs locally on your own computer.

What This Project Demonstrates

How passwords are hashed instead of stored as plain text

Why salting passwords is important

How login verification works without knowing the real password

How dictionary based brute force attacks work

Why weak passwords are dangerous even with strong encryption

How It Works (Simple Explanation)
1. Secure Password Storage

When a user registers:

The password is never saved directly

A random salt is generated

The password is hashed using PBKDF2 with SHA-256

Only the salt and hash are stored

2. Login Verification

When a user logs in:

The entered password is hashed again using the same salt

The new hash is compared to the stored hash

If they match, access is granted

3. Brute Force Dictionary Attack

The attack demo:

Reads a stolen password hash

Tries common passwords from a small dictionary

Hashes each guess using the same method

Stops when a match is found or the list ends

This shows how attackers think and why password strength matters.

Project Structure
password-security-lab/
├── auth.py          # Handles password hashing and verification
├── main.py          # User registration and login system
├── attack_demo.py   # Dictionary-based brute force attack demo
├── users.txt        # Stores usernames and hashed passwords
├── README.md

How to Run the Project
Step 1: Register a User
python main.py


Choose:

1 Register

Example credentials for demo:

Username: testuser

Password: password

Step 2: View Stored Passwords

Open users.txt.

You will see something like:

testuser,9a3f...:e1b2...


This shows that the real password is never stored.

Step 3: Run the Brute Force Demo
python attack_demo.py


Enter:

testuser

The program will try common passwords until it finds a match.

Why This Matters in Cybersecurity

Attackers often steal hashed passwords, not real ones

Weak passwords can still be cracked using guessing attacks

Salting prevents reuse of precomputed hash tables

Slower hashing algorithms reduce attack speed

User behavior is as important as encryption

Skills Demonstrated

Cybersecurity fundamentals

Password hashing and salting

Authentication concepts

Attacker vs defender mindset

Python programming

Secure coding practices

Ethical Notice

This project is for educational purposes only.

No real accounts are attacked

Only test users created by the developer are used

The password list is intentionally small and safe

Possible Improvements

Add password strength validation

Lock accounts after failed attempts

Log attack attempts

Convert to a Flask web application

Expand dictionary size for performance testing

Author

Created as a hands-on cybersecurity learning project.