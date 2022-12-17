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

# Second star: description

import re


class Valve:
    def __init__(self, name, flow):
        self.name = name
        self.flow = flow
        # self.web = web
        # self.web.add_valve(self)
        self.connections = []
        self.opened = 0

    def add_connection(self, valve):
        # for name in names:
        #     if ~self.web.contains(name):
        #         self.web.add_valve(Valve(name, None, self.web))
        # self.connections = 42

    def open_valve(self, time):
        self.opened = time

    def release_gas(self, end):
        if self.opened > 0:
            return (end -self.opened) * self.flow
        else:
            return 0


class ValveGraph:
    def __init__(self):
        self.valves = []

    def contains(self, item):
        return len([x for x in self.valves if x.name == item]) > 0

    def add_valve(self, valve):
        if valve not in self.valves:
            self.valves += [valve]



def create_valves(data):
    valves = ValveGraph()
    for line in data:
        tempo = line.split(';')
        valve_flow = re.split(' |=', tempo[0])
        valve = Valve(valve_flow[1], valve_flow[-1])
        valves.add_valve(valve)
        for linked in [x for x in re.split(' |,', tempo[1]) if re.fullmatch('[A-Z][A-Z]', x)]:
            if valves.contains(linked):
                x = 42
            else:
                other_valve = Valve(linked, None)
                valve.add_connection(other_valve)
                valves.add_valve(other_valve)


    return valves


def max_release_pressure(data):
    valves = create_valves(data)
    return max(release_pressures(valves))


def run(data_dir, star):
    with open(f'{data_dir}/input-day16.txt', 'r') as fic:
        data = [x for x in fic.read().split('\n')[:-1]]

    if star == 1:  # The final answer is:
        solution = max_release_pressure(data)
    elif star == 2:  # The final answer is:
        solution = my_func(data)
    else:
        raise Exception('Star number must be either 1 or 2.')

    print(f'The solution (star {star}) is: {solution}')
    return solution
