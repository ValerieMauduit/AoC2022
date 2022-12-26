# Day 23: Unstable Diffusion

# First star: The scan shows Elves # and empty ground .; outside your scan, more empty ground extends a long way in
# every direction. The scan is oriented so that north is up; orthogonal directions are written N (north), S (south),
# W (west), and E (east), while diagonal directions are written NE, NW, SE, SW.
# The Elves follow a time-consuming process to figure out where they should each go; you can speed up this process
# considerably. The process consists of some number of rounds during which Elves alternate between considering where to
# move and actually moving.
# During the first half of each round, each Elf considers the eight positions adjacent to themself. If no other Elves
# are in one of those eight positions, the Elf does not do anything during this round. Otherwise, the Elf looks in each
# of four directions in the following order and proposes moving one step in the first valid direction:
# - If there is no Elf in the N, NE, or NW adjacent positions, the Elf proposes moving north one step.
# - If there is no Elf in the S, SE, or SW adjacent positions, the Elf proposes moving south one step.
# - If there is no Elf in the W, NW, or SW adjacent positions, the Elf proposes moving west one step.
# - If there is no Elf in the E, NE, or SE adjacent positions, the Elf proposes moving east one step.
# After each Elf has had a chance to propose a move, the second half of the round can begin. Simultaneously, each Elf
# moves to their proposed destination tile if they were the only Elf to propose moving to that position. If two or more
# Elves propose moving to the same position, none of those Elves move.
# Finally, at the end of the round, the first direction the Elves considered is moved to the end of the list of
# directions. For example, during the second round, the Elves would try proposing a move to the south first, then west,
# then east, then north. On the third round, the Elves would first consider west, then east, then north, then south.
# To make sure they're on the right track, the Elves like to check after round 10 that they're making good progress
# toward covering enough ground. To do this, count the number of empty ground tiles contained by the smallest rectangle
# that contains every Elf. (The edges of the rectangle should be aligned to the N/S/E/W directions; the Elves do not
# have the patience to calculate arbitrary rectangles.)
# Simulate the Elves' process and find the smallest rectangle that contains the Elves after 10 rounds. How many empty
# ground tiles does that rectangle contain?

# Second star: It seems you're on the right track. Finish simulating the process and figure out where the Elves need to
# go. How many rounds did you save them?

ORIENTATIONS = {'N': 'NSWE', 'S': 'SWEN', 'W': 'WENS', 'E': 'ENSW'}


class ElvesMap:
    def __init__(self, data, borders=0):
        data = [[x for x in line] for line in data]
        self.width = len(data[0]) + 2 * borders
        self.height = len(data) + 2 * borders
        self.elves = []
        for y in range(self.height - 2 * borders):
            for x in range(self.width - 2 * borders):
                if data[y][x] == '#':
                    self.elves += [Elf(x + borders, y + borders, self)]
        self.elves_orientation = 'N'
        self.map = (
                [['.' for x in range(self.width)] for y in range(borders)]
                + [['.' for x in range(borders)] + line + ['.' for x in range(borders)] for line in data]
                + [['.' for x in range(self.width)] for y in range(borders)]
        )

    def ideal_moves(self):
        ideal_map = [[0 for x in line] for line in self.map]
        for elf in self.elves:
            n = 0
            elf.wants_to_move = False
            while (n < 4) & (not elf.wants_to_move):
                elf.choose_move(ORIENTATIONS[self.elves_orientation][n])
                n += 1
        for elf in self.elves:
            if elf.wants_to_move:
                if ideal_map[elf.next_position[1]][elf.next_position[0]] == 0:
                    ideal_map[elf.next_position[1]][elf.next_position[0]] = elf
                else:
                    ideal_map[elf.next_position[1]][elf.next_position[0]] = 2
        return ideal_map

    def move_elves(self):
        ideal_map = self.ideal_moves()
        for y in range(self.height):
            for x in range(self.width):
                if type(ideal_map[y][x]) == Elf:
                    elf = ideal_map[y][x]
                    elf.move(elf.next_position)
        self.elves_orientation = ORIENTATIONS[self.elves_orientation][1]

    def elves_want_to_move(self):
        return True in [elf.wants_to_move for elf in self.elves]


class Elf:
    def __init__(self, x, y, elves_map):
        self.x = x
        self.y = y
        self.elves_map = elves_map
        self.wants_to_move = True
        self.next_position = None

    def look_around(self):
        return sum([
            self.elves_map.map[y][x] == '#'
            for x in range(self.x - 1, self.x + 2)
            for y in range(self.y - 1, self.y + 2)
        ]) - 1

    def choose_move(self, direction):
        if self.look_around() > 0:
            if (
                    (direction == 'N') &
                    (sum([self.elves_map.map[self.y - 1][x] == '#' for x in range(self.x - 1, self.x + 2)]) == 0)
            ):
                self.wants_to_move = True
                self.next_position = [self.x, self.y - 1]
            elif (
                    (direction == 'S') &
                    (sum([self.elves_map.map[self.y + 1][x] == '#' for x in range(self.x - 1, self.x + 2)]) == 0)
            ):
                self.wants_to_move = True
                self.next_position = [self.x, self.y + 1]
            elif (
                    (direction == 'W') &
                    (sum([self.elves_map.map[y][self.x - 1] == '#' for y in range(self.y - 1, self.y + 2)]) == 0)
            ):
                self.wants_to_move = True
                self.next_position = [self.x - 1, self.y]
            elif (
                    (direction == 'E') &
                    (sum([self.elves_map.map[y][self.x + 1] == '#' for y in range(self.y - 1, self.y + 2)]) == 0)
            ):
                self.wants_to_move = True
                self.next_position = [self.x + 1, self.y]

            else:
                self.wants_to_move = False
                self.next_position = None

    def move(self, next_position):
        self.elves_map.map[self.y][self.x] = '.'
        self.x = next_position[0]
        self.y = next_position[1]
        self.elves_map.map[self.y][self.x] = '#'


def smallest_space(data):
    elves_map = ElvesMap(data, 10)
    for n in range(10):
        elves_map.move_elves()
    final_elves_map = elves_map.map
    elves_by_line = ['#' in line for line in final_elves_map]
    min_y = elves_by_line.index(True)
    elves_by_line.reverse()
    max_y = elves_map.height - elves_by_line.index(True)
    elves_by_column = ['#' in [line[col] for line in final_elves_map] for col in range(elves_map.width)]
    min_x = elves_by_column.index(True)
    elves_by_column.reverse()
    max_x = elves_map.width - elves_by_column.index(True)
    return (max_x - min_x) * (max_y - min_y) - len(elves_map.elves)


def spread_elves(data):
    elves_map = ElvesMap(data, 100)
    rounds = 0
    while elves_map.elves_want_to_move():
        rounds += 1
        if rounds % 100 == 0:
            print('=' * 42 + str(rounds) + '=' * 42)
        elves_map.move_elves()
    return rounds


def run(data_dir, star):
    with open(f'{data_dir}/input-day23.txt', 'r') as fic:
        data = [x for x in fic.read().split('\n')[:-1]]

    if star == 1:  # The final answer is: 3762
        solution = smallest_space(data)
    elif star == 2:  # The final answer is: 997
        solution = spread_elves(data)
    else:
        raise Exception('Star number must be either 1 or 2.')

    print(f'The solution (star {star}) is: {solution}')
    return solution
