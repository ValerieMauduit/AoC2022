# Day5: Supply Stacks

# First star: The ship has a giant cargo crane capable of moving crates between stacks. To ensure none of the crates
# get crushed or fall over, the crane operator will rearrange them in a series of carefully-planned steps.
# After the crates are rearranged, the desired crates will be at the top of each stack.
# The Elves have a drawing of the starting stacks of crates and the rearrangement procedure (your puzzle input).
# The moves are described as: move <count of crates> from <stack> to <stack>. Crates are moved one at a time, so the
# first crate to be moved ends up below the second, tbc. After the rearrangement procedure completes, what crate ends up
# on top of each stack?

# Second star: description

import numpy as np


def format_data(data):
    n = 0
    stacks = []
    while data[n][1] != '1':
        stacks += [[*data[n][1:len(data[0]):4]]]
        n += 1
    stacks = np.array(stacks).T.tolist()
    final_stacks = []
    for stack in stacks:
        final_stacks += [[crate for crate in stack if crate != ' ']]
    arranged_data = {'stacks': final_stacks, 'moves': data[(n + 2):]}
    return arranged_data


def execute_move(stacks, move):
    commands = move.split(' ')
    count_crates = int(commands[1])
    from_stack = int(commands[3]) - 1
    to_stack = int(commands[5]) - 1
    for n in range(count_crates):
        stacks[to_stack] = [stacks[from_stack][0]] + stacks[to_stack]
        stacks[from_stack] = stacks[from_stack][1:]
    return stacks


def move_stacks_and_get_tops(data):
    for move in data['moves']:
        data['stacks'] = execute_move(data['stacks'], move)
    return [data['stacks'], ''.join([stack[0] for stack in data['stacks']])]


def run(data_dir, star):
    with open(f'{data_dir}/input-day05.txt', 'r') as fic:
        data = [x for x in fic.read().split('\n')[:-1]]
    formatted_data = format_data(data)

    if star == 1:  # The final answer is:
        solution = move_stacks_and_get_tops(formatted_data)
    elif star == 2:  # The final answer is:
        solution = my_func(data)
    else:
        raise Exception('Star number must be either 1 or 2.')

    print(f'The solution (star {star}) is: {solution}')
    return solution
