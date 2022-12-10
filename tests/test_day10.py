import os
import sys

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from all_days import day10


def test_sets():
    return [
        {
            'number': 1,
            'input': [
                'addx 15', 'addx -11', 'addx 6', 'addx -3', 'addx 5', 'addx -1', 'addx -8', 'addx 13', 'addx 4', 'noop',
                'addx -1', 'addx 5', 'addx -1', 'addx 5', 'addx -1', 'addx 5', 'addx -1', 'addx 5', 'addx -1',
                'addx -35', 'addx 1', 'addx 24', 'addx -19', 'addx 1', 'addx 16', 'addx -11', 'noop', 'noop', 'addx 21',
                'addx -15', 'noop', 'noop', 'addx -3', 'addx 9', 'addx 1', 'addx -3', 'addx 8', 'addx 1', 'addx 5',
                'noop', 'noop', 'noop', 'noop', 'noop', 'addx -36', 'noop', 'addx 1', 'addx 7', 'noop', 'noop', 'noop',
                'addx 2', 'addx 6', 'noop', 'noop', 'noop', 'noop', 'noop', 'addx 1', 'noop', 'noop', 'addx 7',
                'addx 1', 'noop', 'addx -13', 'addx 13', 'addx 7', 'noop', 'addx 1', 'addx -33', 'noop', 'noop', 'noop',
                'addx 2', 'noop', 'noop', 'noop', 'addx 8', 'noop', 'addx -1', 'addx 2', 'addx 1', 'noop', 'addx 17',
                'addx -9', 'addx 1', 'addx 1', 'addx -3', 'addx 11', 'noop', 'noop', 'addx 1', 'noop', 'addx 1', 'noop',
                'noop', 'addx -13', 'addx -19', 'addx 1', 'addx 3', 'addx 26', 'addx -30', 'addx 12', 'addx -1',
                'addx 3', 'addx 1', 'noop', 'noop', 'noop', 'addx -9', 'addx 18', 'addx 1', 'addx 2', 'noop', 'noop',
                'addx 9', 'noop', 'noop', 'noop', 'addx -1', 'addx 2', 'addx -37', 'addx 1', 'addx 3', 'noop',
                'addx 15', 'addx -21', 'addx 22', 'addx -6', 'addx 1', 'noop', 'addx 2', 'addx 1', 'noop', 'addx -10',
                'noop', 'noop', 'addx 20', 'addx 1', 'addx 2', 'addx 2', 'addx -6', 'addx -11', 'noop', 'noop', 'noop'
            ],
            'expected1': [[420, 1140, 1800, 2940, 2880, 3960], 13140],
            'expected2': [
                '##..##..##..##..##..##..##..##..##..##..', '###...###...###...###...###...###...###.',
                '####....####....####....####....####....', '#####.....#####.....#####.....#####.....',
                '######......######......######......####', '#######.......#######.......#######.....'
            ]
        },
    ]


def test_first_star(test_data, expected):
    solution = day10.cathode_tube_scores(test_data)
    if solution != expected:
        print("Your output is:")
        print(solution)
        raise Exception(f'This is not the solution, you should get {expected}')
    print('--- Test OK')


def test_second_star(test_data, expected):
    solution = day10.render_image(test_data)
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
