import random

def main():
    player_number = None
    my_number= random.randint(1,10)

    print("Welcome to the worst guessing game ever")
    print("All you have to do is guess a number between 1 and 10 ")

    while player_number != my_number:

        player_number = input("What is your guess? ")

        if player_number.isdigit() == True:
            player_number = (int(player_number))
            if player_number < my_number:
                print("too low")
            elif player_number > my_number:
                print("too high")
        else:
            print("nice try not this time")




    print("great job")

main()
