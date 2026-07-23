from random import choice

choices = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0
ties = 0

while True:
    print("-" * 30)
    print(" ROCK - PAPER - SCISSORS")
    print("-" * 30)

    user = input("Select rock, paper or scissors: ").lower()
    if user not in choices:
        print("Invalid choice! Enter rock, paper, or scissors.")
        continue

    computer = choice(choices)

    print(f"You chose: {user}")
    print(f"Computer chose: {computer}")

    if user == computer:
        print("It's a tie!")
        ties += 1

    elif user == "rock" and computer == "scissors":
        print("You won!")
        user_score += 1

    elif user == "rock" and computer == "paper":
        print("You lost!")
        computer_score += 1

    elif user == "paper" and computer == "rock":
        print("You won!")
        user_score += 1

    elif user == "paper" and computer == "scissors":
        print("You lost!")
        computer_score += 1

    elif user == "scissors" and computer == "paper":
        print("You won!")
        user_score += 1

    elif user == "scissors" and computer == "rock":
        print("You lost!")
        computer_score += 1
    print("-" * 30)
    print(" SCORE")
    print("-" * 30)
    print(f"You : {user_score}")
    print(f"Computer : {computer_score}")
    print(f"Ties : {ties}")

    play_again = input("\nPlay again? (y/n): ").lower()

    if play_again != "y":
        print("-" * 30)
        print(" FINAL SCORE")
        print("-" * 30)
        print(f"You : {user_score}")
        print(f"Computer : {computer_score}")
        print(f"Ties : {ties}")
        print("Thanks for playing!")
        break
