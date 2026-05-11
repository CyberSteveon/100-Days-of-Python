def caesar(words, shift, direction):
    alphabet = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g',
        'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's',
        't', 'u', 'v', 'w', 'x', 'y', 'z']
    new_words = ""
    if direction == "decrypt":
        shift *= -1
    for letter in words.lower():
        if letter in alphabet:
            new_words += alphabet[(alphabet.index(letter) + shift) % 26]
        else:
            new_words += letter
    return new_words

