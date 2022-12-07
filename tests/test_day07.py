import os
import sys

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from all_days import day07


def test_sets():
    return [
        {
            'number': 1,
            'input': [
                '$ cd /', '$ ls', 'dir a', '14848514 b.txt', '8504156 c.dat', 'dir d', '$ cd a', '$ ls', 'dir e',
                '29116 f', '2557 g', '62596 h.lst', '$ cd e', '$ ls', '584 i', '$ cd ..', '$ cd ..', '$ cd d', '$ ls',
                '4060174 j', '8033020 d.log', '5626152 d.ext', '7214296 k'
            ],
            'expected1': 95437,
            'expected2': []
        },
    ]


def test_first_star(test_data, expected):
    solution = day07.find_small_dirs(test_data)
    if solution != expected:
        print("Your output is:")
        print(solution)
        raise Exception(f'This is not the solution, you should get {expected}')
    print('--- Test OK')


def test_second_star(test_data, expected):
    solution = day07.my_func(test_data)
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
