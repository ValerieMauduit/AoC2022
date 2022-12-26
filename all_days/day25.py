# Day25: Full of Hot Air

# First star:  You make a list of all of the fuel requirements (your puzzle input), but you don't recognize the number
# format either. "Okay, our Special Numeral-Analogue Fuel Units - SNAFU for short - are sort of like normal numbers.
# You know how starting on the right, normal numbers have a ones place, a tens place, a hundreds place, and so on,
# where the digit in each place tells you how many of that value you have? SNAFU works the same way, except it uses
# powers of five instead of ten. Starting from the right, you have a ones place, a fives place, a twenty-fives place,
# a one-hundred-and-twenty-fives place, and so on. It's that easy!"
# You ask why some of the digits look like - or = instead of "digits".
# "You know, I never did ask the engineers why they did that. Instead of using digits four through zero, the digits are
# 2, 1, 0, minus (written -), and double-minus (written =). Minus is worth -1, and double-minus is worth -2."
# As you go to input this number on Bob's console, you discover that some buttons you expected are missing. Instead, you
# are met with buttons labeled =, -, 0, 1, and 2. Bob needs the input value expressed as a SNAFU number, not in decimal.
# The Elves are starting to get cold. What SNAFU number do you supply to Bob's console?

# Second star: description

from numpy import log

SNAFU_DIGITS = {'=': -2, '-': -1, '0': 0, '1': 1, '2': 2}
DIGITS_SNAFU = {0: '0', 1: '1', 2: '2', 3: '=', 4: '-', 5: '0'}


def decode(snafu):
    if len(snafu) == 0:
        return None
    elif len(snafu) == 1:
        return SNAFU_DIGITS[snafu[0]]
    else:
        return SNAFU_DIGITS[snafu[-1]] + 5 * decode(snafu[:-1])


def encode(number):
    # Write in base 5
    base5 = []
    power = int(log(number) / log(5))
    while power >= 0:
        digit = number // 5 ** power
        base5 += [digit]
        number = number - digit * 5 ** power
        power -= 1
    # Transform a base 5 into a SNAFU code
    base5.reverse()
    base5 += [0]
    snafu = []
    for n in range(len(base5) - 1):
        snafu += DIGITS_SNAFU[base5[n]]
        if base5[n] > 2:
            base5[n + 1] += 1
    if base5[-1] == 1:
        snafu += ['1']
    snafu.reverse()
    return ''.join(snafu)


def decode_sum_encode(data):
    decoded = [decode(snafu_number) for snafu_number in data]
    return [decoded, sum(decoded), encode(sum(decoded))]


def run(data_dir, star):
    with open(f'{data_dir}/input-day25.txt', 'r') as fic:
        data = [x for x in fic.read().split('\n')[:-1]]

    if star == 1:  # The final answer is: 2-00=12=21-0=01--000
        solution = decode_sum_encode(data)
    elif star == 2:  # The final answer is:
        solution = my_func(data)
    else:
        raise Exception('Star number must be either 1 or 2.')

    print(f'The solution (star {star}) is: {solution}')
    return solution
