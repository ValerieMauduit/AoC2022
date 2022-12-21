# Day 20: Grove Positioning System

# First star: Your handheld device has a file (your puzzle input) that contains the grove's coordinates! Unfortunately,
# the file is encrypted - just in case the device were to fall into the wrong hands. Maybe you can decrypt it?
# When you were still back at the camp, you overheard some Elves talking about coordinate file encryption. The main
# operation involved in decrypting the file is called mixing.
# The encrypted file is a list of numbers. To mix the file, move each number forward or backward in the file a number
# of positions equal to the value of the number being moved. The list is circular, so moving a number off one end of the
# list wraps back around to the other end as if the ends were connected.
# The numbers should be moved in the order they originally appear in the encrypted file. Numbers moving around during
# the mixing process do not change the order in which the numbers are moved.
# Then, the grove coordinates can be found by looking at the 1000th, 2000th, and 3000th numbers after the value 0,
# wrapping around the list as necessary.
# Mix your encrypted file exactly once. What is the sum of the three numbers that form the grove coordinates?

# Second star: description

def mix(typed_data):
    length = len(typed_data)
    for n in range(len(typed_data)):
        item = [x for x in typed_data if x[1] == n][0]
        old_position = typed_data.index(item)
        number = item[0]
        new_position = (old_position + number) % (length - 1)
        if new_position == 0:
            new_position = length
        if new_position < 0:
            new_position = length + new_position
        if new_position > old_position:
            typed_data = (
                    typed_data[:old_position] + typed_data[(old_position + 1):(new_position + 1)] + [item]
                    + typed_data[(new_position + 1):]
            )
        elif new_position < old_position:
            typed_data = (
                    typed_data[:new_position] + [item] + typed_data[new_position:old_position]
                    + typed_data[(old_position + 1):]
            )
    return typed_data


def grove_coordinates(data, encryption=1, rounds = 1):
    data = [x * encryption for x in data]
    length = len(data)
    typed_data = [[data[n], n] for n in range(length)]
    for n in range(rounds):
        typed_data = mix(typed_data)
    mixed_data = [x[0] for x in typed_data]
    position_zero = mixed_data.index(0)
    three_coordinates = [
        mixed_data[(1000 % length + position_zero) % length],
        mixed_data[(2000 % length + position_zero) % length],
        mixed_data[(3000 % length + position_zero) % length],
    ]
    return [mixed_data, three_coordinates, sum(three_coordinates)]


def run(data_dir, star):
    with open(f'{data_dir}/input-day20.txt', 'r') as fic:
        data = [int(x) for x in fic.read().split('\n')[:-1]]

    if star == 1:  # The final answer is: 13522
        solution = grove_coordinates(data)
    elif star == 2:  # The final answer is: 17113168880158
        solution = grove_coordinates(data, 811589153, 10)
    else:
        raise Exception('Star number must be either 1 or 2.')

    print(f'The solution (star {star}) is: {solution}')
    return solution
