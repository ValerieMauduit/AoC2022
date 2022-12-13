import os
import sys

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from all_days import day13


def test_sets():
    return [
        {
            'number': 1,
            'input': [
                [[1, 1, 3, 1, 1], [1, 1, 5, 1, 1]], [[[1], [2, 3, 4]], [[1], 4]], [[9], [[8, 7, 6]]],
                [[[4, 4], 4, 4], [[4, 4], 4, 4, 4]], [[7, 7, 7, 7], [7, 7, 7]], [[], [3]], [[[[]]], [[]]],
                [[1, [2, [3, [4, [5, 6, 7]]]], 8, 9], [1, [2, [3, [4, [5, 6, 0]]]], 8, 9]]
            ],
            'expected1': [[1, 2, 4, 6], 13],
            'expected2': []
        },
    ]


def test_first_star(test_data, expected):
    solution = day13.compare_all_packets(test_data)
    if solution != expected:
        print("Your output is:")
        print(solution)
        raise Exception(f'This is not the solution, you should get {expected}')
    print('--- Test OK')


def test_second_star(test_data, expected):
    solution = day13.my_func(test_data)
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
