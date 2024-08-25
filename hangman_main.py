#from replit import clear
import random
# importing the words
from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6
guessed = []
# importing the logo and stages later one
from hangman_art import logo

print(logo)

# print(f'tester is {chosen_word}.')

# Create blanks
display = []
for _ in range(word_length):
    display += "_"
# print(display)
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in guessed:
        print(f"You've already guessed this letter '{guess}'. Try again.")
    else:
        guessed += guess
        print(guessed)
    #clear()
    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter

    # Check if user is wrong.
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's is not in the word. Lost 1 life")
        if lives == 0:
            end_of_game = True
            print("You lose.")

    # Joining the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    from hangman_art import stages

    print(stages[lives])