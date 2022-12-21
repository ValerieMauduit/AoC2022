import os
import sys

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from all_days import day21


def test_sets():
    return [
        {
            'number': 0,
            'input': ['root: humn + pppw', 'pppw: 12','humn: 42'],
            'expected1': 54,
            'expected2': 12
        },
        {
            'number': 1,
            'input': [
                'root: pppw + sjmn', 'dbpl: 5', 'cczh: sllz + lgvd', 'zczc: 2', 'ptdq: humn - dvpt', 'dvpt: 3',
                'lfqf: 4', 'humn: 5', 'ljgn: 2', 'sjmn: drzm * dbpl', 'sllz: 4', 'pppw: cczh / lfqf',
                'lgvd: ljgn * ptdq', 'drzm: hmdt - zczc', 'hmdt: 32'
            ],
            'expected1': 152,
            'expected2': 301
        },
    ]


def test_first_star(test_data, expected):
    solution = day21.answer_monkeys_riddle(test_data)
    print(solution)
    if solution != expected:
        print("Your output is:")
        print(solution)
        raise Exception(f'This is not the solution, you should get {expected}')
    print('--- Test OK')


def test_second_star(test_data, expected):
    solution = day21.answer_monkeys_riddle_fixed(test_data)
    if solution != expected:
        print("Your output is:")
        print(solution)
        raise Exception(f'This is not the solution, you should get {expected}')
    print('--- Test OK')


def main():
    test_case = int(input('Which star to test? '))
    for test in test_sets():
        print(f"=== Test #{test['number']} ===")
        if test_case == 1:
            test_first_star(test['input'], test['expected1'])
        elif test_case == 2:
            test_second_star(test['input'], test['expected2'])
        else:
            print("Error, the star must be 1 or 2.")


if __name__ == '__main__':
    main()
