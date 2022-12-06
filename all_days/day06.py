# Day 6: Tuning Trouble

# First star: The signal is a series of seemingly-random characters that the device receives one at a time.
# To fix the communication system, you need to add a subroutine to the device that detects a start-of-packet marker in
# the datastream. In the protocol being used by the Elves, the start of a packet is indicated by a sequence of four
# characters that are all different.
# Your subroutine needs to identify the first position where the four most recently received characters were all
# different. Specifically, it needs to report the number of characters from the beginning of the buffer to the end of
# the first such four-character marker.
#
# Second star: description

def detect_position(data):
    n = 3
    all_different = False
    while not all_different:
        n += 1
        subset = []
        subset[:0] = data[(n - 4):n]
        all_different = (len(set(subset)) == 4)
    return n


def run(data_dir, star):
    with open(f'{data_dir}/input-day06.txt', 'r') as fic:
        data = fic.read()[:-1]

    if star == 1:  # The final answer is:
        solution = detect_position(data)
    elif star == 2:  # The final answer is:
        solution = my_func(data)
    else:
        raise Exception('Star number must be either 1 or 2.')

    print(f'The solution (star {star}) is: {solution}')
    return solution
