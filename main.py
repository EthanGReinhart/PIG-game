import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll


while True:
    players = input("How many players will be playing(2-4)? ")
    if players.isnumeric():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Player count must be at least 2")
    else:
        print("Player count must be a number")

MAX_SCORE = 50
player_scores = [0 for _ in range(players)]

while max(player_scores) < MAX_SCORE:

    current_score = 0

    for player_idx in range(players):

        current_score = 0
        print(f"\nPlayer {player_idx + 1}s turn has begun\n")
        while True:
            should_roll = input("Do you want to roll? (Y/N) ")
            if should_roll.lower() != "y":
                break

            else:
                value = roll()
                if value == 1:
                    print("You rolled a ONEEEEE! Turn done")
                    current_score = 0
                    break
                else:
                    print(f"You rolled a {value}!")
                    current_score += value

                print(f"Your score is {current_score}.")
        player_scores[player_idx] += current_score
        print(f"Your total score is {player_scores[player_idx]}.")

MAX_SCORE = max(player_scores)
winning_idx = player_scores.index(MAX_SCORE)
print(f"\nPlayer {winning_idx+1} WINS! With a score of {MAX_SCORE}")
