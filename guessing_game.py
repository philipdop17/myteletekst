import random

def play_game():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    
    print("Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess it.\n")
    
    while attempts < max_attempts:
        try:
            # Get player's guess
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts} - Enter your guess: "))
            attempts += 1
            
            # Check the guess
            if guess < secret_number:
                print("Too low! Try a higher number.\n")
            elif guess > secret_number:
                print("Too high! Try a lower number.\n")
            else:
                print(f"\n🎉 Congratulations! You guessed it in {attempts} attempts!")
                return
                
        except ValueError:
            print("Please enter a valid number!\n")
            continue
    
    print(f"\n😔 Game over! The number was {secret_number}.")

def main():
    while True:
        play_game()
        
        # Ask if player wants to play again
        play_again = input("\nWould you like to play again? (yes/no): ").lower()
        if play_again not in ['yes', 'y']:
            print("Thanks for playing! Goodbye!")
            break
        print("\n" + "="*50 + "\n")

if __name__ == "__main__":
    main()
