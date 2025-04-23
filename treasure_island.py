print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
first_choice = input(
    'You are at a crossroad, where do you choose to go "left" or "right"? '
)

if first_choice.lower() == "left":
    second_choice = input(
        'You\'ve come to a lake, \nthere is an island in the middle of the lake. \nType "wait" to wait for a boat \nType or "swim" to swim across. '
    )

    if second_choice.lower() == "wait":
        third_choice = input(
            "\nYou arrive at the island unharmed. \nThere is house within three doors. \nOne red, one yellow and one blue.\nWhich door do you choose? "
        )

        if third_choice.lower() == "yellow":
            print("Congratulations! You've found the treasure!")
        elif third_choice.lower() == "red":
            print("You've been eaten by a shark!")
        elif third_choice.lower() == "blue":
            print("You've fallen into a pond and drowned!")
        else:
            print("Invalid choice. You died.")
    else:
        print("You got swallowed by a whale! Game over.")

else:
    print("You fell into a hole and died. Game over.")
