# Day 9: Rope Bridge

# First star: Consider a rope with a knot at each end; these knots mark the head and the tail of the rope. If the head
# moves far enough away from the tail, the tail is pulled toward the head. Due to nebulous reasoning involving Planck
# lengths, you should be able to model the positions of the knots on a two-dimensional grid. Then, by following a
# hypothetical series of motions (your puzzle input) for the head, you can determine how the tail will move. Due to the
# aforementioned Planck lengths, the rope must be quite short; in fact, the head (H) and tail (T) must always be
# touching (diagonally adjacent and even overlapping both count as touching).
# If the head is ever two steps directly up, down, left, or right from the tail, the tail must also move one step in
# that direction so it remains close enough. Otherwise, if the head and tail aren't touching and aren't in the same row
# or column, the tail always moves one step diagonally to keep up. Simulate your complete hypothetical series of
# motions. How many positions does the tail of the rope visit at least once?

# Second star: description

def move(previous_position, command):
    n_moves = int(command[1])
    if command[0] == 'R':
        heads = [(previous_position['head'][0], previous_position['head'][1] + n + 1) for n in range(n_moves)]
    elif command[0] == 'L':
        heads = [(previous_position['head'][0], previous_position['head'][1] - n - 1) for n in range(n_moves)]
    elif command[0] == 'U':
        heads = [(previous_position['head'][0] + n + 1, previous_position['head'][1]) for n in range(n_moves)]
    elif command[0] == 'D':
        heads = [(previous_position['head'][0] - n - 1, previous_position['head'][1]) for n in range(n_moves)]
    else:
        Exception(f'This command ({command}) is not permitted')
    tails = [previous_position['tail']]
    for n in range(n_moves):
        if tails[-1][0] - heads[n][0] > 1:
            tails += [(heads[n][0] + 1, heads[n][1])]
        elif tails[-1][0] - heads[n][0] < -1:
            tails += [(heads[n][0] - 1, heads[n][1])]
        elif tails[-1][1] - heads[n][1] > 1:
            tails += [(heads[n][0], heads[n][1] + 1)]
        elif tails[-1][1] - heads[n][1] < -1:
            tails += [(heads[n][0], heads[n][1] - 1)]
    return {'head': heads, 'tail': tails[1:]}


def count_tail_positions(data):
    commands = [x.split(' ') for x in data]
    rope_positions = {'head': [(0, 0)], 'tail': [(0, 0)]}
    for command in commands:
        new_positions = move({ k: rope_positions[k][-1] for k in rope_positions}, command)
        rope_positions = {k: rope_positions[k] + new_positions[k] for k in rope_positions}
    return len(set(rope_positions['tail']))


def run(data_dir, star):
    with open(f'{data_dir}/input-day09.txt', 'r') as fic:
        data = [x for x in fic.read().split('\n')[:-1]]

    if star == 1:  # The final answer is: 6470
        solution = count_tail_positions(data)
    elif star == 2:  # The final answer is:
        solution = my_func(data)
    else:
        raise Exception('Star number must be either 1 or 2.')

    print(f'The solution (star {star}) is: {solution}')
    return solution
