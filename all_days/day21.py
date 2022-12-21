# Day21: Monkey Math

# First star: Each monkey is given a job: either to yell a specific number or to yell the result of a math operation.
# All of the number-yelling monkeys know their number from the start; however, the math operation monkeys need to wait
# for two other monkeys to yell a number, and those two other monkeys might also be waiting on other monkeys.
# Your job is to work out the number the monkey named root will yell before the monkeys figure it out themselves.

# Second star: First, you got the wrong job for the monkey named root; specifically, you got the wrong math operation.
# The correct operation for monkey root should be =, which means that it still listens for two numbers
# (from the same two monkeys as before), but now checks that the two numbers match.
# Second, you got the wrong monkey for the job starting with humn:. It isn't a monkey - it's you. Actually, you got the
# job wrong, too: you need to figure out what number you need to yell so that root's equality check passes.
# (The number that appears after humn: in your input is now irrelevant.)
# What number do you yell to pass root's equality test?

REVERSE = {'+': '-', '-': '+', '*': '/', '/': '*'}


def create_monkeys(data):
    monkeys = {}
    for monkey in data:
        values = monkey.split(' ')
        if len(values) == 2:
            monkeys[values[0][:-1]] = {'number': int(values[1])}
        elif len(values) == 4:
            monkeys[values[0][:-1]] = {'left': values[1], 'right': values[3], 'operation': values[2]}
        else:
            raise Exception(f"The parsing is problematic with the line '{monkey}', splitted in {values}")
    return monkeys


def run_math(name, monkeys):
    if 'number' in monkeys[name]:
        return monkeys[name]['number']
    else:
        if monkeys[name]['operation'] == '+':
            monkeys[name]['number'] = (
                    run_math(monkeys[name]['left'], monkeys) + run_math(monkeys[name]['right'], monkeys)
            )
            return monkeys[name]['number']
        elif monkeys[name]['operation'] == '-':
            monkeys[name]['number'] = (
                    run_math(monkeys[name]['left'], monkeys) - run_math(monkeys[name]['right'], monkeys)
            )
            return monkeys[name]['number']
        elif monkeys[name]['operation'] == '*':
            monkeys[name]['number'] = (
                    run_math(monkeys[name]['left'], monkeys) * run_math(monkeys[name]['right'], monkeys)
            )
            return monkeys[name]['number']
        elif monkeys[name]['operation'] == '/':
            monkeys[name]['number'] = (
                    run_math(monkeys[name]['left'], monkeys) / run_math(monkeys[name]['right'], monkeys)
            )
            return monkeys[name]['number']
        else:
            raise Exception(f"What is ths opération? ({monkeys[name]['operation']})")


def answer_monkeys_riddle(data, root='root'):
    monkeys = create_monkeys(data)
    return run_math(root, monkeys)


def answer_monkeys_riddle_fixed(data):
    monkeys = create_monkeys(data)
    count_monkeys = len(monkeys)
    m_reversed = {}
    m_to_pop = []
    # Process root and numerical monkeys
    for name, monkey in monkeys.items():
        if name == 'root':
            m_reversed[monkey['left']] = {'left': monkey['right'], 'right': name, 'operation': '+'}
            m_reversed[name] = {'number': 0}
        elif ('number' in monkey) & (name != 'humn'):
            m_reversed[name] = {'number': monkey['number']}
            m_to_pop += [name]
    # Get the human operation
    # I know that the human is on the left and the operation is minus
    m_for_human = [name for name in [name for name, monkey in monkeys.items() if 'left' in monkey] if
                   (monkeys[name]['left'] == 'humn') | (monkeys[name]['right'] == 'humn')][0]
    m_reversed['humn'] = {'left': m_for_human, 'right': monkeys[m_for_human]['right'], 'operation': '+'}
    # Inverse all the other monkeys
    for name in set([m_for_human, 'root', 'humn'] + m_to_pop):
        monkeys.pop(name)
    while len(m_reversed) < count_monkeys:
        to_get = [
            x
            for x in
            [v['left'] for k, v in m_reversed.items() if 'left' in v]
            + [v['right'] for k, v in m_reversed.items() if 'left' in v]
            if x not in m_reversed
        ]
        m_to_pop = []
        for name, monkey in monkeys.items():
            if name in to_get:
                m_reversed[name] = monkeys[name]
                m_to_pop += [name]
            elif monkey['left'] in to_get:
                m_reversed[monkey['left']] = {
                    'left': name, 'right': monkey['right'], 'operation': REVERSE[monkey['operation']]
                }
                m_to_pop += [name]
            elif monkey['right'] in to_get:
                if monkey['operation'] == '+':
                    m_reversed[monkey['right']] = {'left': name, 'right': monkey['left'], 'operation': '-'}
                elif monkey['operation'] == '-':
                    m_reversed[monkey['right']] = {'left': monkey['left'], 'right': name, 'operation': '-'}
                elif monkey['operation'] == '*':
                    m_reversed[monkey['right']] = {'left': name, 'right': monkey['left'], 'operation': '/'}
                elif monkey['operation'] == '/':
                    m_reversed[monkey['right']] = {'left': monkey['left'], 'right': name, 'operation': '/'}
                m_to_pop += [name]
        for name in m_to_pop:
            monkeys.pop(name)
    return run_math("humn", m_reversed)


def run(data_dir, star):
    with open(f'{data_dir}/input-day21.txt', 'r') as fic:
        data = [x for x in fic.read().split('\n')[:-1]]

    if star == 1:  # The final answer is:  232974643455000
        solution = answer_monkeys_riddle(data)
    elif star == 2:  # The final answer is: 3740214169961
        solution = answer_monkeys_riddle_fixed(data)
    else:
        raise Exception('Star number must be either 1 or 2.')

    print(f'The solution (star {star}) is: {solution}')
    return solution
