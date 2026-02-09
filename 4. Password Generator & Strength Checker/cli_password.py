# 🔐 Password Generator + Strength Checker (CLI)
# ---------------------------------------------------
# Random password generate karega
# Password strength bhi check karega
# ---------------------------------------------------

import random     # random characters choose karne ke liye
import string     # letters + digits + symbols


# 🔑 Password generate function
def generate_password(length):

    # 🔤 characters ka pool banao
    characters = string.ascii_letters + string.digits + string.punctuation

    # 🎲 random password generate karo
    password = "".join(random.choice(characters) for _ in range(length))

    return password


# 💪 Strength check function
def check_strength(password):

    score = 0

    # length check
    if len(password) >= 8:
        score += 1

    # uppercase check
    if any(c.isupper() for c in password):
        score += 1

    # digits check
    if any(c.isdigit() for c in password):
        score += 1

    # symbols check
    if any(c in string.punctuation for c in password):
        score += 1

    # score decide
    levels = ["Weak 😢", "Medium 🙂", "Strong 💪", "Very Strong 🔥"]

    return levels[score-1] if score > 0 else "Very Weak"


# 🚀 Main program
length = int(input("Enter password length: "))

pwd = generate_password(length)

print("\n🔑 Generated Password:", pwd)
print("💪 Strength:", check_strength(pwd))
