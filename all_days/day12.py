# Day 12: Hill Climbing Algorithm

# First star: You ask your device for a heightmap of the surrounding area (your puzzle input). The heightmap shows the
# local area from above broken into a grid; the elevation of each square of the grid is given by a single lowercase
# letter, where a is the lowest elevation, b is the next-lowest, and so on up to the highest elevation, z.
# Also included on the heightmap are marks for your current position (S) and the location that should get the best
# signal (E). Your current position (S) has elevation a, and the location that should get the best signal (E) has
# elevation z.
# You'd like to reach E, but to save energy, you should do it in as few steps as possible. During each step, you can
# move exactly one square up, down, left, or right. To avoid needing to get out your climbing gear, the elevation of the
# destination square can be at most one higher than the elevation of your current square. This also means that the
# elevation of the destination square can be much lower than the elevation of your current square.
# What is the fewest steps required to move from your current position to the location that should get the best signal?

# Second star: To maximize exercise while hiking, the trail should start as low as possible: elevation a. The goal is
# still the square marked E. However, the trail should still be direct, taking the fewest steps to reach its goal. So,
# you'll need to find the shortest path from any square at elevation a to the square marked E.
# What is the fewest steps required to move starting from any square with elevation a to the location that should get
# the best signal?

def get_key_coords(value, input_map):
    key_points = []
    for line in range(len(input_map)):
        position = input_map[line].find(value)
        if position >= 0:
            key_points += [[line, position]]
    return key_points


def distances_map(initial_map, key_point):
    max_path = len(initial_map) * len(initial_map[0])
    changes = 1
    nb_rows, nb_cols = len(initial_map), len(initial_map[0])
    # add a boundary to the maps to avoid limit effects
    initial_map = (
            [[100 for x in range(len(initial_map[0]) + 2)]] +
            [[100] + row + [100] for row in initial_map] +
            [[100 for x in range(len(initial_map[0]) + 2)]]
    )
    final_map = [[max_path for x in row] for row in initial_map]
    final_map[key_point[0] + 1][key_point[1] + 1] = 0
    while changes > 0:
        changes = 0
        for row in range(nb_rows):
            for col in range(nb_cols):
                if final_map[row][col + 1] > final_map[row + 1][col + 1] + 1:
                    if initial_map[row][col + 1] >= initial_map[row + 1][col + 1] - 1:
                        final_map[row][col + 1] = final_map[row + 1][col + 1] + 1
                        changes += 1
                if final_map[row + 2][col + 1] > final_map[row + 1][col + 1] + 1:
                    if initial_map[row + 2][col + 1] >= initial_map[row + 1][col + 1] - 1:
                        final_map[row + 2][col + 1] = final_map[row + 1][col + 1] + 1
                        changes += 1
                if final_map[row + 1][col] > final_map[row + 1][col + 1] + 1:
                    if initial_map[row + 1][col] >= initial_map[row + 1][col + 1] - 1:
                        final_map[row + 1][col] = final_map[row + 1][col + 1] + 1
                        changes += 1
                if final_map[row + 1][col + 2] > final_map[row + 1][col + 1] + 1:
                    if initial_map[row + 1][col + 2] >= initial_map[row + 1][col + 1] - 1:
                        final_map[row + 1][col + 2] = final_map[row + 1][col + 1] + 1
                        changes += 1
    return final_map


def get_path(data, values):
    height_map = [[ord(x)-96 for x in line] for line in data]
    end = get_key_coords('E', data)[0]
    height_map[end[0]][end[1]] = 26
    start = []
    for value in values:
        local_coord = get_key_coords(value, data)
        start += local_coord
        if value == 'S':
            height_map[local_coord[0][0]][local_coord[0][1]] = 1
    distances = distances_map(height_map, end)
    return min([distances[point[0] + 1][point[1] + 1] for point in start])


def run(data_dir, star):
    with open(f'{data_dir}/input-day12.txt', 'r') as fic:
        data = [x for x in fic.read().split('\n')[:-1]]

    if star == 1:  # The final answer is: 394
        solution = get_path(data, ['S'])
    elif star == 2:  # The final answer is: 388
        solution = get_path(data, ['S', 'a'])
    else:
        raise Exception('Star number must be either 1 or 2.')

    print(f'The solution (star {star}) is: {solution}')
    return solution
