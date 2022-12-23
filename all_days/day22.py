# Day 22: Monkey Map

# First star: To pass through the force field, you have to enter a password; doing so involves tracing a specific path
# on a strangely-shaped board.At least, you're pretty sure that's what you have to do; the elephants aren't exactly
# fluent in monkey.
# The monkeys give you notes that they took when they last saw the password entered (your puzzle input).
# The first half of the monkeys' notes is a map of the board. It is comprised of a set of open tiles (on which you can
# move, drawn .) and solid walls (tiles which you cannot enter, drawn #).
# The second half is a description of the path you must follow. It consists of alternating numbers and letters.
# - A number indicates the number of tiles to move in the direction you are facing. If you run into a wall, you stop
#   moving forward and continue with the next instruction.
# - A letter indicates whether to turn 90 degrees clockwise (R) or counterclockwise (L). Turning happens in-place; it
#   does not change your current tile.
# You begin the path in the leftmost open tile of the top row of tiles. Initially, you are facing to the right (from
# the perspective of how the map is drawn).
# If a movement instruction would take you off of the map, you wrap around to the other side of the board. In other
# words, if your next tile is off of the board, you should instead look in the direction opposite of your current facing
# as far as you can until you find the opposite edge of the board, then reappear there.
# To finish providing the password to this strange input device, you need to determine numbers for your final row,
# column, and facing as your final position appears from the perspective of the original map. Rows start from 1 at the
# top and count downward; columns start from 1 at the left and count rightward. (In the above example, row 1, column 1
# refers to the empty space with no tile on it in the top-left corner.) Facing is 0 for right (>), 1 for down (v), 2 for
# left (<), and 3 for up (^). The final password is the sum of 1000 times the row, 4 times the column, and the facing.
# Follow the path given in the monkeys' notes. What is the final password?

# Second star: description

# TODO: regarder les print du cas réel et faire plein de tests avec une ligne à chaque fois pour comprendre ce qui a
#  l'air de se passer.

import re

TURN_COUNT = {'R': 0, 'D': 1, 'L': 2, 'U': 3}
TURN = {'R': {'R': 'D', 'D': 'L', 'L': 'U', 'U': 'R'}, 'L': {'R': 'U', 'D': 'R', 'L': 'D', 'U': 'L'}}
MARKERS = {'R': '>', 'D': 'v', 'L': '<', 'U': '^'}


def move_n_steps(position, distance, map_line, reverse=False):
    map_width = len([x for x in map_line if x != ' '])
    sign = 1
    if '#' in map_line:
        print('  wall in line')
        reordered_line = [x for x in (map_line[position:] + map_line[:position]) if x != ' ']
        if reverse:
            reordered_line.reverse()
            if position == 0:
                reordered_line = [reordered_line[-1]] + reordered_line[:-1]
            sign = -1
        print(f"  distance: {distance} vs 1er mur: {reordered_line.index('#') - 1}")
        displacement = min([distance, reordered_line.index('#') - 1])
    else:
        print('  free line')
        displacement = distance
        if reverse:
            sign = -1
    blanks = re.search('\.|#', ''.join(map_line)).span()[0]
    print(f" map_width: {map_width}")
    print(f" displacement: {displacement}") # TODO: faux 0, je devrais avoir 1
    print(f" sign: {sign}")
    print(f" position: {position}")
    print(f" blanks: {blanks}") # TODO: faux 0, je devrais avoir 50
    print(f" (map_width + displacement * sign + position - blanks): {(map_width + displacement * sign + position - blanks)}")
    print(f" (map_width + displacement * sign + position - blanks) % map_width: {(map_width + displacement * sign + position - blanks) % map_width}")

    return (map_width + displacement * sign + position - blanks) % map_width + blanks


def go_ahead(position, distance, my_map):
    orientation  = position[2]
    if orientation == 'R':
        position[0] = move_n_steps(position[0], distance, my_map[position[1]])
    elif orientation == 'L':
        position[0] = move_n_steps(position[0], distance, my_map[position[1]], True)
    elif orientation == 'D':
        position[1] = move_n_steps(position[1], distance, [line[position[0]] for line in my_map])
    elif orientation == 'U':
        position[1] = move_n_steps(position[1], distance, [line[position[0]] for line in my_map], True)
    else:
        raise Exception(f'WTF is this orientation??? ({orientation})')
    return position


def travel_in_map(my_map, instructions):
    position = [my_map[0].index('.'), 0, 'R']
    for n in range(len(instructions['turns'])):
        print(f'round {n}:')
        print(f"go ahead {position}, {instructions['distances'][n]}:")
        position = go_ahead(position, instructions['distances'][n], my_map)
        print(f"turn {TURN[instructions['turns'][n]][position[2]]}")
        position = [position[0], position[1], TURN[instructions['turns'][n]][position[2]]]
        input('...')
    print('last step')
    print(f"go ahead {position}, {instructions['distances'][-1]}:")
    position = go_ahead(position, instructions['distances'][-1], my_map)
    return position


def get_password(data):
    max_width = max([len(line) for line in data[0]])
    my_map = [[x for x in line] + [' ' for x in range(max_width - len(line) + 1)] for line in data[0]]
    last_position = travel_in_map(
        my_map,
        {'distances': [int(x) for x in re.split('R|L', data[1])], 'turns': re.split('[0-9]+', data[1])[1:-1]}
    )
    last_position = [last_position[1] + 1, last_position[0] + 1, last_position[2]]
    return [last_position, 1000 * last_position[0] + 4 * last_position[1] + TURN_COUNT[last_position[2]]]


def run(data_dir, star):
    with open(f'{data_dir}/input-day22.txt', 'r') as fic:
        data = [x for x in fic.read().split('\n')[:-1]]
        data = [data[:data.index('')], data[-1]]

    if star == 1:  # The final answer is: # TODO: 189192, too high - 18512 too low
        solution = get_password(data)
    elif star == 2:  # The final answer is:
        solution = my_func(data)
    else:
        raise Exception('Star number must be either 1 or 2.')

    print(f'The solution (star {star}) is: {solution}')
    return solution
