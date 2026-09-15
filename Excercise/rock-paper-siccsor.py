import random

options = ("rock", "paper", "scissors")

computer = random.choice(options)
player = None

while player not in options:
    player = input("Enter your choice (rock/paper/scissors): ").lower()

    if player not in options:
        print("Invalid option. Try again.")

print(f"Computer: {computer}")
print(f"Player: {player}")

if player == computer:
    print("==== Draw ====")

elif player == "rock" and computer == "scissors":
    print("Player wins!")

elif player == "paper" and computer == "rock":
    print("Player wins!")

elif player == "scissors" and computer == "paper":
    print("Player wins!")

else:
    print("Computer wins!")