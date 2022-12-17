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

def rock_paths(data):
    rock_map = []
    for path in data:
        corners = [[int(y[0]), int(y[1])] for y in [x.split(',') for x in path.split(' -> ')]]
        for n in range(1, len(corners)):
            xmin = min([corners[n - 1][0], corners[n][0]])
            xmax = max([corners[n - 1][0], corners[n][0]])
            ymin = min([corners[n - 1][1], corners[n][1]])
            ymax = max([corners[n - 1][1], corners[n][1]])
            # I duplicate thne corners. Is it a problem?
            rock_map += [[x, y] for x in range(xmin, xmax + 1) for y in range(ymin, ymax + 1)]
    return rock_map


def drop_grain(blocked_map, deepest_value, origin):
    if origin[1] < deepest_value:
        if [origin[0], origin[1] + 1] in blocked_map:
            if [origin[0] - 1, origin[1] + 1] in blocked_map:
                if [origin[0] + 1, origin[1] + 1] in blocked_map:
                    return origin
                else:
                    return drop_grain(blocked_map, deepest_value, [origin[0] + 1, origin[1] + 1])
            else:
                return drop_grain(blocked_map, deepest_value, [origin[0] - 1, origin[1] + 1])
        else:
            return drop_grain(blocked_map, deepest_value, [origin[0], origin[1] + 1])
    else:
        return origin


def sand_pile_size_lower_limit(data):
    rock_map = rock_paths(data)
    sand_origin = [500, 0]
    sand_grain = sand_origin
    sand_pile = []
    lowest_rock = max([rock[1] for rock in rock_map])
    while sand_grain[1] <= lowest_rock:
        sand_grain = drop_grain(rock_map + sand_pile, lowest_rock + 1, sand_origin)
        sand_pile += [sand_grain]
    return len(sand_pile) - 1


def sand_pile_size_upper_limit(data):
    rock_map = rock_paths(data)
    sand_origin = [500, 0]
    sand_grain = [500, 1]
    sand_pile = []
    lowest_rock = max([rock[1] for rock in rock_map])
    while sand_grain[1] >= 1:
        sand_grain = drop_grain(rock_map + sand_pile, lowest_rock + 1, sand_origin)
        sand_pile += [sand_grain]
    return len(sand_pile)


def run(data_dir, star):
    with open(f'{data_dir}/input-day14.txt', 'r') as fic:
        data = [x for x in fic.read().split('\n')[:-1]]

    if star == 1:  # The final answer is: 979
        solution = sand_pile_size_lower_limit(data)
    elif star == 2:  # The final answer is: 29382 is too high - même 29363 est trop haut
        solution = sand_pile_size_upper_limit(data)
    else:
        raise Exception('Star number must be either 1 or 2.')

    print(f'The solution (star {star}) is: {solution}')
    return solution
