# Day 13: title

# First star: Your handheld device must still not be working properly; the packets from the distress signal got decoded
# out of order. You'll need to re-order the list of received packets (your puzzle input) to decode the message.
# Your list consists of pairs of packets; pairs are separated by a blank line. You need to identify how many pairs of
# packets are in the right order.
# Packet data consists of lists and integers. Each list starts with [, ends with ], and contains zero or more
# comma-separated values (either integers or other lists). Each packet is always a list and appears on its own line.
# When comparing two values, the first value is called left and the second value is called right. Then:
# - If both values are integers, the lower integer should come first. If the left integer is lower than the right
#   integer, the inputs are in the right order. If the left integer is higher than the right integer, the inputs are not
#   in the right order. Otherwise, the inputs are the same integer; continue checking the next part of the input.
# - If both values are lists, compare the first value of each list, then the second value, and so on. If the left list
#   runs out of items first, the inputs are in the right order. If the right list runs out of items first, the inputs
#   are not in the right order. If the lists are the same length and no comparison makes a decision about the order,
#   continue checking the next part of the input.
# - If exactly one value is an integer, convert the integer to a list which contains that integer as its only value,
#   then retry the comparison. For example, if comparing [0,0,0] and 2, convert the right value to [2] (a list
#   containing 2); the result is then found by instead comparing [0,0,0] and [2].
# Determine which pairs of packets are already in the right order. What is the sum of the indices of those pairs?

# Second star: description

def compare_packets(left, right, space=''):
    print(f'{space}{left} vs {right}')
    space += '  '
    if type(left) == list:
        if len(left) == 0:
            print(f'{space}True')
            return True
        elif type(right) == list:  # left: list, right: list
            if len(right) == 0:
                print(f'{space}False')
                return False
            elif left[0] == right[0]:
                return compare_packets(left[1:], right[1:], space)
            else:
                return compare_packets(left[0], right[0], space)
        else:                      # left: list, right: number
            return compare_packets(left[0], right, space)
    elif type(right) == list:      # left: number, right: list
        if len(right) == 0:
            print(f'{space}False')
            return False
        else:
            return compare_packets(left, right[0], space)
    else:                          # left: number, right: number
        print(f'{space}{left < right}')
        return left < right


def compare_all_packets(packets):
    true_packets = []
    for n in range(len(packets)):
        input('-' * 69)
        if compare_packets(packets[n][0], packets[n][1]):
            true_packets += [n + 1]
    return [true_packets, sum(true_packets)]


def run(data_dir, star):
    with open(f'{data_dir}/input-day13.txt', 'r') as fic:
        data = [x for x in fic.read().split('\n\n')]
    packets = [[eval(y[0]), eval(y[1])] for y in [x.split('\n') for x in data]]

    if star == 1:  # The final answer is: 4486
        solution = compare_all_packets(packets)
    elif star == 2:  # The final answer is:
        solution = my_func(data)
    else:
        raise Exception('Star number must be either 1 or 2.')

    print(f'The solution (star {star}) is: {solution}')
    return solution
