import random
import time


def Print_message(Message):
    print(Message)
    time.sleep(2)


def Introduction(item, option):

    Print_message("\nYou find yourself in an open field, filled"
                  "with grass and yellow wildflowers.")
    Print_message("\nRumor has it that a " + option + " is somewhere around"
                  "here, and has been terrifying the nearby village.")
    Print_message("\nIn front of you is a house.")
    Print_message("\nTo your right is a dark cave.")
    Print_message("\nIn your hand you hold your trusty (but not very"
                  "effective) dagger.")


def Cave(item, option):
    if "sword" in item:
        Print_message("\n\nYou peer cautiously into the cave.")
        Print_message("\nYou've been here before, and gotten all"
                      " the good stuff. It's just an empty cave"
                      " now.")
        Print_message("\nYou walk back to the field.\n")
    else:
        Print_message("\n\nYou peer cautiously into the cave.")
        Print_message("\nIt turns out to be only a very small cave.")
        Print_message("\nYour eye catches a glint of metal behind a"
                      " rock.")
        Print_message("\nYou have found the magical sword of Ogoroth!")
        Print_message("\nYou discard your silly old dagger and take "
                      "the sword with you.")
        Print_message("\nYou walk back out to the field.\n")
        item.append("sword")
    Field(item, option)


def House(item, option):
    Print_message("\nYou approach the door of the house.")
    Print_message("\nYou are about to knock when the door "
                  "opens and out steps a " + option + ".")
    Print_message("\nEep! This is the " + option + "'s house!")
    Print_message("\nThe " + option + " attacks you!\n")
    if "sword" not in item:
        Print_message("You feel a bit under-prepared for this, "
                      "what with only having a tiny dagger,\n")
    while True:
        alternative2 = input("Would you like to (1) fight or (2) "
                             "run away?")
        if alternative2 == "1":
            if "sword" in item:
                Print_message("\nAs the " + option + " moves to attack, "
                              "you unsheath your new sword.")
                Print_message("\nThe Sword of Ogoroth shines brightly in "
                              "your hand as you brace yourself for the "
                              "attack,")
                Print_message("\nBut the " + option + "takes one look at "
                              "your shiny new toy and runs away!")
                Print_message("\nYou have rid the town of the " + option +
                              ". You are victorious!\n")
            else:
                Print_message("\nYou do your best...")
                Print_message("but your dagger is no match for "
                              "the " + option + ".")
                Print_message("\nYou have been defeated!\n")
            PLAY_AGAIN()
            break
        if alternative2 == "2":
            Print_message("\nYou run back into the field. "
                          "\nLuckily, you don't seem to have been "
                          "followed.\n")
            Field(item, option)
            break


def Field(item, option):
    Print_message("\nEnter 1 to Knock on the door of the house.")
    Print_message("\nEnter 2 to peer into the cave.")
    Print_message("\nWhat would you like to do?")
    while True:
        alternative1 = input("\n(Please enter 1 or 2.)")
        if alternative1 == "1":
            House(item, option)
            break
        elif alternative1 == "2":
            Cave(item, option)
            break


def PLAY_AGAIN():
    repeat = input("Would you like to play again? (y/n)").lower()
    if repeat == "y":
        Print_message("\n\nExcellent! Restarting the game ...\n\n")
        main()
    elif repeat == "n":
        Print_message("\n\nThanks for playing! See you next time.\n\n")
    else:
        PLAY_AGAIN()


def main():
    item = []
    option = random.choice(["bannik", "pirate", "angus", "troll",
                            "medusa"])
    Introduction(item, option)
    Field(item, option)
main()
# Made By :- Isha Gupta
