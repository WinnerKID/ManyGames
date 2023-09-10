import random

def start_game():
    while True:
        user_choice = input("Rock, paper, scissors, or exit to quit?\n").lower()
        if user_choice == "exit":
            print("Thanks for playing! Exiting the game.")
            import __main__
            __main__.menu_start()
            break

        choices = ["rock", "paper", "scissors"]

        if user_choice in choices:
            computer_choice = random.choice(choices)
            print(f"Computer chooses {computer_choice}")

            if user_choice == computer_choice:
                print("It's a tie!")
            elif (
                (user_choice == "rock" and computer_choice == "scissors")
                or (user_choice == "paper" and computer_choice == "rock")
                or (user_choice == "scissors" and computer_choice == "paper")
            ):
                print("You win!")
            else:
                print("Computer wins!")
        else:
            print("Please choose a valid option (rock, paper, scissors, or exit)")

if __name__ == "__main__":
    start_game()
