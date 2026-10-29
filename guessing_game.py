import random

secret_number = random.randint(1, 100)
attempts = 0

print("=== Number Guessing Game ===")
print("Guess a number between 1 and 100.")

while True:
    try:
        guess = int(input("Your guess: "))
        attempts += 1

        if guess < 1 or guess > 100:
            print("Enter a number between 1 and 100.")
        elif guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print("Correct! You won.")
            print("Attempts:", attempts)
            break

    except ValueError:
        print("Please enter a whole number.")
