import random


def menu():
    while True:
        print()
        print("would you like to...")
        print()
        print("1. play")
        print("2. quit")

        menu_option = input(">")

        if menu_option.isdigit() == True:
            if int(menu_option) > 2 or int(menu_option) < 1:
                print("option is not availible")
                continue

            elif int(menu_option) == 1:
                return 0
            elif int(menu_option) == 2:
                exit()
        else:
            print("input must be a number")
            continue


def main():

    print()
    print("Welcome to the worst guessing game ever")
    print()
    print("All you have to do is guess a number between 1 and 100 ")

    while True:

        menu()
        player_number = None
        my_number= random.randint(1,100)
        guess_count = 0
        has_lied = False
        lied_num = None


        while player_number != my_number:

            player_number = input("What is your guess? ")
            guess_count += 1
            if player_number.isdigit() == True:
                player_number = (int(player_number))
                if has_lied == False and random.random() <= .2:
                    if player_number > my_number:
                            print("too low")
                    elif player_number < my_number:
                            print("too high")
                    has_lied = True
                    lied_num = player_number

                elif player_number < my_number:
                        print("too low")
                elif player_number > my_number:
                        print("too high")
            else:
                print("nice try not this time")

        print("great job it only took you {} tries".format(guess_count))
        if lied_num != None:
            print("I lied on number {}".format(lied_num))

main()
