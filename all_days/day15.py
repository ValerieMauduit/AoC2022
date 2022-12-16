# Day 15: Beacon Exclusion Zone

# First star: Once a sensor finds a spot it thinks will give it a good reading, it attaches itself to a hard surface and
# begins monitoring for the nearest signal source beacon. Sensors and beacons always exist at integer coordinates. Each
# sensor knows its own position and can determine the position of a beacon precisely; however, sensors can only lock on
# to the one beacon closest to the sensor as measured by the Manhattan distance. (There is never a tie where two beacons
# are the same distance to a sensor.)
# This isn't necessarily a comprehensive map of all beacons in the area, though. Because each sensor only identifies its
# closest beacon, if a sensor detects a beacon, you know there are no other beacons that close or closer to that sensor.
# There could still be beacons that just happen to not be the closest beacon to any sensor.
# None of the detected beacons seem to be producing the distress signal, so you'll need to work out where the distress
# beacon is by working out where it isn't. For now, keep things simple by counting the positions where a beacon cannot
# possibly be along just a single row.
# Consult the report from the sensors you just deployed. In the row where y=2000000, how many positions cannot contain a
# beacon?

# Second star: description

import re


def sensors_and_beacons(data):
    return [
        {'sensor': [int(y[1]), int(y[3])], 'beacon': [int(y[5]), int(y[7])]}
        for y in [re.split(', |=|:', x) for x in data]
    ]


def find_intervals(SB_coords, line):
    for n in range(len(SB_coords)):
        sb = SB_coords[n]
        distance_sb = abs(sb['sensor'][0] - sb['beacon'][0]) + abs(sb['sensor'][1] - sb['beacon'][1])
        y_gap = abs(line - sb['sensor'][1])
        half_interval = distance_sb - y_gap
        if half_interval > 0:
            SB_coords[n]['interval'] = [sb['sensor'][0] - half_interval, sb['sensor'][0] + half_interval]
        else:
            SB_coords[n]['interval'] = []
    return SB_coords


def count_places(intervals):
    intervals.sort()
    all_places = [intervals[0]]
    for i in intervals[1:]:
        print(f'all places: {all_places}, new interval: {i}')
        if i[0] <= all_places[-1][1]:
            all_places[-1][1] = max([all_places[-1][1], i[1]])
        else:
            all_places += [i]
        input('next...')
    return sum([x[1] - x[0] + 1 for x in all_places])


def forbidden_places(data, line=2000000):
    SB = sensors_and_beacons(data)
    SB = find_intervals(SB, line)
    return (
            count_places([sb['interval'] for sb in SB if len(sb['interval']) > 0])
            - len(list(set([sb['beacon'][0] for sb in SB if sb['beacon'][1] == line])))
    )


def run(data_dir, star):
    with open(f'{data_dir}/input-day15.txt', 'r') as fic:
        data = [x for x in fic.read().split('\n')[:-1]]

    if star == 1:  # The final answer is: 4919281
        solution = forbidden_places(data)
    elif star == 2:  # The final answer is:
        solution = my_func(data)
    else:
        raise Exception('Star number must be either 1 or 2.')

    print(f'The solution (star {star}) is: {solution}')
    return solution
