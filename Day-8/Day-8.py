from caesar import caesar
import art

print(art.logo)

should_continue = True

while should_continue:
    what_direction = input("Do you want to encrypt or decrypt? ").lower()

    while what_direction not in ["encrypt", "decrypt"]:
        what_direction = input("Please type 'encrypt' or 'decrypt': ").lower()

    if what_direction == "decrypt":
        phrase = input("Enter the encrypted phrase: ")
    elif what_direction == "encrypt":
        phrase = input("Enter your message: ")

    shift_number = int(input("What number are we shifting by? "))
    print(caesar(phrase, shift_number, what_direction))

    go_again = input("Type 'yes' to go again or 'no' to quit: ")
    if go_again.lower() == "no":
        should_continue = False
        print("Goodbye!")