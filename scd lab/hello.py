import random

number = random.randint(1, 10)
attempts = 0

print("🎯 Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 10.")
print("Type 'q' anytime to quit.\n")

while True:
    guess = input("Enter your guess: ")

    if guess.lower() == 'q':
        print("👋 Thanks for playing! Goodbye!")
        break

    if not guess.isdigit():
        print("⚠️ Please enter a valid number!")
        continue

    guess = int(guess)
    attempts += 1

    if guess == number:
        print(f"🎉 Correct! You guessed it in {attempts} tries.")
        break
    elif guess < number:
        print("⬆️ Too low! Try again.")
    else:
        print("⬇️ Too high! Try again.")
