# 🎯 Number Guessing Game (CLI Version)
# --------------------------------------------------
# Ye game terminal me chalega
# Computer random number choose karega
# User guess karega until correct
# --------------------------------------------------

# 🎲 Random number generate karne ke liye library
import random


# 🚀 Main game function
def play_game():

    # 🔢 Computer 1 se 100 ke beech number choose karega
    secret_number = random.randint(1, 100)

    # 🔁 Number of attempts count karne ke liye
    attempts = 0

    print("\n🎯 Welcome to Number Guessing Game!")
    print("👉 Guess a number between 1 and 100\n")

    # ♻ Loop tab tak chalega jab tak correct guess nahi hota
    while True:

        # 👤 User se input lena
        guess = int(input("Enter your guess: "))

        # ➕ Attempt count badhao
        attempts += 1

        # 🔽 Agar guess chhota hai
        if guess < secret_number:
            print("📉 Too low! Try again.\n")

        # 🔼 Agar guess bada hai
        elif guess > secret_number:
            print("📈 Too high! Try again.\n")

        # ✅ Agar correct hai
        else:
            print(f"🎉 Correct! You guessed in {attempts} attempts.")
            break


# ▶ Program start
if __name__ == "__main__":
    play_game()
