import random
import string

words = ["mango", "saturn", "red"]


def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 7
    while len(word_letters) > 0 and lives > 0:
        print("You have ", lives, " and you have used these letters: ",
              ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]

        print("Current Word: ", ' '.join(word_list))

        user_input = input("Guess a letter: ").upper()
        if user_input in alphabet:
            used_letters.add(user_input)
            if user_input in word_letters:
                word_letters.remove(user_input)
                lives -= 1

            else:
                lives -= 1
                print("Your letter,", user_input, "is not in the word.")

        elif user_input in used_letters:
            print("You have already used that letter. Please try a different one.")

        else:
            print("Invalid Character.")

    if lives == 0:
        print('You died, sorry. The word was', word)
    else:
        print('YAY! You guessed the word', word, '!!')


hangman()
