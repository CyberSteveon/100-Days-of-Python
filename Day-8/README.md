# Caesar Cipher

A Python implementation of the classic Caesar cipher encryption technique, built as part of the 100 Days of Code curriculum (Day 8).

## What It Does

Encrypts and decrypts messages by shifting each letter in the alphabet by a specified number of positions. Non-alphabetic characters (spaces, numbers, symbols) are preserved as-is.

**Example:**
```
Message:   hello world
Shift:     3
Encrypted: khoor zruog
```

## Project Structure

```
caesar_cipher/
├── Day-8.py       # User input, validation loop, and program flow
├── caesar.py     # Core caesar() function (encrypt + decrypt)
└── art.py        # ASCII art logo
```

## How to Run

```bash
python main.py
```

## Usage

1. Choose `encrypt` or `decrypt`
2. Enter your message
3. Enter a shift number (1–26)
4. View the result
5. Choose to go again or quit

## How It Works

### Encrypting
Each letter is shifted right in the alphabet by the shift amount. If the shift goes past `z` it wraps back around to `a` using the modulo operator (`% 26`).

```
a + shift of 3 = d
z + shift of 1 = a  (wraps around)
```

### Decrypting
The shift is flipped negative, reversing the encryption.

```
d - shift of 3 = a
```

### Handling Large Shift Numbers
Shift numbers greater than 26 are handled automatically via modulo:
```
shift of 27 = shift of 1
shift of 52 = shift of 0
```

## Features

- Encrypt and decrypt messages
- Handles uppercase and lowercase input
- Preserves spaces, numbers, and special characters
- Input validation — only accepts `encrypt` or `decrypt`
- Repeats until the user chooses to quit

## Built With

- Python 3
- No external libraries

## Author

Steven — [GitHub: CyberSteveon](https://github.com/CyberSteveon)