import time

def print_with_typing(text, delay=0.08):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

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
            import chatbot
            break
        elif choice == "3":
            import rps
            rps.start_game()
        elif choice == "4":
            print()
        elif choice == "5":
            print()
        elif choice == "6":
            print('Exiting the menu.')
            exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu_start()
