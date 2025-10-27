import random


def number_guessing_game():
    print("Welcome to my number guessing game!")
    print("I'm thinking of a number from 1-100. Can you guess which one it is?")

    print("Please select a difficulty")
    print("1. Easy (10 tries)")
    print("2. Medium (5 tries)")
    print("3. Hard (3 tries)")

    choice = input("Enter difficulty: ")
    if choice == "1":
        chances = 10
        print("You have 10 tries.")
    elif choice == "2":
        chances = 5
        print("You have 5 tries.")
    else:
        choice = "3"
        print("You have 3 tries")
    number = random.randint(1, 100)
    attempts = 0
    game_over = False

    while attempts < chances and not game_over:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number")
            continue

        attempts += 1

        if guess == number:
            print(
                f" Congratulations! You guessed the correct number in {attempts} attempts.")
            game_over = True
        elif guess < number:
            print(f" The number is higher than {guess}")
        else:
            print(f" The number is smaller than {guess}")

    if not game_over:
        print(f" You've run out of tries! The number was {number}.")


number_guessing_game()
