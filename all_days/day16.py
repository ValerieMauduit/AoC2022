# Day 16: Proboscidea Volcanium

# First star: You need to get the elephants out of here, quickly. Your device estimates that you have 30 minutes before
# the volcano erupts, so you don't have time to go back out the way you came in.
# You scan the cave for other options and discover a network of pipes and pressure-release valves. You aren't sure how
# such a system got into a volcano, but you don't have time to complain; your device produces a report (your puzzle
# input) of each valve's flow rate if it were opened (in pressure per minute) and the tunnels you could use to move
# between the valves.
# There's even a valve in the room you and the elephants are currently standing in labeled AA. You estimate it will take
# you one minute to open a single valve and one minute to follow any tunnel from one valve to another. What is the most
# pressure you could release?
# All the valves begin closed. You start at valve AA. Each move takes 1min and opening a valve takes 1min. The
# release pressure is the remaining time times the flow rate.
# Work out the steps to release the most pressure in 30 minutes. What is the most pressure you can release?

# Second star: You're worried that even with an optimal approach, the pressure released won't be enough. What if you got
# one of the elephants to help you?
# It would take you 4 minutes to teach an elephant how to open the right valves in the right order, leaving you with
# only 26 minutes to actually execute your plan. Would having two of you working together be better, even if it means
# having less time? (Assume that you teach the elephant before opening any valves yourself, giving you both the same
# full 26 minutes.)

import re


def create_valves(data):
    valves = {}
    for line in data:
        tempo = line.split(';')
        valve_flow = re.split(' |=', tempo[0])
        valves[valve_flow[1]] = {
            'flow': int(valve_flow[-1]),
            'neighbours': [x for x in re.split(' |,', tempo[1]) if re.fullmatch('[A-Z][A-Z]', x)]
        }
    return valves


def best_max_pressure(flows, time_left):
    flows.sort(reverse=True)
    steps = [x for x in range(time_left - 2, -1, -2)]
    max_pressure = 0
    for n in range(min([len(steps), len(flows)])):
        max_pressure += flows[n] * steps[n]
    return max_pressure


def get_next_step(step, valves):
    neighbours = [[v, f['flow']] for v, f in valves.items() if v in valves[step['position']]['neighbours']]
    neighbours.sort(key=lambda x: x[1], reverse=True)
    neighbours = [v[0] for v in neighbours]
    next_steps = []
    for neighbour in neighbours:
        # Add the case when I move to the next valve + I open it
        if (step['time_left'] > 2) & (neighbour in step['valves_to_open']):
            time_left = step['time_left'] - 2
            pressure = valves[neighbour]['flow'] * time_left
            valves_to_open = [valve for valve in step['valves_to_open'] if valve != neighbour]
            next_steps += [{
                'valves' : step['valves'] + [{neighbour: pressure}],
                'position': neighbour,
                'valves_to_open': valves_to_open,
                'time_left': time_left,
                'obtained_pressure': step['obtained_pressure'] + pressure,
                'dream_pressure': best_max_pressure([valves[valve]['flow'] for valve in valves_to_open], time_left)
            }]
        # Add the case when I move to the next valve + I don't open it (save 1min)
        if step['time_left'] > 1:
            time_left = step['time_left'] - 1
            next_steps += [{
                'valves' : step['valves'] + [{neighbour: 0}],
                'position': neighbour,
                'valves_to_open': step['valves_to_open'],
                'time_left': time_left,
                'obtained_pressure': step['obtained_pressure'],
                'dream_pressure': best_max_pressure(
                    [valves[valve]['flow'] for valve in step['valves_to_open']],
                    time_left
                )
            }]
    return next_steps


def max_release_pressure(data, total_time):
    valves = create_valves(data)
    non_zero_valves = [valve for valve, value in valves.items() if value['flow'] > 0]
    all_paths = [
        {'valves': [{'AA': 0}],
         'position': 'AA',
         'valves_to_open': non_zero_valves,
         'time_left': total_time,
         'obtained_pressure': 0,
         'dream_pressure': best_max_pressure([valves[valve]['flow'] for valve in non_zero_valves], total_time)}
    ]
    max_pressure = 0
    while len(all_paths) > 0:
        if (all_paths[0]['dream_pressure'] + all_paths[0]['obtained_pressure']) < max_pressure:
            all_paths = all_paths[1:]
        else:
            if all_paths[0]['obtained_pressure'] > max_pressure:
                max_pressure = all_paths[0]['obtained_pressure']
                print(f"Max pressure increased to {max_pressure}, still {len(all_paths)} branches to explore")
            if all_paths[0]['dream_pressure'] > 0:
                new_paths = get_next_step(all_paths[0], valves)
                all_paths = new_paths + all_paths[1:]
            else:
                all_paths = all_paths[1:]
    return max_pressure


def max_release_pressure_two_people(data, total_time):
    valves = create_valves(data)
    non_zero_valves = [valve for valve, value in valves.items() if value['flow'] > 0]
    first_step = {
        'valves': [{'AA': 0}],
        'position': 'AA',
        'valves_to_open': non_zero_valves,
        'time_left': total_time,
        'obtained_pressure': 0,
        'dream_pressure': best_max_pressure([valves[valve]['flow'] for valve in non_zero_valves], total_time)
    }
    all_paths = [[first_step, first_step]]
    max_pressure = 0
    while len(all_paths) > 0:
        if (
                all_paths[0][0]['dream_pressure'] + all_paths[0][0]['obtained_pressure'] +
                all_paths[0][1]['dream_pressure'] + all_paths[0][1]['obtained_pressure']
        ) < max_pressure:
            all_paths = all_paths[1:]
        else:
            if (all_paths[0][0]['obtained_pressure'] + all_paths[0][1]['obtained_pressure']) > max_pressure:
                max_pressure = all_paths[0][0]['obtained_pressure'] + all_paths[0][1]['obtained_pressure']
                print(f"Max pressure increased to {max_pressure}, still {len(all_paths)} branches to explore")
            if (all_paths[0][0]['dream_pressure'] + all_paths[0][1]['dream_pressure']) > 0:
                new_paths0 = get_next_step(all_paths[0][0], valves)
                new_paths1 = get_next_step(all_paths[0][1], valves)
                new_paths_two_people = []
                for p0 in new_paths0:
                    for p1 in new_paths1:
                        if (
                                (p0['valves'][-1].keys() != p1['valves'][-1].keys()) |
                                (list(p0['valves'][-1].values())[0] == 0) |
                                (list(p1['valves'][-1].values())[0] == 0)
                        ):
                            valves_to_open = [v for v in p0['valves_to_open'] if v in p1['valves_to_open']]
                            p0['valves_to_open'] = valves_to_open
                            p1['valves_to_open'] = valves_to_open
                            new_paths_two_people += [[p0, p1]]
                all_paths = new_paths_two_people + all_paths[1:]
            else:
                all_paths = all_paths[1:]
    return max_pressure


def run(data_dir, star):
    with open(f'{data_dir}/input-day16.txt', 'r') as fic:
        data = [x for x in fic.read().split('\n')[:-1]]

    if star == 1:  # The final answer is: 1647
        solution = max_release_pressure(data, 30)
    elif star == 2:  # The final answer is:
        solution = max_release_pressure_two_people(data, 26)
    else:
        raise Exception('Star number must be either 1 or 2.')

    print(f'The solution (star {star}) is: {solution}')
    return solution
