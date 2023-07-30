import random

#rock > scissors
#scissors > paper
#paper > rock

choices = ["Rock", "Paper", "Scissors"]

def player_guess():
    selection = input("Rock, Paper, Scissors: ")

    if selection == "Rock" or selection == "ROCK" or selection == "R":
        counter = 0
    elif selection == "Paper" or selection == "PAPER" or selection == "P":
        counter = 1
    elif selection == "Scissors" or selection == "SCISSORS" or selection == "S":
        counter = 2

    return choices[counter]


def computer_guess():
    choice = random.randint(1,3)

    if choice == 1:
        print("Computer chooses Rock")
        return "Rock"
    elif choice == 2:
        print("Computer chooses Paper")
        return "Paper"
    elif choice == 3:
        print("Computer chooses Scissors")
        return "Scissors"
    

user = player_guess()
print(f"User has chosen {user}")
computer = computer_guess()

if user == "Rock" and computer == "Scissors":
    print("You win!!")
elif user == "Scissors" and computer == "Paper":
    print("You win!!")
elif user == "Paper" and computer == "Rock":
    print("You win!!")
elif computer == "Rock" and user == "Scissors":
    print("Computer wins!!")
elif computer == "Scissors" and user == "Paper":
    print("Computer wins!!")
elif computer == "Paper" and user == "Rock":
    print("Computer wins!!")
else:
    print("Its a tie!!")