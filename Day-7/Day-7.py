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
print("Hint is " + placeholder)



def displays():
    guess = input("What letter would you like to guess? ").lower()
    correct_letters.append(guess)
    display = ""
    for letter in chosen_word:
        if letter in correct_letters:
            display += letter
        else:
            display += "_"

    return display, guess


result, guessed = "", ""
while guess_chances > 0 and result != chosen_word:
    result, guessed = displays()
    if guessed not in chosen_word:
        guess_chances -= 1
        print("Wrong guess. Try again.")
        print(result)
    elif guessed in correct_letters:
        print("Correct")
        print(result)
    print(hangman_stages[6 - guess_chances])


if guess_chances == 0:
    print("Sorry, you've been hanged.")
else:
    print(f"Congratz! You win!\nWord is {chosen_word}")
'''
        while game going:get guess
    check if already guessed → skip/warn
    otherwise → call displays once, store result
    if result == chosen_word → win
    if guess not in chosen_word → lose a life
    '''




