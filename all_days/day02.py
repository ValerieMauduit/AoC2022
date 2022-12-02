# Day2: Rock Paper Scissors

# First star: The first column is what your opponent is going to play: A for Rock, B for Paper, and C for Scissors.
# The second column, you reason, must be what you should play in response: X for Rock, Y for Paper, and Z for Scissors.
# The winner of the whole tournament is the player with the highest score. Your total score is the sum of your scores
# for each round. The score for a single round is the score for the shape you selected
# (1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome of the round
# (0 if you lost, 3 if the round was a draw, and 6 if you won).
# Since you can't be sure if the Elf is trying to help you or trick you, you should calculate the score you would get if
# you were to follow the strategy guide.
# What would your total score be if everything goes exactly according to your strategy guide?

# Second star: description

def explicit_round(rps_round):
    translation = {'A': 'rock', 'B': 'paper', 'C': 'scissors', 'X': 'rock', 'Y': 'paper', 'Z': 'scissors'}
    return [translation[rps_round[0]], translation[rps_round[2]]]


def score(rps_round):
    better_than = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}
    if better_than[rps_round[1]] == rps_round[0]:
        return 6
    elif rps_round[1] == rps_round[0]:
        return 3
    return 0


def calculate_score(data):
    intelligible_rounds = [explicit_round(rps_round) for rps_round in data]
    shape_score = {'rock': 1, 'paper': 2, 'scissors': 3}
    scores = [shape_score[rps_round[1]] + score(rps_round) for rps_round in intelligible_rounds]
    return sum(scores)


def run(data_dir, star):
    with open(f'{data_dir}/input-day02.txt', 'r') as fic:
        data = [x for x in fic.read().split('\n')[:-1]]

    if star == 1:  # The final answer is: 11767
        solution = calculate_score(data)
    elif star == 2:  # The final answer is:
        solution = my_func() + my_func()
    else:
        raise Exception('Star number must be either 1 or 2.')

    print(f'The solution (star {star}) is: {solution}')
    return solution
