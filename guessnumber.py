# The import statement makes the random generator available
import random

# This function acts as a guess the number simulator named playgame
def playgame():
     print("\nWelcome to Guess the Number!")
     print("I am thinking of a number from 1 and 500.")
     print("Start guessing and I will say higher or lower.\n")

     # "secret_num" defines what the computer chooses as its number
     # between 1 and 500
     secret_num = random.randint(1, 500)
     # "attempts" is a placeholder for the starting number of guesses the user has
     attempts = 0

     # This code creates a loop for the game until the number is guessed correctly
     while True: 
          try:
               guess = int(input("Place your guess: "))
          except ValueError:
               print("Please enter valid number.")
               continue

          # This code adds the number attempts the user has made each time the program is run.
          attempts += 1

          # The if and else statements provide a message to the user based on the user's
          # guess on the random number computer stores
          if guess < secret_num:
               print("Higher!\n")
          elif guess > secret_num:
               print("Lower!\n")
          else:
               print(f"Good job! You guessed the number in {attempts} attempts!")
               break

# this allows the user to play the game and when the number is guessed
# the user can decide to play again or stop (which ends the game).
while True:
     playgame()
     playagain = input("\nWould you like to play again? (y/n): ")
     if playagain != "yes" and playagain != "y":
          print("\nThanks for playing! See ya!")
          break
