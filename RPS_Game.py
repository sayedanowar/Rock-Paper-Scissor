# Rock Paper Scissor Game

import random

while True:
    print("---------- Rock Paper Scissor ----------")
    user_input = input("User Turn :\n Rock ( R )\n Paper ( P )\n Scissor ( S )\n Input : ").upper()

    computer_turn = random.randint(1, 3)

    if computer_turn == 1:
        rps = "Rock"
    elif computer_turn == 2:
        rps = "Paper"
    elif computer_turn == 3:
        rps = "Scissor"

    if user_input == "R" or user_input == "P" or user_input == "S":
        print("Computer Turn :\n Rock\n Paper\n Scissor\n Computer : ", rps)
        if user_input == "R" and computer_turn == 1:
            print("Tie 😐")
        elif user_input == "R" and computer_turn == 2:
            print("Computer Won Better Luck Next Time 😔")
        elif user_input == "R" and computer_turn == 3:
            print("You Won 😎🎉🎊")
        elif user_input == "P" and computer_turn == 1:
            print("You Won 😎🎉🎊")
        elif user_input == "P" and computer_turn == 2:
            print("Tie 😐")
        elif user_input == "P" and computer_turn == 3:
            print("Computer Won Better Luck Next Time 😔")
        elif user_input == "S" and computer_turn == 1:
            print("Computer Won Better Luck Next Time 😔")
        elif user_input == "S" and computer_turn == 2:
            print("You Won 😎🎉🎊")
        elif user_input == "S" and computer_turn == 3:
            print("Tie 😐")
    else:
        print("Input Not Found 😣")
    
    play_again = input("Do You Want To Paly Again - ( Y / N ) : ").upper()
    if play_again != "Y":
        break

