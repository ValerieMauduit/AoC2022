import os
import sys

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from all_days import day15


def test_sets():
    return [
        {
            'number': 1,
            'input': [
                'Sensor at x=2, y=18: closest beacon is at x=-2, y=15',
                'Sensor at x=9, y=16: closest beacon is at x=10, y=16',
                'Sensor at x=13, y=2: closest beacon is at x=15, y=3',
                'Sensor at x=12, y=14: closest beacon is at x=10, y=16',
                'Sensor at x=10, y=20: closest beacon is at x=10, y=16',
                'Sensor at x=14, y=17: closest beacon is at x=10, y=16',
                'Sensor at x=8, y=7: closest beacon is at x=2, y=10',
                'Sensor at x=2, y=0: closest beacon is at x=2, y=10',
                'Sensor at x=0, y=11: closest beacon is at x=2, y=10',
                'Sensor at x=20, y=14: closest beacon is at x=25, y=17',
                'Sensor at x=17, y=20: closest beacon is at x=21, y=22',
                'Sensor at x=16, y=7: closest beacon is at x=15, y=3',
                'Sensor at x=14, y=3: closest beacon is at x=15, y=3',
                'Sensor at x=20, y=1: closest beacon is at x=15, y=3'
            ],
            'expected1': 26,
            'expected2': []
        },
    ]


def test_first_star(test_data, expected):
    solution = day15.forbidden_places(test_data, 10)
    if solution != expected:
        print("Your output is:")
        print(solution)
        raise Exception(f'This is not the solution, you should get {expected}')
    print('--- Test OK')


def test_second_star(test_data, expected):
    solution = day15.my_func(test_data)
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
