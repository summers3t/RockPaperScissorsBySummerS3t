import random

rock = "Rock"
paper = "Paper"
scissors = "Scissors"
game_counter = 0
wins = 0
loses = 0
draws = 0

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
        print("Invalid move. Please try again...")
        player_move = input("Choose [r]ock, [p]aper, [s]cissors or [e]xit: ")
        continue

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
        wins += 1
        print("You win!")
    elif player_move == computer_move:
        draws += 1
        print("Draw!")
    else:
        loses += 1
        print("You lose!")
    player_move = input("Choose [r]ock, [p]aper, [s]cissors or [e]xit: ")
else:
    print("Thank you for playing!")
    print(f"Total wins: {wins}")
    print(f"Total loses: {loses}")
    print(f"Total draws: {draws}")

    raise SystemExit(f"Total games played: {game_counter}")