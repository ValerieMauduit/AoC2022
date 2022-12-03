# Day4: Camp Cleanup

# First star: Several Elves have been assigned the job of cleaning up sections of the camp. Every section has a unique
# ID number, and each Elf is assigned a range of section IDs.
# However, as some of the Elves compare their section assignments with each other, they've noticed that many of the
# assignments overlap.
# Some of the pairs have noticed that one of their assignments fully contains the other.
# In how many assignment pairs does one range fully contain the other?

# Second star: description

def overlap_count(data):
    count = 0
    for section in data:
        elf1 = [int(x) for x in section[0].split('-')]
        elf2 = [int(x) for x in section[1].split('-')]
        if (elf1[0] - elf2[0]) * (elf1[1] - elf2[1]) <= 0:
            count += 1
    return count


def run(data_dir, star):
    with open(f'{data_dir}/input-day04.txt', 'r') as fic:
        data = [x.split(',') for x in fic.read().split('\n')[:-1]]

    if star == 1:  # The final answer is: 494
        solution = overlap_count(data)
    elif star == 2:  # The final answer is:
        solution = my_func() + my_func()
    else:
        raise Exception('Star number must be either 1 or 2.')

    print(f'The solution (star {star}) is: {solution}')
    return solution
