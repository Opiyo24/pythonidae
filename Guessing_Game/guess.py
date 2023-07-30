import random

def guess(x):
    random_number = random.randint(1, x)

    guess = 0 #Initialize number to 0 to get us into the loop
    while guess != random_number: #Loop till the guessed number is equal to the random number
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print("Sorry, too low. Guess again")
        elif guess > random_number:
            print("Sorry, too high. Guess again")

    print(f"Yaay! Congratulations, you have guessed correctly.")

def computer_guess(x):
    computer_guess = 0
    number2 = int(input("Give a number between 1 and 10: "))

    high = x
    low = 1

    while computer_guess != number2 and low != high:#randint would gove an error

        computer_guess = random.randint(low,high)
        if computer_guess < number2:
            print("The computer guessed too low. It'll try again.")
            low = computer_guess + 1
        elif computer_guess > number2:
            print("The computer guessed too high, It'll try again.")
            high = computer_guess - 1
        
    print("The computer guessed right!!")
guess(10)
computer_guess(10)