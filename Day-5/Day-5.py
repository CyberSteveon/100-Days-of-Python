# A password generator
# Goal is to practice manipulating lists


## student_scores = [ 180, 124, 165, 173, 189, 169, 146]
##
## max_score = 0
## for score in student_scores:
##     if score > max_score:
##         max_score = score
##         print(max_score)
# total = 0
# for number in range(1,101):
#     total += number
# print(total)
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator!")
n_letters = int(input("How many letters would you like?\n"))
n_symbols = int(input("How many symbols would you like?\n"))
n_numbers = int(input("How many numbers would you like?\n"))
password = ""

for _ in range(n_letters):
    password += random.choice(letters)

for _ in range(n_symbols):
    password += random.choice(symbols)

for _ in range(n_numbers):
    password += random.choice(numbers)

char = list(password)
random.shuffle(char)
result = ''.join(char)
print(result)

