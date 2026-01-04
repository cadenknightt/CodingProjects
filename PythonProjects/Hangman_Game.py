# Imports random word generator
from wonderwords import RandomWord

# Main hangman game function
def hangman_game():
     # Give introduction to game:
     print("\nWELCOME TO HANGMAN!")
     print("- Fill in the empty spaces with letters or words to win.")
     print("- Wrong letters take 1 life and wrong words cost 2 lives.")

     # Computer chooses a word from the word generator:
     d = RandomWord()
     word = d.word()

     # These variables set beginning values and allow for updates throughout the game:
     random_word = word.upper()
     guessed_letters = set()
     guessed_words = set()
     lives = 5
     # Allows hangman to print based on lives left:
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

     # While lives > 0 show info and run loop:
     while lives > 0:
          # Display the hangman visual based on lives:
          print(hangman_stages[5-lives])
          # Display the fill in the blank word display:
          display = ' '.join([char if char in guessed_letters else '_' for char in random_word])
          print(f"    {display}\n")
          # Display remaining lives, guessed letters, and guessed words:
          print(f"LIVES REMAINING: {lives}")
          print(f"GUESSED LETTERS: {', '.join(sorted(guessed_letters)).upper() or 'NONE YET'}")
          print(f"GUESSED WORDS: {', '.join(sorted(guessed_words)).upper() or 'NONE YET'}\n")
          # If lives are at 0 then break from loop:
          if lives <= 0:
               break
          # If all the letters in guessed_letters are in random_word then break from loop.
          if all(char in guessed_letters for char in random_word):
               break

          # Run the main game:
          while True:
               prompt = input("Are you guessing a letter or word (l/w): ")
               # If user decides to guess a letter:
               if prompt in ["letter", "l"]:
                    while True:
                         letter = input("Enter a letter: ").upper()
                         # If letter doesn't have 1 value or is not alphabetical:
                         if len(letter) != 1 or not letter.isalpha():
                              print("Please enter a single letter.\n")
                              continue
                         # Give an error if letter is already in guessed_letters:
                         if letter in guessed_letters:
                              print(f"You already guessed {letter}.\n")
                              continue
                         # Add letter to guessed_letters:
                         guessed_letters.add(letter)

                         # If letter is in the random_word:
                         if letter in random_word:
                              print(f"Good guess! {letter} is in the word.\n")
                              break
                         # If letter is not in the random_word:
                         else:
                              print(f"Good try! {letter} is not in the word.\n")
                              lives -= 1
                         break
                    break
               # If user decides to guess a word:
               elif prompt in ["word", "w"]:
                    while True:
                         word = input("Enter a word: ").upper()
                         # If word doesn't have more than 2 values or is not alphabetical:
                         if len(word) < 2 or not word.isalpha():
                              print("Please enter a word with more than 2 letters.\n")
                              continue
                         # Give an error if word is already in guessed_words:
                         if word in guessed_words:
                              print(f"You already guessed {word}.\n")
                              continue
                         # Add word to guessed_words:
                         guessed_words.add(word)

                         # If word is random_word, end game:
                         if word == random_word:
                              lives = 0
                              break
                         # If word is not random_word, lose 2 lives and keep playing:
                         else:
                              print("You guessed the word incorrectly.\n")
                              lives -= 2
                         break
                    break
               # Give an error if user doesn't decide to guess a letter or word:
               else:
                    print("Please enter 'l' for letter or 'w' for word.\n")
                    continue
     
     # Display message for when the user wins:
     if random_word in guessed_words or all(char in guessed_letters for char in random_word):
          print(f"""             
|--------------------------------------------------------------
|    Yay! You correctly guessed the word!
|    The word was: {random_word}  
|--------------------------------------------------------------
""")
     # Display final hangman stage and message for when the user loses:
     else:
          print(f"""
   {hangman_stages[5]}          
|--------------------------------------------------------------
|    You lost. Better luck next time.
|    The word was: {random_word}      
|--------------------------------------------------------------
""")

     # Asks if user wants to play again, if not then end program:
     while True:
          playagain = input("Would you like to play again? (y/n): ").lower()
          # Re-run program if yes:
          if playagain in ["yes", "y"]:
               hangman_game()
          # Quit if no:
          elif playagain in ["no", "n"]:
               print("Thanks for playing!\n")
               break
          # If neither option is entered:
          else:
               print("Please enter 'y' for yes or 'n' for no.\n")

if __name__ == "__main__":
     hangman_game()
