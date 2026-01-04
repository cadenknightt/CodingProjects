# Imports random word generator
from wonderwords import RandomWord

# Main game function
def hangman_game():
     print("\nWelcome to Hangman!")

     # Computer chooses the word
     d = RandomWord()
     word = d.word()
     while word is None or not word.isalpha():
           word = d.word()

     # These attributes help the user know what words and letters have been guessed, and the starting number for lives left
     word = word.upper()
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

     # While lives are greater than 0 display the appropriate hangman visual and word display
     while lives > 0:
          print(hangman_stages[5-lives])

          display = ' '.join([char if char in guessed_letters else '_' for char in word])
          print(f"    {display}\n")
          print(f"LIVES REMAINING: {lives}")
          print(f"GUESSED LETTERS: {', '.join(sorted(guessed_letters)).upper() or 'NONE YET'}")
          print(f"GUESSED WORDS: {', '.join(sorted(guessed_words)).upper() or 'NONE YET'}\n")

          if all(char in guessed_letters for char in word):
               break

          # Run the main loop to play the game
          while True:
               prompt = input("Are you guessing a letter or word (l/w): ")
               
               # If user enters 'letter' or 'l', than provide the following prompts based on conditions
               if prompt in ["letter", "l"]:
                    while True:
                         # Enter input for a single letter
                         letter_selected = input("Enter a letter: ").strip().upper()
                         # If input doesnt equal 1 number or is not a alphabetical
                         if len(letter_selected) != 1 or not letter_selected.isalpha():
                              print("Please enter a single letter.\n")
                              continue
                         # If input is already in guessed letters list, give an error
                         if letter_selected in guessed_letters:
                              print("You already guessed that letter.\n")
                              continue
                         
                         # Adds the input to a guessed letters list
                         guessed_letters.add(letter_selected)

                         # If input is the word
                         if letter_selected in word:
                              print(f"Good guess! '{letter_selected}' is in the word.\n")
                              break
                         # If input is not the word
                         else:
                              print(f"Good try! '{letter_selected}' is not in the word.\n")
                              lives -= 1
                         break
                    break

               # If user enters 'word' or 'w' in input, than provide the following prompts based on conditions
               elif prompt in ["word", "w"]:
                    while True:
                         # Enter input for word.
                         word_selected = input("Enter a word: ").strip().upper()
                         # If input is less than two characters or is not alphabetical
                         if len(word_selected) < 2 or not word_selected.isalpha():
                              print("Please enter a word with more than 2 letters.\n")
                              continue
                         # If input is in guessed words list, give an error
                         if word_selected in guessed_words:
                              print("You already guessed that word.\n")
                              continue

                         # Add input to guessed words list if not in there already
                         guessed_words.add(word_selected)

                         # If input = word, then congratulate and end game
                         if word_selected == word:
                              print("You guessed the word correctly!\n")
                              lives = 0
                              break
                         # If the input does not match the correct word, give an error
                         else:
                              print("You guessed the word incorrectly.\n")
                              lives -= 2
                         break
                    break

               # Give an error if neither options are satisfied
               else:
                    print("Please enter 'letter'/'l', or 'word'/'w'.\n")
                    continue
     
     # Options for when the word is correctly guessed or lost (0 lives)
     if word in guessed_words or all(char in guessed_letters for char in word):
          print(f"""             
|--------------------------------------------------------------
|    Yay! You correctly guessed the word!
|    The word was: {word}  
|--------------------------------------------------------------
""")
     else:
          print(hangman_stages[5])
          print(f"""             
|--------------------------------------------------------------
|    You lost. Better luck next time.
|    The word was: {word}      
|--------------------------------------------------------------
""")

     # When the game is over, ask if the user wants to play again
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
