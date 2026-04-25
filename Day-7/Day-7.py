import random
from ascii_art import hangman_stages
from game_words import word_list

chosen_word = random.choice(word_list)
correct_letters = []
guess_chances = 6


placeholder = ""
for letters in chosen_word:
    placeholder += "_"

print(chosen_word)
print("Welcome to Hangman!")
print("Hint is " + placeholder)



def displays(result):
    guess = input("What letter would you like to guess? ").lower()
    hints = "Hint is "
    checker = ""
    if guess in correct_letters:
        checker = f"********** Letter {guess} used already! **********"
        return result, guess,checker
    correct_letters.append(guess)
    display = ""
    for letter in chosen_word:
        if letter in correct_letters:
            display += letter
        else:
            display += "_"

    hints += display
    print(hints)
    return display, guess, checker


result, guessed, hint, check = "", "", "", ""
while guess_chances > 0 and result != chosen_word:
    result, guessed, check = displays(result)
    if guessed not in chosen_word:
        guess_chances -= 1
        print("Wrong guess. Try again.")
    elif guessed in correct_letters:
        print("Correct")


    print(hangman_stages[6 - guess_chances])
    print(check)
    print(f"    ********** {6 - guess_chances}/6 Lives left **********")



if guess_chances == 0:
    print("        ********** YOU LOSE **********")
    print(f"Sorry correct word was {chosen_word}, you've been hanged.")
else:
    print(f"Congratz! You win!\nWord is {chosen_word}")




