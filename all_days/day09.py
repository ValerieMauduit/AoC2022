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

# Second star: Rather than two knots, you now must simulate a rope consisting of ten knots. One knot is still the head
# of the rope and moves according to the series of motions. Each knot further down the rope follows the knot in front of
# it using the same rules as before. Now, you need to keep track of the positions the new tail visits. Simulate your
# complete series of motions on a larger rope with ten knots. How many positions does the tail of the rope visit at
# least once?


def follow_previous(previous_node):
    follower_positions = [(0, 0)]
    for leader in previous_node:
        follower = follower_positions[-1]
        if follower[0] - leader[0] > 1:
            follower_positions += [(leader[0] + 1, max([min([leader[1], follower[1] + 1]), follower[1] - 1]))]
        elif follower[0] - leader[0] < -1:
            follower_positions += [(leader[0] - 1, max([min([leader[1], follower[1] + 1]), follower[1] - 1]))]
        elif follower[1] - leader[1] > 1:
            follower_positions += [(max([min([leader[0], follower[0] + 1]), follower[0] - 1]), leader[1] + 1)]
        elif follower[1] - leader[1] < -1:
            follower_positions += [(max([min([leader[0], follower[0] + 1]), follower[0] - 1]), leader[1] - 1)]
    return follower_positions


def move_head(commands):
    positions = [(0, 0)]
    for command in commands:
        n_moves = int(command[1])
        previous_position = positions[-1]
        if command[0] == 'R':
            positions += [(previous_position[0], previous_position[1] + n + 1) for n in range(n_moves)]
        elif command[0] == 'L':
            positions += [(previous_position[0], previous_position[1] - n - 1) for n in range(n_moves)]
        elif command[0] == 'U':
            positions += [(previous_position[0] + n + 1, previous_position[1]) for n in range(n_moves)]
        elif command[0] == 'D':
            positions += [(previous_position[0] - n - 1, previous_position[1]) for n in range(n_moves)]
        else:
            Exception(f'This command ({command}) is not permitted')
    return positions


def count_tail_positions(data, rope_length):
    commands = [x.split(' ') for x in data]
    head_positions = move_head(commands)
    node_positions = head_positions
    for node in range(rope_length - 1):
        node_positions = follow_previous(node_positions)
    return len(set(node_positions))


def run(data_dir, star):
    with open(f'{data_dir}/input-day09.txt', 'r') as fic:
        data = [x for x in fic.read().split('\n')[:-1]]
    if star == 1:  # The final answer is: 6470
        solution = count_tail_positions(data, 2)
    elif star == 2:  # The final answer is: 2658
        solution = count_tail_positions(data, 10)
    else:
        raise Exception('Star number must be either 1 or 2.')

    print(f'The solution (star {star}) is: {solution}')
    return solution
