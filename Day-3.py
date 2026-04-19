print("Welcome to treasure Island! Lets see if you can get to the treasure.")

direction = input('You\'re at a forked road, would you like to go "left" or "right"? ').lower()

if direction == "left":                          # Step 1: correct path
    swim = input('You\'ve come to a river and see a bunch of bears! '
                 'Would you like to "swim" or "wait"? ').lower()

    if swim == "wait":                           # Step 2: correct choice
        door = input('After waiting out the bears you search along the river bed '
                     'and found some doors! What door will you take? '
                     'Blue, Red, or Yellow? ').lower()

        if door == "yellow":                     # Step 3: correct door
            print("You've happened upon a treasure chest! You've won!")
        elif door == "red":                      # Step 3: wrong door
            print("You walked in on a dragon! Game over!")
        elif door == "blue":                     # Step 3: wrong door
            print("You walked in on the leviathan! Game over!")
        else:                                    # Step 3: invalid input
            print("You're not very good at treasure hunts. Goodbye!")

    else:                                        # Step 2: wrong choice
        print("The current of the river was too strong. Game Over!")

else:                                            # Step 1: wrong path
    print("You've been bitten by a venomous snake. Game over!")