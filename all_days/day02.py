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

# Second star: Anyway, the second column says how the round needs to end:
# X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win.
# The total score is still calculated in the same way, but now you need to figure out what shape to choose so the round
# ends as indicated.
# Following the Elf's instructions for the second column, what would your total score be if everything goes exactly
# according to your strategy guide?

BETTER_THAN = {'A': 'Z', 'B': 'X', 'C': 'Y', 'X': 'C', 'Y': 'A', 'Z': 'B'}
EQUIVALENT = {'A': 'X', 'B': 'Y', 'C': 'Z', 'X': 'A', 'Y': 'B', 'Z': 'C'}
SHAPE_SCORE = {'X': 1, 'Y': 2, 'Z': 3, 'A': 1, 'B': 2, 'C': 3}
WIN_LOSS_SCORES = {'X': 0, 'Y': 3, 'Z': 6}


def score(rps_round):
    if BETTER_THAN[rps_round[1]] == rps_round[0]:
        return 6
    elif rps_round[1] == EQUIVALENT[rps_round[0]]:
        return 3
    return 0


def calculate_score_my_way(data):
    rps_rounds = [[rps_round[0], rps_round[2]] for rps_round in data]
    scores = [SHAPE_SCORE[rps_round[1]] + score(rps_round) for rps_round in rps_rounds]
    print(scores)
    return sum(scores)


def guess_choice(opponent, result):
    if result == 'X': # lose
        return BETTER_THAN[opponent]
    elif result == 'Y': # draw
        return opponent
    elif result == 'Z': # win
        return [k for k in BETTER_THAN if BETTER_THAN[k] == opponent][0]
    else:
        Exception(f"This choice -{result}- is not recognized.")


def calculate_score_elves_way(data):
    forecasted_choices = [guess_choice(rps_round[0], rps_round[2]) for rps_round in data]
    shape_scores = [SHAPE_SCORE[rps_guess] for rps_guess in forecasted_choices]
    return sum(shape_scores) + sum([WIN_LOSS_SCORES[rps_round[2]] for rps_round in data])


def run(data_dir, star):
    with open(f'{data_dir}/input-day02.txt', 'r') as fic:
        data = [x for x in fic.read().split('\n')[:-1]]

    if star == 1:  # The final answer is: 11767
        solution = calculate_score_my_way(data)
    elif star == 2:  # The final answer is: 13886
        solution = calculate_score_elves_way(data)
    else:
        raise Exception('Star number must be either 1 or 2.')

    print(f'The solution (star {star}) is: {solution}')
    return solution
