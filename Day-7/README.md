# Day 7 – Hangman: My Solution vs Best Practices

---

## Overview

This document compares my working Hangman solution against what would be considered
best practices or a typical instructor-style solution. Both work. The goal is to
understand the tradeoffs and design decisions behind each approach.

---

## My Solution (Summary)

- Used a function `displays(result)` that accepts the previous display state as a parameter
- Returned a tuple of 3 values: `display, guess, checker`
- Unpacked the tuple outside the function: `result, guessed, check = displays(result)`
- Used `correct_letters` as a global list accessible inside the function
- Printed the hint inside the function immediately after the player guesses
- Used a `while` loop with a direct condition: `while guess_chances > 0 and result != chosen_word`
- Tracked duplicate guesses by checking `if guess in correct_letters` before appending

---

## Instructor / Best Practice Solution (Summary)

- Used a simpler loop structure with a `game_over = False` boolean flag
- Controlled loop exit by setting `game_over = True` inside `if` blocks
- Checked win condition with `if "_" not in display`
- Checked loss condition with `if lives == 0`
- Built display letter by letter with a 3-branch if/elif/else inside the loop:
  - `if letter == guess` — current guess match
  - `elif letter in correct_letters` — previously guessed letter
  - `else` — underscore
- Kept input, display logic, and game state all in the main loop without a separate function

---

## Key Differences

```
+----------------------+-----------------------------+----------------------------+
| Area                 | My Approach                 | Instructor Approach        |
+----------------------+-----------------------------+----------------------------+
| Loop control         | while condition directly    | boolean flag game_over     |
| Display function     | yes, returns tuple          | no function, inline loop   |
| Duplicate check      | before append, early return | not always handled         |
| Win condition        | result == chosen_word       | "_" not in display         |
| Hint printing        | inside function             | inside main loop           |
| Return values        | tuple of 3                  | no return needed           |
+----------------------+-----------------------------+----------------------------+
```

---

## Win Condition Comparison

**My approach:**
```
result == chosen_word
```
Compares the fully revealed display string directly to the chosen word.
Works because when every letter is guessed, display and chosen_word are identical.

**Instructor approach:**
```
"_" not in display
```
Checks if any blanks remain. If no underscores exist, all letters are revealed.
Slightly more flexible — works regardless of what the word is.

---

## Loop Control Comparison

**My approach — direct condition:**
```
while guess_chances > 0 and result != chosen_word:
    ...
```
Clean and concise. Both exit conditions live in one place.
Harder to extend if more ending conditions are added later.

**Instructor approach — boolean flag:**
```
game_over = False
while not game_over:
    if lives == 0:
        game_over = True
    if "_" not in display:
        game_over = True
```
More verbose but scales better. Common pattern in real game development
where many different events can end the game.

---

## Display Logic Comparison

**My approach — check history list:**
```
for letter in chosen_word:
    if letter in correct_letters:
        display += letter
    else:
        display += "_"
```
Appends guess to correct_letters before the loop runs.
One condition handles both current and previous guesses.
Cleaner and more concise.

**Instructor approach — check current and history separately:**
```
for letter in chosen_word:
    if letter == guess:
        display += letter
        correct_letters.append(letter)
    elif letter in correct_letters:
        display += letter
    else:
        display += "_"
```
Appends inside the loop. Needs the elif to handle previously guessed letters.
More explicit but requires an extra branch.

---

## What My Solution Did Well

- Cleaner display logic — one condition instead of three
- Proper duplicate handling with early return
- Tuple unpacking to pass state cleanly in and out of a function
- Direct while condition that reads clearly

## What The Instructor Solution Does Better

- Boolean flag pattern scales to more complex games
- No function means less complexity for a beginner project
- Easier to follow top to bottom without jumping in and out of a function

---

## Final Note

Both solutions solve the problem. The differences are about design philosophy —
simplicity vs scalability, inline vs modular. At this stage, understanding why
each decision was made matters more than which one is "right."