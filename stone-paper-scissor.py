import random

# options = ("rock", "paper", "scissors")
# running = True

#introduction function
def welcome():
    print("<--Welcome to Roct, Paper, Scisors-->")

#making a function for the game logic
def gamegoing():
    options = ("rock", "paper", "scissors")
    running = True
    while running:
        player = None
        computer = random.choice(options)

        while player not in options:
            player = input("Enter a choice ---> [rock, paper, scissors] : ")

        print(f"Player: {player}")
        print(f"Computer: {computer}")
        
        #conditional statements
        if player == computer:
            print("It's a tie!")
        elif player == "rock" and computer == "scissors":
            print("Congratulations ---> You win!")
        elif player == "paper" and computer == "rock":
            print("Congratulations ---> You win!")
        elif player == "scissors" and computer == "paper":
            print("Congratulations ---> You win!")
        else:
            print("Better luck next time ---> You lose!")

        #play continuation
        if not input("Want to play again ? [y/n]: ").lower() == "y":
            running = False

#ending statement
def end():
    print("<--Thanks You-->")

welcome()
gamegoing()
end()
