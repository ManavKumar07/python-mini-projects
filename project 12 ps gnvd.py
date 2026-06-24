# project 4:
# Password generator & validator:
# Generates random strong passwords using a random and string modules, validates user enetred passswords with custom exception if rules not met
import random
import string
# Custom Exception
class WeakPasswordError(Exception):
    pass
def generate_password(length=8):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ""
    for i in range(length):
        password += random.choice(chars)
    return password
def validate_password(password):
    if len(password) < 8:
        raise WeakPasswordError("Password must be at least 8 characters")
    if not any(ch.isupper() for ch in password):
        raise WeakPasswordError("Password must contain an uppercase letter")
    if not any(ch.isdigit() for ch in password):
        raise WeakPasswordError("Password must contain a digit")

    if not any(ch in string.punctuation for ch in password):
        raise WeakPasswordError("Password must contain a special character")
# Main Program
try:
    print("Generated Strong Password:", generate_password())
    user_pass = input("Enter your password to validate: ")
    validate_password(user_pass)
    print("Password is strong ")
except WeakPasswordError as e:
    print("Weak Password :", e)
