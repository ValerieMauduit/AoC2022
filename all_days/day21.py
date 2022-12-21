# Day21: Monkey Math

# First star: Each monkey is given a job: either to yell a specific number or to yell the result of a math operation.
# All of the number-yelling monkeys know their number from the start; however, the math operation monkeys need to wait
# for two other monkeys to yell a number, and those two other monkeys might also be waiting on other monkeys.
# Your job is to work out the number the monkey named root will yell before the monkeys figure it out themselves.

# Second star: description

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


def answer_monkeys_riddle(data):
    monkeys = create_monkeys(data)
    return run_math('root', monkeys)


def run(data_dir, star):
    with open(f'{data_dir}/input-day21.txt', 'r') as fic:
        data = [x for x in fic.read().split('\n')[:-1]]

    if star == 1:  # The final answer is:  232974643455000
        solution = answer_monkeys_riddle(data)
    elif star == 2:  # The final answer is:
        solution = my_func(data)
    else:
        raise Exception('Star number must be either 1 or 2.')

    print(f'The solution (star {star}) is: {solution}')
    return solution
