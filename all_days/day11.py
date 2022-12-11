# Day 11: Monkey in the Middle

# First star: To get your stuff back, you need to be able to predict where the monkeys will throw your items. After some
# careful observation, you realize the monkeys operate based on how worried you are about each item. You take some notes
# (your puzzle input) on the items each monkey currently has, how worried you are about those items, and how the monkey
# makes decisions based on your worry level.
# Starting items lists your worry level for each item the monkey is currently holding in the order they will be
# inspected.
# Operation shows how your worry level changes as that monkey inspects an item. (An operation like new = old * 5 means
# that your worry level after the monkey inspected the item is five times whatever your worry level was before
# inspection.)
# After each monkey inspects an item your relief that the monkey's inspection didn't damage the item causes your worry
# level to be divided by three and rounded down to the nearest integer.
# Then, the test shows how the monkey uses your worry level to decide where to throw an item next.
# If true shows what happens with an item if the Test was true.
# If false shows what happens with an item if the Test was false.
# The monkeys take turns inspecting and throwing items. On a single monkey's turn, it inspects and throws all of the
# items it is holding one at a time and in the order listed. Monkey 0 goes first, then monkey 1, and so on until each
# monkey has had one turn. The process of each monkey taking a single turn is called a round.
# When a monkey throws an item to another monkey, the item goes on the end of the recipient monkey's list. A monkey that
# starts a round with no items could end up inspecting and throwing many items by the time its turn comes around. If a
# monkey is holding no items at the start of its turn, its turn ends.
# Chasing all of the monkeys at once is impossible; you're going to have to focus on the two most active monkeys if you
# want any hope of getting your stuff back. Count the total number of times each monkey inspects items over 20 rounds.
# Figure out which monkeys to chase by counting how many items they inspect over 20 rounds. What is the level of monkey
# business after 20 rounds of stuff-slinging simian shenanigans?

# Second star: Worry levels are no longer divided by three after each item is inspected; you'll need to find another way
# to keep your worry levels manageable. Starting again from the initial state in your puzzle input, what is the level of
# monkey business after 10000 rounds?

def one_round_congruence(monkeys):
    inspected = []
    for nb in range(len(monkeys)):
        monkey = monkeys[nb]
        inspected += [len(monkey['congruences'])]
        for item in monkey['congruences']:
            new = {}
            for divisor in item:
                old = item[divisor]
                new[divisor] = eval(monkey['formula']) % divisor
            if new[monkey['divisor']] == 0:
                monkeys[monkey['true']]['congruences'] += [new]
            else:
                monkeys[monkey['false']]['congruences'] += [new]
        monkeys[nb]['congruences'] = []
    return {'inspected': inspected, 'monkeys': monkeys}


def one_round(monkeys, decreasing):
    inspected = []
    for nb in range(len(monkeys)):
        monkey = monkeys[nb]
        inspected += [len(monkey['items'])]
        for old in monkey['items']:
            new = int(eval(monkey['formula']) / decreasing)
            if new % monkey['divisor'] == 0:
                monkeys[monkey['true']]['items'] += [new]
            else:
                monkeys[monkey['false']]['items'] += [new]
        monkeys[nb]['items'] = []
    return {'inspected': inspected, 'monkeys': monkeys}


def create_monkeys(data):
    monkeys = []
    for definition in data:
        instructions = definition.split('\n')
        monkeys += [{
            'items': [int(x) for x in instructions[1].split(':')[1].split(',')],
            'formula': instructions[2].split('=')[1],
            'divisor': int(instructions[3].split(' ')[-1]),
            'true': int(instructions[4].split(' ')[-1]),
            'false': int(instructions[5].split(' ')[-1])
        }]
    return monkeys


def items_congruences(monkeys):
    divisors = set([monkey['divisor'] for monkey in monkeys])
    for nb in range(len(monkeys)):
        items = monkeys[nb]['items']
        congruences = [{d: item % d for d in divisors} for item in items]
        monkeys[nb]['congruences'] = congruences
    return monkeys


def monkey_business_score(data, rounds, decreasing):
    monkeys = create_monkeys(data)
    monkeys = items_congruences(monkeys)
    inspected = [0 for k in monkeys]
    for round in range(rounds):
        if round % 100 == 0:
            print(f'round {round}')
        if decreasing == 1:
            round_results = one_round_congruence(monkeys)
        else:
            round_results = one_round(monkeys, decreasing)
        inspected = [inspected[n] + round_results['inspected'][n] for n in range(len(monkeys))]
        monkeys = round_results['monkeys']
    return [inspected, sorted(inspected)[-2] * sorted(inspected)[-1]]


def run(data_dir, star):
    with open(f'{data_dir}/input-day11.txt', 'r') as fic:
        data = [x for x in fic.read().split('\n\n')]

    if star == 1:  # The final answer is: 61005
        solution = monkey_business_score(data, 20, 3)
    elif star == 2:  # The final answer is: 20567144694
        solution = monkey_business_score(data, 10000, 1)
    else:
        raise Exception('Star number must be either 1 or 2.')

    print(f'The solution (star {star}) is: {solution}')
    return solution
