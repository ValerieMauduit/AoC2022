# Day 13: Distress Signal

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
#
# Second star: Now, you just need to put all of the packets in the right order. Disregard the blank lines in your list
# of received packets.
# The distress signal protocol also requires that you include two additional divider packets: [[2]] and [[6]].
# Using the same rules as before, organize all packets - the ones in your list of received packets as well as the two
# divider packets - into the correct order.
# Afterward, locate the divider packets. To find the decoder key for this distress signal, you need to determine the
# indices of the two divider packets and multiply them together.
# Organize all of the packets into the correct order. What is the decoder key for the distress signal?

def compare_packets(left, right):
    if type(left) == list:                                  # [?] - ?
        if len(left) == 0:                                  # [] - ?
            if type(right) == list:
                if len(right) == 0:                         # [] - []
                    return 'identical'
                else:                                       # [] - [y]
                    return 'right'
            else:                                           # [] - y
                return 'right'
        elif type(right) == list:                           # [x] - [?]
            if len(right) == 0:                             # [x] - []
                return 'left'
            else:                                           # [x] - [y]
                head_comparison = compare_packets(left[0], right[0])
                if head_comparison == 'identical':
                    return compare_packets(left[1:], right[1:])
                else:
                    return head_comparison
        else:                                               # [x] - y
            head_comparison = compare_packets(left[0], right)
            if head_comparison == 'identical':
                return compare_packets(left[1:], [])
            else:
                return head_comparison
    elif type(right) == list:                               # x - [?]
        if len(right) == 0:                                 # x - []
            return 'left'
        else:                                               # x - [y]
            head_comparison = compare_packets(left, right[0])
            if head_comparison == 'identical':
                return compare_packets([], right[1:])
            else:
                return head_comparison
    else:                                                   # x - y
        if left == right:
            return 'identical'
        elif left > right:
            return 'left'
        else:
            return 'right'


def compare_all_packets(packets):
    true_packets = []
    for n in range(len(packets)):
        if compare_packets(packets[n][0], packets[n][1]) == 'right':
            true_packets += [n + 1]
    return [true_packets, sum(true_packets)]


def merge_packets(left, right):
    result = []
    while (len(left) > 0) & (len(right) > 0):
        if compare_packets(left[0], right[0]) == 'right':
            result += [left[0]]
            left = left[1:]
        else:
            result += [right[0]]
            right = right[1:]
    result += left + right
    return result


def sort_packets(packets):
    length = len(packets)
    if length <= 1:
        return packets
    else:
        left = sort_packets(packets[:int(length / 2)])
        right = sort_packets(packets[int(length / 2):])
        return merge_packets(left, right)


def order_all_packets(packets, dividers=[[[2]], [[6]]]):
    sorted_packets = sort_packets([item for sublist in packets for item in sublist] + dividers)
    div1 = sorted_packets.index(dividers[0]) + 1
    div2 = sorted_packets.index(dividers[1]) + 1
    return [[div1, div2], div1 * div2]


def run(data_dir, star):
    with open(f'{data_dir}/input-day13.txt', 'r') as fic:
        data = [x for x in fic.read().split('\n\n')]
    packets = [[eval(y[0]), eval(y[1])] for y in [x.split('\n') for x in data]]

    if star == 1:  # The final answer is: 4821
        solution = compare_all_packets(packets)
    elif star == 2:  # The final answer is: 21890
        solution = order_all_packets(packets)
    else:
        raise Exception('Star number must be either 1 or 2.')

    print(f'The solution (star {star}) is: {solution}')
    return solution
