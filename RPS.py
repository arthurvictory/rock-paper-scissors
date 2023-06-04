import random

options = ("rock", "paper", "scissors")
running = True

while running:
    player = input("Enter a choice (rock, paper, scissors) or 'I quit' to exit: ")

    if player.lower() == "i quit":
        running = False
        break

    player = player.lower()
    computer = random.choice(options)

    if player not in options:
        print("Invalid choice. Please try again.")
        continue

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "scissors":
        print("You win!")
    elif player == "paper" and computer == "rock":
        print("You win!")
    elif player == "scissors" and computer == "paper":
        print("You win!")
    else:
        print("You lose!")

print("Thanks for playing!")
