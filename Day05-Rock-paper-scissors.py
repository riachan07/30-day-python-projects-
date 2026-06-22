import random

print("This is a Rock Paper Scissors game")

choices = ["rock", "paper", "scissors"]
player_score=0
comp_score=0

while True:

    computer = random.choice(choices)

    choice = input("Enter rock, paper or scissors: ")

    print(f"You chose {choice}")
    print(f"Computer chose {computer}")

    if computer == choice:
        print("It's a tie")

    elif choice == "rock" and computer == "scissors":
        print("The user won")
        player_score+=1

    elif choice == "rock" and computer == "paper":
        print("Computer won")
        comp_score+=1

    elif choice == "paper" and computer == "rock":
        print("User won")
        player_score+=1

    elif choice == "paper" and computer == "scissors":
        print("Computer won")
        comp_score+=1


    elif choice == "scissors" and computer == "paper":
        print("User won")
        player_score+=1

    elif choice == "scissors" and computer == "rock":
        print("Computer won")
        comp_score+=1


    else:
        print("Invalid choice")

    print(f"computer score is {comp_score}")
    print(f"player score is {player_score}")




    play=input("play again yes or no ")
    if play== "no":
         print("okie")
         break 
