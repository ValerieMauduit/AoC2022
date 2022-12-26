# Day 24: Blizzard Basin

# First star: As the expedition reaches a valley that must be traversed to reach the extraction site, you find that
# strong, turbulent winds are pushing small blizzards of snow and sharp ice around the valley. To make it across safely,
# you'll need to find a way to avoid them. Fortunately, it's easy to see all of this from the entrance to the valley, so
# you make a map of the valley and the blizzards (your puzzle input). The walls of the valley are drawn as #; everything
# else is ground. Clear ground - where there is currently no blizzard - is drawn as .. Otherwise, blizzards are drawn
# with an arrow indicating their direction of motion: up (^), down (v), left (<), or right (>). Due to conservation of
# blizzard energy, as a blizzard reaches the wall of the valley, a new blizzard forms on the opposite side of the valley
# moving in the same direction. Your expedition begins in the only non-wall position in the top row and needs to reach
# the only non-wall position in the bottom row. On each minute, you can move up, down, left, or right, or you can wait
# in place. You and the blizzards act simultaneously, and you cannot share a position with a blizzard.
# What is the fewest number of minutes required to avoid the blizzards and reach the goal?

# Second star: description

def get_blizzard_rules(blizzard_map, width, height):
    rules = {'>': [], '<': [], '^': [], 'v': []}
    for line in range(height):
        for col in range(width):
            if blizzard_map[line][col] != '.':
                rules[blizzard_map[line][col]] += [[line, col]]
    return rules


def build_blizzard_map(rules, width, height, time):
    actual_map = [['.' for col in range(width)] for line in range(height)]
    for blizzard in [[position[0], (position[1] + time % width) % width] for position in rules['>']]:
        actual_map[blizzard[0]][blizzard[1]] = '>'
    for blizzard in [[position[0], (width + position[1] - time % width) % width] for position in rules['<']]:
        actual_map[blizzard[0]][blizzard[1]] = '<'
    for blizzard in [[(position[0] + time % height) % height, position[1]] for position in rules['v']]:
        actual_map[blizzard[0]][blizzard[1]] = 'v'
    for blizzard in [[(height + position[0] - time % height) % height, position[1]] for position in rules['^']]:
        actual_map[blizzard[0]][blizzard[1]] = '^'
    return actual_map


def one_more_step(map_step_before, blizzard_map, width, height):
    new_map = [[0 for x in range(width)] for y in range(height)]
    for y in range(height):
        for x in range(width):
            if map_step_before[y][x] == 1:
                for xn in range(max(0, x - 1), min(width - 1, x + 1) + 1):
                    if blizzard_map[y][xn] == '.':
                        new_map[y][xn] = 1
                for yn in range(max(0, y - 1), min(height - 1, y + 1) + 1):
                    if blizzard_map[yn][x] == '.':
                        new_map[yn][x] = 1
    if blizzard_map[0][0] == '.':
        new_map[0][0] = 1
    return new_map


def reach_exit_time(data):
    blizzard_map0 = [line[1:-1] for line in data[1:-1]]
    width = len(blizzard_map0[0])
    height = len(blizzard_map0)
    blizzard_rules = get_blizzard_rules(blizzard_map0, width, height)
    time = 0
    travel_map = [[0 for x in line] for line in blizzard_map0]
    while travel_map[-1][-1] == 0:
        time += 1
        travel_map = one_more_step(travel_map, build_blizzard_map(blizzard_rules, width, height, time), width, height)
    return time + 1


def run(data_dir, star):
    with open(f'{data_dir}/input-day24.txt', 'r') as fic:
        data = [x for x in fic.read().split('\n')[:-1]]

    if star == 1:  # The final answer is: 230
        solution = reach_exit_time(data)
    elif star == 2:  # The final answer is:
        solution = my_func(data)
    else:
        raise Exception('Star number must be either 1 or 2.')

    print(f'The solution (star {star}) is: {solution}')
    return solution
