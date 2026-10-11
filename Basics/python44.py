import random
import string

def generate_password(length=12, use_symbols=True):
    pool = string.ascii_letters + string.digits
    if use_symbols:
        pool += string.punctuation
    
    return "".join(random.choice(pool) for _ in range(length))

user_length = int(input("Password length (e.g., 12): ") or 12)
include_symbols = input("Include symbols? (y/n): ").strip().lower() == "y"

print(f"Generated Password: {generate_password(user_length, include_symbols)}")