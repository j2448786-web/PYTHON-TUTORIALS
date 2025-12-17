import random

print("Welcome to Rock Paper Scissors!")
choices = ["rock", "paper", "scissors"]
computer_choice = random.choice(choices)
player_choice = input("Enter your choice (rock, paper, scissors): ").lower()

print("You chose:", player_choice)
print("Computer chose:", computer_choice)

# Add the game logic to determine winner
if player_choice == computer_choice:
    print("It's a tie!")
elif (player_choice == "rock" and computer_choice == "scissors") or \
     (player_choice == "paper" and computer_choice == "rock") or \
     (player_choice == "scissors" and computer_choice == "paper"):
    print("You win! 🎉")
else:
    print("Computer wins! 💻")

import secrets

choices = ["rock", "paper", "scissors"]

def get_player_choice():
    player_choice = input("Enter your choice (rock, paper, scissors): q to quit")
    return player_choice

def get_computer_choice():
    computer_choice = secrets.choice(choices)
    return computer_choice

def decide_winner(player, computer):
    if player.lower() == computer:
        print("It's a tie!")
    elif (
        (player.lower() == 'rock' and computer == 'scissors') or
        (player.lower() == 'paper' and computer == 'rock') or
        (player.lower() == 'scissors' and computer == 'paper')
    ):
        return 'win'
    else:
        return "lose"

def main():
    print("Welcome to Rock Paper Scissors! Press q to quit")
    
    while True:
        player_choice = get_player_choice()
        
        if player_choice == "q":
            print("Thanks for playing bye 👋🏾")
            break
        
        if player_choice not in choices:
            print('Invalid choice! Please try again and choose rock, paper, or scissors')
            continue
        computer_choice = get_computer_choice()

        print("You chose:", player_choice)
        print("Computer chose:", computer_choice)
        
        result = decide_winner(player_choice, computer_choice)
        
        if result == "tie":
            print("It's a tie")
        elif result == "win":
            print("You win 🏆")
        else:
            print('You lose! 💀')

if __name__ == "__main__":
    main()
       
        