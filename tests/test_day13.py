import os
import sys

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from all_days import day13


def test_sets():
    return [
        {
            'number': 42,
            'input': [[
                [
                    [[[]]],
                    [
                        [10, 10, 10], [[8, 9, 6, 4, 1]], [[5, 0, 4, 7], [5, 4, 1, 7], 3, 9, [8, 10]],
                        [[9, 0, 9], 7, 2, 9],
                        [[6], [0, 7, 10, 2], [5, 6, 10], [5, 8, 5], 1]
                    ],
                    [[4], [[], [7, 2], [9], [9, 0, 8, 3, 10]], 10, [4, 7, 3, 3, [1, 9, 4, 3]]], [1, 2]
                ],
                [
                    [8, 4], [[], 7, 7], [[[10, 1], [7, 5, 7, 0]], [[3], [2, 3, 3, 6]]],
                    [[9, 6, 5, 5], 3, [1, [10], 9, [6]], 5, 3], [[], [8, 4, 3, 3]]
                ]
            ]],
            'expected1': [[1], 1],
            'expected2': [[2, 3], 6]
        },
        {
            'number': 1,
            'input': [
                [[1, 1, 3, 1, 1], [1, 1, 5, 1, 1]],
                [[[1], [2, 3, 4]], [[1], 4]],
                [[9], [[8, 7, 6]]],
                [[[4, 4], 4, 4], [[4, 4], 4, 4, 4]],
                [[7, 7, 7, 7], [7, 7, 7]],
                [[], [3]],
                [[[[]]], [[]]],
                [[1, [2, [3, [4, [5, 6, 7]]]], 8, 9], [1, [2, [3, [4, [5, 6, 0]]]], 8, 9]]
            ],
            'expected1': [[1, 2, 4, 6], 13],
            'expected2': [[10, 14], 140]
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
    solution = day13.order_all_packets(test_data)
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
