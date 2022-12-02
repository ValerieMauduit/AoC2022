# Day1: Calorie Counting

# First star:
# The Elves take turns writing down the number of Calories contained by the various meals, snacks, rations, etc. that
# they've brought with them, one item per line. Each Elf separates their own inventory from the previous Elf's inventory
# (if any) by a blank line. In case the Elves get hungry and need extra snacks, they need to know which Elf to ask:
# they'd like to know how many Calories are being carried by the Elf carrying the most Calories.
# Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?

# Second star:
# By the time you calculate the answer to the Elves' question, they've already realized that the Elf carrying the most
# Calories of food might eventually run out of snacks. To avoid this unacceptable situation, the Elves would instead
# like to know the total Calories carried by the top three Elves carrying the most Calories.
# Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?

def max_calories(elves_bags):
    return max([sum(elf_bag) for elf_bag in elves_bags])


def top3_calories_sum(elves_bags):
    elves_summary = [sum(elf_bag) for elf_bag in elves_bags]
    elves_summary.sort(reverse=True)
    return sum(elves_summary[0:3])


def run(data_dir, star):
    with open(f'{data_dir}/input-day01.txt', 'r') as fic:
        all_elves_bags = [elf_bag.split('\n') for elf_bag in fic.read().split('\n\n')]
        calories = [[int(value) for value in elf_bag if value != ''] for elf_bag in all_elves_bags]

    if star == 1:  # The final answer is: 66616
        solution = max_calories(calories)
    elif star == 2:  # The final answer is: 1999172
        solution = top3_calories_sum(calories)
    else:
        raise Exception('Star number must be either 1 or 2.')

    print(f'The solution (star {star}) is: {solution}')
    return solution
