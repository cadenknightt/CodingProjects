# Allows for random number generation.
import random

# Main guess the number game function
def guess_the_number_game():
     # Give introduction to the game:
     print("\nWELCOME TO GUESS THE NUMBER!")
     print("- I am thinking of a number from 1 and 400.")
     print("- Guess a nunber and I will say higher or lower.\n")

     # The "secret_num" variable allows the computer to choose a number from 1 to 400.
     # The "attempts" variable defines the starting number of attempts a user has:
     secret_number = random.randint(1, 400)
     attempts = 0

     # While user has not won the game yet, run loop:
     while True: 
          # Allows user to guess a number until correct:
          try:
               guess = int(input("Place your guess: "))
          # When guess is not an integer, give an error:
          except ValueError:
               print("Please enter a valid number.")
               continue
          # Add 1 to "attempts" variable each time user fails to guess number.
          attempts += 1
          # If guess is lower than secret_number:
          if guess < secret_number:
               print("Higher!\n")
          # If guess is higher than secret_number
          elif guess > secret_number:
               print("Lower!\n")
          # If guess equals secret_number:
          elif guess == secret_number:
               print(f"Good job! {secret_number} was guessed in {attempts} attempts!\n")
               break

     # Asks if user wants to play again, if not then end program:  
     while True:
          playagain = input("Would you like to play again? (y/n): ").lower()
          # Re-run program if yes:
          if playagain in ["yes", "y"]:
               guess_the_number_game()
          # Quit if no:
          elif playagain in ["no", "n"]:
               print("Thanks for playing!\n")
               break
          # If neither option is entered:
          else:
               print("Please enter 'y' for yes or 'n' for no.\n")

if __name__ == "__main__":
     guess_the_number_game()
