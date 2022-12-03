# Day3: Rucksack Reorganization

# First star: One Elf has the important job of loading all of the rucksacks with supplies for the jungle journey.
# Each rucksack has two large compartments. All items of a given type are meant to go into exactly one of the two
# compartments. The Elf that did the packing failed to follow this rule for exactly one item type per rucksack.
# The Elves have made a list of all of the items currently in each rucksack (your puzzle input). Every item type is
# identified by a single lowercase or uppercase letter (that is, a and A refer to different types of items).
# The list of items for each rucksack is given as characters all on a single line. A given rucksack always has the same
# number of items in each of its two compartments, so the first half of the characters represent items in the first
# compartment, while the second half of the characters represent items in the second compartment.
# To help prioritize item rearrangement, every item type can be converted to a priority:
# Lowercase item types a through z have priorities 1 through 26.
# Uppercase item types A through Z have priorities 27 through 52.
# Find the item type that appears in both compartments of each rucksack. What is the sum of the priorities of those item
# types?

# Second star: For safety, the Elves are divided into groups of three. Every Elf carries a badge that identifies their
# group. For efficiency, within each group of three Elves, the badge is the only item type carried by all three Elves.
# The problem is that someone forgot to put this year's updated authenticity sticker on the badges. All of the badges
# need to be pulled out of the rucksacks so the new authenticity stickers can be attached.
# Additionally, nobody wrote down which item type corresponds to each group's badges. The only way to tell which item
# type is the right one is by finding the one item type that is common between all three Elves in each group.
# Find the item type that corresponds to the badges of each three-Elf group. What is the sum of the priorities of those
# item types?

import re


def wrong_item(rucksack):
    compartment_size = int(len(rucksack) / 2)
    return re.search(f"[{rucksack[:compartment_size]}]", rucksack[compartment_size:]).group()


def count_score(wrong_items):
    return [re.search(item, "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ").span()[1] for item in wrong_items]


def process_all_rucksacks(data):
    wrong_items = [wrong_item(rucksack) for rucksack in data]
    return [wrong_items, sum(count_score(wrong_items))]


def find_badges(data):
    nb_groups = int(len(data) / 3)
    badges = []
    for group in range(nb_groups):
        rucksacks = data[(3 * group):(3 * group + 3)]
        badge = None
        for item in rucksacks[0]:
            if badge is None:
                found_in_rucksack1 = re.search(item, rucksacks[1])
                found_in_rucksack2 = re.search(item, rucksacks[2])
                if not((found_in_rucksack1 is None) | (found_in_rucksack2 is None)):
                    badge = found_in_rucksack1.group()
        badges += [badge]
    return badges


def groups_score(data):
    badges = find_badges(data)
    return [badges, sum(count_score(badges))]


def run(data_dir, star):
    with open(f'{data_dir}/input-day03.txt', 'r') as fic:
        data = [x for x in fic.read().split('\n')[:-1]]

    if star == 1:  # The final answer is: 7746
        solution = process_all_rucksacks(data)
    elif star == 2:  # The final answer is: 2604
        solution = groups_score(data)
    else:
        raise Exception('Star number must be either 1 or 2.')

    print(f'The solution (star {star}) is: {solution}')
    return solution
