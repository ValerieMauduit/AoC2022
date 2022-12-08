# Day 8: Treetop Tree House

# First star: First, determine whether there is enough tree cover here to keep a tree house hidden. To do this, you need
# to count the number of trees that are visible from outside the grid when looking directly along a row or column.
# Each tree is represented as a single digit whose value is its height, where 0 is the shortest and 9 is the tallest.
# Consider your map; how many trees are visible from outside the grid?

# Second star: description

import numpy as np


def count_visible_trees(data):
    tree_map = [[int(x) for x in [*line]] for line in data]
    visible_map = [[0 for tree in raw] for raw in tree_map]
    # horizontal search
    for row in range(1, len(tree_map) - 1):
        for tree in range(1, len(tree_map[row]) - 1):
            if tree_map[row][tree] > min(max(tree_map[row][:tree]), max(tree_map[row][(tree + 1):])):
                visible_map[row][tree] = 1
    # vertical search
    transposed_tree_map = np.array(tree_map).T.tolist()
    transposed_visible_map = np.array(visible_map).T.tolist()
    for row in range(1, len(transposed_tree_map) - 1):
        for tree in range(1, len(transposed_tree_map[row]) - 1):
            if transposed_tree_map[row][tree] > min(max(transposed_tree_map[row][:tree]), max(transposed_tree_map[row][(tree + 1):])):
                transposed_visible_map[row][tree] = 1
    return sum([sum(row) for row in transposed_visible_map]) + 2 * len(tree_map) + 2 * (len(tree_map[0]) - 2)


def run(data_dir, star):
    with open(f'{data_dir}/input-day08.txt', 'r') as fic:
        data = [x for x in fic.read().split('\n')[:-1]]

    if star == 1:  # The final answer is: 1679
        solution = count_visible_trees(data)
    elif star == 2:  # The final answer is:
        solution = my_func(data)
    else:
        raise Exception('Star number must be either 1 or 2.')

    print(f'The solution (star {star}) is: {solution}')
    return solution
