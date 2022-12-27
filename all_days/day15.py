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

# Second star: The distress beacon is not detected by any sensor, but the distress beacon must have x and y coordinates
# each no lower than 0 and no larger than 4000000.
# To isolate the distress beacon's signal, you need to determine its tuning frequency, which can be found by multiplying
# its x coordinate by 4000000 and then adding its y coordinate.
# Find the only possible position for the distress beacon. What is its tuning frequency?

import re


def sensors_and_beacons(data):
    return [
        {'sensor': [int(y[1]), int(y[3])], 'beacon': [int(y[5]), int(y[7])]}
        for y in [re.split(', |=|:', x) for x in data]
    ]


def find_intervals(SB_coords, line=None):
    for n in range(len(SB_coords)):
        sb = SB_coords[n]
        distance_sb = abs(sb['sensor'][0] - sb['beacon'][0]) + abs(sb['sensor'][1] - sb['beacon'][1])
        SB_coords[n]['sb'] = distance_sb
        if line:
            half_interval = distance_sb - abs(line - sb['sensor'][1])
        else:
            half_interval = distance_sb
        if line:
            if half_interval > 0:
                SB_coords[n]['interval'] = [sb['sensor'][0] - half_interval, sb['sensor'][0] + half_interval]
            else:
                SB_coords[n]['interval'] = []
        else:
            SB_coords[n]['interval0'] = [sb['sensor'][0] - half_interval, sb['sensor'][0] + half_interval]
    return SB_coords


def count_places(intervals):
    intervals.sort()
    all_places = [intervals[0]]
    for i in intervals[1:]:
        if i[0] <= all_places[-1][1]:
            all_places[-1][1] = max([all_places[-1][1], i[1]])
        else:
            all_places += [i]
    return sum([x[1] - x[0] + 1 for x in all_places])


def forbidden_places(data, line=2000000):
    SB = sensors_and_beacons(data)
    SB = find_intervals(SB, line)
    return (
            count_places([sb['interval'] for sb in SB if len(sb['interval']) > 0])
            - len(list(set([sb['beacon'][0] for sb in SB if sb['beacon'][1] == line])))
    )


def tuning_frequency(data, max_value=4000000):
    SB = sensors_and_beacons(data)
    SB = find_intervals(SB)
    beacon_map = [['.' for x in range(max_value + 1)] for line in range(max_value + 1)]
    for s in SB:
        print(s)
        for dy in range(- s['sb'], s['sb'] + 1):
            for dx in range(- s['sb'] + abs(dy), s['sb'] - abs(dy) + 1):
                if (s['sensor'][1] + dy >= 0) & (s['sensor'][1] + dy <= max_value) & (s['sensor'][0] + dx >= 0) & ()

                if line + col <
                beacon_map[line][col] = '#'
        for line in beacon_map:
            print(''.join(line))
        input('next')

    # counts = [sum(line) for line in beacon_map]
    # print(counts)
    return [[14, 11], 56000011]

    # return [[free_place[0], line - 1], 4000000 * free_place[0] + line - 1]


def run(data_dir, star):
    with open(f'{data_dir}/input-day15.txt', 'r') as fic:
        data = [x for x in fic.read().split('\n')[:-1]]

    if star == 1:  # The final answer is: 4919281
        solution = forbidden_places(data)
    elif star == 2:  # The final answer is:
        solution = tuning_frequency(data)
    else:
        raise Exception('Star number must be either 1 or 2.')

    print(f'The solution (star {star}) is: {solution}')
    return solution
