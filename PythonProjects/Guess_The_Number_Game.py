# Allows for random number generation.
import random

# Main guess the number game function
def guess_the_number_game():
     print("\nWELCOME TO GUESS THE NUMBER!")
     print("- I am thinking of a number from 1 and 400.")
     print("- Guess a nunber and I will say higher or lower.\n")

     # The secret_num variable allows the computer to choose a number from 1 to 400.
     # The attempts variable defines the starting number of attempts a user has.
     secret_num = random.randint(1, 400)
     attempts = 0

     # While user has not won the game yet, run loop.
     while True: 
          try:
               guess = int(input("Place your guess: "))
          except ValueError:
               print("Please enter a valid number.")
               continue
          # Add 1 to attempts each time user fails to guess number.
          attempts += 1

          # Give message based on user's guess.
          if guess < secret_num:
               print("Higher!\n")
          elif guess > secret_num:
               print("Lower!\n")
          else:
               print(f"Good job! You guessed the number in {attempts} attempts!")
               break

     # When the game is over, ask if the user wants to play again.
     while True:
          playagain = input("\nWould you like to play again? (y/n): ").strip().lower()
          if playagain in ["yes", "y"]:
               guess_the_number_game()
          elif playagain in ["no", "n"]:
               print("Thanks for playing!\n")
               break
          else:
               print("Please enter 'y' for yes or 'n' for no.\n")

if __name__ == "__main__":
     guess_the_number_game()
