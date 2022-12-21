import os
import sys

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from all_days import day20


def test_sets():
    return [
        {
            'number': 1,
            'input': [1, 2, -3, 3, -2, 0, 4],
            'expected1': [[1, 2, -3, 4, 0, 3, -2], [4, -3, 2], 3],
            'expected2': [[811589153, 2434767459,-1623178306], 1623178306]
        },
        {
            'number': 42,
            'input': [1, 2, -3, 3, -2, 0, 4, -5],
            'expected1': [[1, -5, 2, 4, 0, -3, 3, -2], [0, 0, 0], 0],
        },
        {
            'number': 12,
            'input': [11, 12, -13, 13, -12, 0, 14],
            'expected1': [[13, 0, 11, -13, 12, 14, -12], [13, -12, 14], 15],
        },
    ]


def test_first_star(test_data, expected):
    solution = day20.grove_coordinates(test_data)
    if solution != expected:
        print("Your output is:")
        print(solution)
        raise Exception(f'This is not the solution, you should get {expected}')
    print('--- Test OK')


def test_second_star(test_data, expected):
    solution = day20.grove_coordinates(test_data, 811589153, 10)
    if solution[1:] != expected:
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
            if 'expected2' in test:
                test_second_star(test['input'], test['expected2'])
        else:
            print("Error, the star must be 1 or 2.")


if __name__ == '__main__':
    main()
