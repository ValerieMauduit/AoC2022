# Day 14: Regolith Reservoir

# First star: Your scan traces the path of each solid rock structure and reports the x,y coordinates that form the shape
# of the path, where x represents distance to the right and y represents distance down. Each path appears as a single
# line of text in your scan. After the first point of each path, each point indicates the end of a straight horizontal
# or vertical line to be drawn from the previous point.
# The sand is pouring into the cave from point 500,0.
# Sand is produced one unit at a time, and the next unit of sand is not produced until the previous unit of sand comes
# to rest. A unit of sand is large enough to fill one tile of air in your scan. A unit of sand always falls down one
# step if possible. If the tile immediately below is blocked (by rock or sand), the unit of sand attempts to instead
# move diagonally one step down and to the left. If that tile is blocked, the unit of sand attempts to instead move
# diagonally one step down and to the right. Sand keeps moving as long as it is able to do so, at each step trying to
# move down, then down-left, then down-right. If all three possible destinations are blocked, the unit of sand comes to
# rest and no longer moves, at which point the next unit of sand is created back at the source.
# Using your scan, simulate the falling sand. How many units of sand come to rest before sand starts flowing into the
# abyss below?

# Second star: You realize you misread the scan. There isn't an endless void at the bottom of the scan - there's floor,
# and you're standing on it! You don't have time to scan the floor, so assume the floor is an infinite horizontal line
# with a y coordinate equal to two plus the highest y coordinate of any point in your scan. Using your scan, simulate
# the falling sand until the source of the sand becomes blocked. How many units of sand come to rest?

def build_rock_map(data, border=10):
    paths = [[[int(y[0]), int(y[1])] for y in [x.split(',') for x in path.split(' -> ')]] for path in data]
    x_origin = min([item[0] for sublist in paths for item in sublist]) - 1
    lowest_rock = max([item[1] for sublist in paths for item in sublist])
    rock_map = [
        ['.' for x in range(x_origin, max([item[0] for sublist in paths for item in sublist]) + 2 * border)]
        for y in range(lowest_rock + 2)
    ]
    rocks = []
    for path in paths:
        for n in range(1, len(path)):
            x_min = min([path[n - 1][0], path[n][0]])
            x_max = max([path[n - 1][0], path[n][0]])
            y_min = min([path[n - 1][1], path[n][1]])
            y_max = max([path[n - 1][1], path[n][1]])
            rocks += [[x, y] for x in range(x_min, x_max + 1) for y in range(y_min, y_max + 1)]
    for rock in rocks:
        rock_map[rock[1]][rock[0] - x_origin + border] = '#'
    return {'map': rock_map, 'x_origin': x_origin, 'lowest_rock': lowest_rock}


def drop_grain(blocked_map, deepest_value, origin):
    if origin[1] < deepest_value:
        if blocked_map[origin[1] + 1][origin[0]] != '.':
            if origin[0] > 0:
                if blocked_map[origin[1] + 1][origin[0] - 1] != '.':
                    if origin[0] < len(blocked_map[0]) - 1:
                        if blocked_map[origin[1] + 1][origin[0] + 1] != '.':
                            return origin
                        else:
                            return drop_grain(blocked_map, deepest_value, [origin[0] + 1, origin[1] + 1])
                    else:
                        return origin
                else:
                    return drop_grain(blocked_map, deepest_value, [origin[0] - 1, origin[1] + 1])
            else:
                return origin
        else:
            return drop_grain(blocked_map, deepest_value, [origin[0], origin[1] + 1])
    else:
        return origin


def sand_pile_size(data):
    border = 10
    rock_map_data = build_rock_map(data, border)
    rock_map = rock_map_data['map']
    x_min = rock_map_data['x_origin']
    sand_origin = [500 - x_min + border, 0]
    sand_grain = sand_origin
    lowest_rock = rock_map_data['lowest_rock']
    sand_pile = 0
    while sand_grain[1] < lowest_rock:
        sand_grain = drop_grain(rock_map, lowest_rock, sand_origin)
        rock_map[sand_grain[1]][sand_grain[0]] = 'S'
        sand_pile += 1
    return sand_pile - 1


def sand_pile_to_the_ground(data):
    border = 5
    rock_map_data = build_rock_map(data, border)
    rock_map = rock_map_data['map']
    x_min = rock_map_data['x_origin']
    sand_origin = [500 - x_min + border, 0]
    sand_grain = [42, 42]
    lowest_rock = rock_map_data['lowest_rock']
    sand_pile = 0
    while sand_grain != sand_origin:
        sand_grain = drop_grain(rock_map, lowest_rock + 1, sand_origin)
        rock_map[sand_grain[1]][sand_grain[0]] = 'S'
        sand_pile += 1
    # right triangle
    right_side = [x[-1] for x in rock_map]
    if 'S' in right_side:
        height = lowest_rock + 1 - right_side.index('S')
    else:
        height = 0
    right_triangle = height * (height + 1) / 2
    # left triangle
    left_side = [x[0] for x in rock_map]
    if 'S' in left_side:
        height = lowest_rock + 1 - left_side.index('S')
    else:
        height = 0
    left_triangle = height * (height + 1) / 2
    return sand_pile + right_triangle + left_triangle


def run(data_dir, star):
    with open(f'{data_dir}/input-day14.txt', 'r') as fic:
        data = [x for x in fic.read().split('\n')[:-1]]

    if star == 1:  # The final answer is: 979
        solution = sand_pile_size(data)
    elif star == 2:  # The final answer is: 29044
        solution = sand_pile_to_the_ground(data)
    else:
        raise Exception('Star number must be either 1 or 2.')

    print(f'The solution (star {star}) is: {solution}')
    return solution