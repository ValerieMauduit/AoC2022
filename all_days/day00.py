# Day1: title

# First star: description

# Second star: description

def my_func():
    return 42


def run(data_dir, star):
    with open(f'{data_dir}/input-day00.txt', 'r') as fic:
        data = [int(x) for x in fic.read().split('\n')[:-1]]

    if star == 1:  # The final answer is:
        solution = my_func()
    elif star == 2:  # The final answer is:
        solution = my_func() + my_func()
    else:
        raise Exception('Star number must be either 1 or 2.')

    print(f'The solution (star {star}) is: {solution}')
    return solution
