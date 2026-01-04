# Imports random word generator
from wonderwords import RandomWord

# Main hangman game function
def hangman_game():
     print("\nWELCOME TO HANGMAN!")
     print("- Fill in the empty spaces with letters or words to win.")
     print("- Wrong letters take 1 life and wrong words cost 2 lives.")

     # Computer chooses a word from the word generator
     d = RandomWord()
     word = d.word()

     # These variables set the game beginning and allow for updates throughout the game.
     random_word = word.upper()
     guessed_letters = set()
     guessed_words = set()
     lives = 5
     hangman_stages = ["""
     -----------|
                |
                |
                |
                |
                |
     """,
     """
     -----------|
     O          |
                |
                |
                |
                |
     """,
     """
     -----------|
     O          |
     |          |
     ^          |
                |
                |
     """,
     """
     -----------|
     O          |
    \|/         |
     ^          |
                |
                |
     """,
     """
     -----------|
     O          |
    \|/         |
     ^          |
    / \         |
                |
     """,
     """
     -----------|
     O          |
   '\|/'        |
     ^          |
   _/ \_        |
                |
     """
     ]

     # While lives > 0: display the hangman visual, display, and run game loop.
     while lives > 0:
          print(hangman_stages[5-lives])
          display = ' '.join([char if char in guessed_letters else '_' for char in random_word])
          print(f"    {display}\n")
          print(f"LIVES REMAINING: {lives}")
          print(f"GUESSED LETTERS: {', '.join(sorted(guessed_letters)).upper() or 'NONE YET'}")
          print(f"GUESSED WORDS: {', '.join(sorted(guessed_words)).upper() or 'NONE YET'}\n")

          # If all the letters in guessed_letters are in random_word then break from loop.
          if all(char in guessed_letters for char in random_word):
               break

          # Run the main loop to play the game
          while True:
               prompt = input("Are you guessing a letter or word (l/w): ")
               
               # If user enters 'letter' or 'l' in input
               if prompt in ["letter", "l"]:
                    while True:
                         # Enter input for a single valid letter.
                         letter = input("Enter a letter: ").strip().upper()
                         # If the letter doesnt have 1 value or is not a alphabetical value.
                         if len(letter) != 1 or not letter.isalpha():
                              print("Please enter a single letter.\n")
                              continue
                         # Give an error if the letter is already in guessed_letters list.
                         if letter in guessed_letters:
                              print("You already guessed that letter.\n")
                              continue
                         # Adds the input to a guessed_letters list.
                         guessed_letters.add(letter)

                         # If letter is in the random_word.
                         if letter in random_word:
                              print(f"Good guess! {letter} is in the word.\n")
                              break
                         # If letter is not in the random_word.
                         else:
                              print(f"Good try! {letter} is not in the word.\n")
                              lives -= 1
                         break
                    break

               # If user enters 'word' or 'w' in input.
               elif prompt in ["word", "w"]:
                    while True:
                         # Enter input for word.
                         word = input("Enter a word: ").strip().upper()
                         # If input is less than two characters or is not alphabetical
                         if len(word) < 2 or not word.isalpha():
                              print("Please enter a word with more than 2 letters.\n")
                              continue
                         # If input is in guessed words list, give an error
                         if word in guessed_words:
                              print(f"You already guessed {word}.\n")
                              continue
                         # Add input to guessed words list
                         guessed_words.add(word)

                         # If input = word, then congratulate and end game.
                         if word == random_word:
                              lives = 0
                              break
                         # If the input does not match the correct word, give an error.
                         else:
                              print("You guessed the word incorrectly.\n")
                              lives -= 2
                         break
                    break

               # If user doesn't enter 'letter'/'l' or 'word'/'w'.
               else:
                    print("Please enter 'letter'/'l', or 'word'/'w'.\n")
                    continue
     
     # Display message for when the user wins or loses either with words or letters.
     if word in guessed_words or all(char in guessed_letters for char in random_word):
          print(f"""             
|--------------------------------------------------------------
|    Yay! You correctly guessed the word!
|    The word was: {random_word}  
|--------------------------------------------------------------
""")
     else:
          print(hangman_stages[5])
          print(f"""             
|--------------------------------------------------------------
|    You lost. Better luck next time.
|    The word was: {random_word}      
|--------------------------------------------------------------
""")

     # Ask if the user wants to play again when the game is over.
     while True:
          playagain = input("Would you like to play again? (y/n): ").strip().lower()
          if playagain in ["yes", "y"]:
               hangman_game()
          elif playagain in ["no", "n"]:
               print("Thanks for playing!\n")
               break
          else:
               print("Please enter 'y' for yes or 'n' for no.\n")

if __name__ == "__main__":
     hangman_game()
