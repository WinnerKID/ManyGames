from utils import print_with_typing

def menu_start():
    while True:
        print('\nWelcome to the \'MANY GAMES\' menu\n'
              '---------------------------------------\n'
              '1. Guessing game\n'
              '2. Talk to someone\n'
              '3. Rock, paper, scissors game\n'
              '4. AI chatbot(under construction)\n'
              '5.\n'
              '6. Exit')

        choice = input("Enter your choice: ")

        if choice == "1":
            # Import and run the game script
            import game
            game.guess_game()
        elif choice == "2":
            # Import and run chatbot
            print_with_typing("Someone will come and talk to you...")
            break
        elif choice == "3":
            import rps
            rps.start_game()
        elif choice == "4":
            pass
        elif choice == "5":
            print()
        elif choice == "6":
            print('Exiting the menu.')
            exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu_start()

