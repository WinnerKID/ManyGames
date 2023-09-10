import random


def guess_game():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Guess the Number game!")
    print("I'm thinking of a number between 1 and 100.")
    print("Enter 'exit' to return to the main menu.")

    while True:
        try:
            player_input = input("Enter your guess: ")
            if player_input == "exit":
                import __main__
                main.menu_start()
                break
            # Convert the player's input to an integer for guessing
            player_guess = int(player_input)
            attempts += 1

        except ValueError:
            print("Invalid input. Please enter a valid number or 'exit'.")
            continue

        # Check if the guess is correct
        if player_guess == secret_number:
            print(f"\nCongratulations! You guessed the number {secret_number} in {attempts} attempts.\n")
            import __main__
            main.menu_start()
            break
        elif player_guess < secret_number:
            print("Higher.")
        else:
            print("Lower.")




if __name__ == "__main__":
    guess_game()
