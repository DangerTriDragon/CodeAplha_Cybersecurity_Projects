import os
import sys
import subprocess
import yaml
import random

# Hardcoded credentials (Security Risk)
USERNAME = "admin"
PASSWORD = "password123"

# Insecure input handling (SQL Injection vulnerability)
user_input = input("Enter username: ")
query = "SELECT * FROM users WHERE username = '" + user_input + "';"
print("Executing query:", query)

# Insecure subprocess call (Command Injection vulnerability)
cmd = input("Enter a command: ")
subprocess.call(cmd, shell=True)

# Using eval() unsafely (Remote Code Execution vulnerability)
user_code = input("Enter Python code to execute: ")
eval(user_code)

# Insecure YAML loading (Arbitrary Code Execution vulnerability)
def load_config():
    with open("config.yaml", "r") as f:
        config = yaml.load(f)  # Unsafe YAML loading
    return config

# Weak random number generator for security-sensitive operations
token = random.randint(100000, 999999)  # Predictable security token
print(f"Generated token: {token}")

# Unused variable (Code quality issue)
unused_var = "I am never used"

if __name__ == "__main__":
    print("Vulnerable script running...")
