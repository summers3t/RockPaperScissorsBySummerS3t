import random

rock = "Rock"
paper = "Paper"
scissors = "Scissors"
game_counter = 0

player_move = input("Choose [r]ock, [p]aper, [s]cissors or [e]xit: ")
while player_move != "e":
    game_counter += 1

    if player_move == "r":
        player_move = rock
    elif player_move == "p":
        player_move = paper
    elif player_move == "s":
        player_move = scissors
    else:
        raise SystemExit("Invalid Input. Try again...")

    computer_random_number = random.randint(1, 3)

    computer_move = ""

    if computer_random_number == 1:
        computer_move = rock
    elif computer_random_number == 2:
        computer_move = paper
    else:
        computer_move = scissors

    print(f"The computer chose {computer_move}.")

    if player_move == rock and computer_move == scissors or \
            player_move == paper and computer_move == rock or \
            player_move == scissors and computer_move == paper:
        print("You win!")
    elif player_move == computer_move:
        print("Draw!")
    else:
        print("You lose!")
    player_move = input("Choose [r]ock, [p]aper, [s]cissors or [e]xit: ")
else:
    print("Thank you for playing!")
    raise SystemExit(f"Total games played: {game_counter}")