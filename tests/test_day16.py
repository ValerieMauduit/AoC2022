import os
import sys

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from all_days import day16


def test_sets():
    return [
        {
            'number': 1,
            'input': [
                'Valve AA has flow rate=0; tunnels lead to valves DD, II, BB',
                'Valve BB has flow rate=13; tunnels lead to valves CC, AA',
                'Valve CC has flow rate=2; tunnels lead to valves DD, BB',
                'Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE',
                'Valve EE has flow rate=3; tunnels lead to valves FF, DD',
                'Valve FF has flow rate=0; tunnels lead to valves EE, GG',
                'Valve GG has flow rate=0; tunnels lead to valves FF, HH',
                'Valve HH has flow rate=22; tunnel leads to valve GG',
                'Valve II has flow rate=0; tunnels lead to valves AA, JJ',
                'Valve JJ has flow rate=21; tunnel leads to valve II'
            ],
            'expected1': 1651,
            'expected2': []
        },
    ]


def test_first_star(test_data, expected):
    solution = day16.max_release_pressure(test_data, 30)
    if solution != expected:
        print("Your output is:")
        print(solution)
        raise Exception(f'This is not the solution, you should get {expected}')
    print('--- Test OK')


def test_second_star(test_data, expected):
    solution = day16.my_func(test_data)
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
