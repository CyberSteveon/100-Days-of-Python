# A small game for finding treasure - Takes choice based inputs
# Goal is for if statement practice

print("Welcome to treasure Island! Lets see if you can get to the treasure.")

direction = input('You\'re at a forked road, would you like to go "left" or "right"? ').lower()

if direction == "left":
    swim = input('You\'ve come to a river and see a bunch of bears! '
                 'Would you like to "swim" or "wait"? ').lower()

    if swim == "wait":
        door = input('After waiting out the bears you search along the river bed '
                     'and found some doors! What door will you take? '
                     'Blue, Red, or Yellow? ').lower()

        if door == "yellow":
            print("You've happened upon a treasure chest! You've won!")
        elif door == "red":
            print("You walked in on a dragon! Game over!")
        elif door == "blue":
            print("You walked in on the leviathan! Game over!")
        else:
            print("You're not very good at treasure hunts. Goodbye!")

    else:
        print("The current of the river was too strong. Game Over!")

else:
    print("You've been bitten by a venomous snake. Game over!")