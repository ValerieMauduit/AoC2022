# Day 17: Pyroclastic Flow

# First star:  The five types of rocks have the following peculiar shapes, where # is rock and . is empty space:
# #### | .#. | ..# | # | ##
#      | ### | ..# | # | ##
#      | .#. | ### | #
#                  | #
# The rocks fall in the order shown above: first the - shape, then the + shape, and so on. Once the end of the list is
# reached, the same order repeats: the - shape falls first, sixth, 11th, 16th, etc.
# The rocks don't spin, but they do get pushed around by jets of hot gas coming out of the walls themselves. A quick
# scan reveals the effect the jets of hot gas will have on the rocks as they fall (your puzzle input). In jet patterns,
# < means a push to the left, while > means a push to the right.
# The tall, vertical chamber is exactly seven units wide. Each rock appears so that its left edge is two units away from
# the left wall and its bottom edge is three units above the highest rock in the room (or the floor, if there isn't one).
# After a rock appears, it alternates between being pushed by a jet of hot gas one unit (in the direction indicated by
# the next symbol in the jet pattern) and then falling one unit down. If any movement would cause any part of the rock
# to move into the walls, floor, or a stopped rock, the movement instead does not occur. If a downward movement would
# have caused a falling rock to move into the floor or an already-fallen rock, the falling rock stops where it is
# (having landed on something) and a new rock immediately begins falling.
# To prove to the elephants your simulation is accurate, they want to know how tall the tower will get after 2022 rocks
# have stopped (but before the 2023rd rock begins falling).

# Second star: description

# TODO partie 2: il faut que je regarde tous les 1026 (longueur de mon jet pattern, à vérifier) l'abcisse de chacune des
#  5 premières pierres + leur forme. Dès que je retrouve le même pattern, c'est que j'ai atteint le cycle.
#  Reste à savoir:
#  - ce que j'avais avant,
#  - de combien les cycles se superposent, (ou peut-être pas, si avoir le nb de lignes ajoutées est + simple)
#  - faire tomber ce qui manque

ROCKS = [
    {'coord': [[0, 0], [0, 1], [0, 2], [0, 3]], 'l': 4, 'h': 1},
    {'coord': [[0, 1], [1, 0], [1, 1], [1, 2], [2, 1]], 'l': 3, 'h': 3},
    {'coord': [[0, 2], [1, 2], [2, 0], [2, 1], [2, 2]], 'l': 3, 'h': 3},
    {'coord': [[0, 0], [1, 0], [2, 0], [3, 0]], 'l': 1, 'h': 4},
    {'coord': [[0, 0], [0, 1], [1, 0], [1, 1]], 'l': 2, 'h': 2},
]


def rock_on_free_space(rock, position, chamber, width):
    if (position[1] + rock['l'] > width) or (position[1] < 0) or (position[0] >= len(chamber)):
        return False
    else:
        for coord in rock['coord']:
            if chamber[position[0] + coord[0]][position[1] + coord[1]] != '.':
                return False
    return True


def drop_rock(rock, already_fallen, width, jet_pattern):
    chamber = [['.' for x in range(width)] for y in range(3 + rock['h'])] + already_fallen.copy()
    rock_position = [0, 2]
    fallen = False
    while not fallen:
        jet = jet_pattern[0]
        if jet == '>':
            if rock_on_free_space(rock, [rock_position[0], rock_position[1] + 1], chamber, width):
                rock_position = [rock_position[0], rock_position[1] + 1]
        elif jet == '<':
            if rock_on_free_space(rock, [rock_position[0], rock_position[1] - 1], chamber, width):
                rock_position = [rock_position[0], rock_position[1] - 1]
        else:
            raise Exception(f"Pattern '{jet}' - not recognized in {jet_pattern[:5]}...")
        jet_pattern = jet_pattern[1:] + jet
        if rock_on_free_space(rock, [rock_position[0] + 1, rock_position[1]], chamber, width):
            rock_position = [rock_position[0] + 1, rock_position[1]]
        else:
            # put the rock in the chamber map
            fallen = True
            for coord in rock['coord']:
                chamber[rock_position[0] + coord[0]][rock_position[1] + coord[1]] = '#'
    return {
        'chamber': chamber[(next((i for i, v in enumerate([''.join(x) for x in chamber]) if v != '.......'), -1)):10000],
        'next_pattern': jet_pattern
    }


def drop_rocks(width, jet_pattern, drops=2022):
    chamber = []
    rocks_count = len(ROCKS)
    for drop in range(drops):
        if drop % 10000 == 0:
            print(drop)
        dropped = drop_rock(ROCKS[drop % rocks_count], chamber, width, jet_pattern)
        chamber = dropped['chamber']
        jet_pattern = dropped['next_pattern']
    return len(chamber)


def display_map(chamber, rock=None, rock_position=None):
    displayed = chamber.copy()
    if rock:
        for coord in rock['coord']:
            displayed[coord[0] + rock_position[0]][coord[1] + rock_position[1]] = 'R'
    for line in displayed:
        print(''.join(line))


def run(data_dir, star):
    with open(f'{data_dir}/input-day17.txt', 'r') as fic:
        data = fic.read()[:-1]

    if star == 1:  # The final answer is: 3215
        solution = drop_rocks(7, data)
    elif star == 2:  # The final answer is:
        solution = my_func(data)
    else:
        raise Exception('Star number must be either 1 or 2.')

    print(f'The solution (star {star}) is: {solution}')
    return solution
