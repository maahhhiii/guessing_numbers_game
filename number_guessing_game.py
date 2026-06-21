import random

def get_difficulty():
    """Prompts user for difficulty and returns the maximum range value."""
    print("\n--- Choose Difficulty ---")
    print("1. Easy (Range: 1 - 10)")
    print("2. Medium (Range: 1 - 50)")
    print("3. Hard (Range: 1 - 100)")
    
    while True:
        choice = input("Select a difficulty level (1-3): ").strip()
        if choice == '1':
            return 10
        elif choice == '2':
            return 50
        elif choice == '3':
            return 100
        else:
            print("Invalid selection. Please choose 1, 2, or 3.")

def get_valid_guess(max_range):
    """Validates that the user input is a number within the valid range."""
    while True:
        try:
            guess = int(input(f"Enter your guess (1-{max_range}): "))
            if 1 <= guess <= max_range:
                return guess
            else:
                print(f"Out of bounds! Please guess a number between 1 and {max_range}.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def play_game(max_range):
    """Handles the main guessing logic and returns the number of attempts taken."""
    secret_number = random.randint(1, max_range)
    attempts = 0
    
    print(f"\nI've chosen a number between 1 and {max_range}. Start guessing!")
    
    while True:
        guess = get_valid_guess(max_range)
        attempts += 1
        
        if guess < secret_number:
            print("Too low! Try a higher number.")
        elif guess > secret_number:
            print("Too high! Try a lower number.")
        else:
            print(f"Correct! You guessed the number in {attempts} attempts.")
            return attempts

def main():
    best_score = float('inf')
    
    print("Welcome to the Number Guessing Game!")
    
    while True:
        max_range = get_difficulty()
        attempts_taken = play_game(max_range)
        
        if attempts_taken < best_score:
            best_score = attempts_taken
            print(f" New Best Score: {best_score} attempts!")
        else:
            print(f"Current Best Score: {best_score} attempts.")
            
        replay = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if replay not in ['y', 'yes']:
            print("\nThanks for playing! Final Best Score:", best_score if best_score != float('inf') else 0)
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
