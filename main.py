import random
import string

def generate_password(length):
    if length < 8:
        print("Password length should be at least 8 characters.")
        return None

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    all_characters = lowercase + uppercase + digits + symbols

    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(symbols)
    ]

    for _ in range(length - 4):
        password.append(random.choice(all_characters))

    random.shuffle(password)

    return "".join(password)

length = int(input("Enter password length: "))
password = generate_password(length)

if password:
    print("Generated Password:", password)