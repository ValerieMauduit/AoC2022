import os
import sys

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from all_days import day11


def test_sets():
    return [
        {
            'number': 1,
            'input': [
                'Monkey 0:\nStarting items: 79, 98\nOperation: new = old * 19\nTest: divisible by 23\nIf true: throw to monkey 2\nIf false: throw to monkey 3',
                'Monkey 1:\nStarting items: 54, 65, 75, 74\nOperation: new = old + 6\nTest: divisible by 19\nIf true: throw to monkey 2\nIf false: throw to monkey 0',
                'Monkey 2:\nStarting items: 79, 60, 97\nOperation: new = old * old\nTest: divisible by 13\nIf true: throw to monkey 1\nIf false: throw to monkey 3',
                'Monkey 3:\nStarting items: 74\nOperation: new = old + 3\nTest: divisible by 17\nIf true: throw to monkey 0\nIf false: throw to monkey 1'
            ],
            'expected1': [[101, 95, 7, 105], 10605],
            'expected2': []
        },
    ]


def test_first_star(test_data, expected):
    solution = day11.monkey_business_score(test_data, 20)
    if solution != expected:
        print("Your output is:")
        print(solution)
        raise Exception(f'This is not the solution, you should get {expected}')
    print('--- Test OK')


def test_second_star(test_data, expected):
    solution = day11.my_func(test_data)
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
