# Day 22: Monkey Map

# First star: To pass through the force field, you have to enter a password; doing so involves tracing a specific path
# on a strangely-shaped board.At least, you're pretty sure that's what you have to do; the elephants aren't exactly
# fluent in monkey.
# The monkeys give you notes that they took when they last saw the password entered (your puzzle input).
# The first half of the monkeys' notes is a map of the board. It comprises a set of open tiles (on which you can
# move, drawn .) and solid walls (tiles which you cannot enter, drawn #).
# The second half is a description of the path you must follow. It consists of alternating numbers and letters.
# - A number indicates the number of tiles to move in the direction you are facing. If you run into a wall, you stop
#   moving forward and continue with the next instruction.
# - A letter indicates whether to turn 90 degrees clockwise (R) or counterclockwise (L). Turning happens in-place; it
#   does not change your current tile.
# You begin the path in the leftmost open tile of the top row of tiles. Initially, you are facing to the right (from
# the perspective of how the map is drawn).
# If a movement instruction would take you off of the map, you wrap around to the other side of the board. In other
# words, if your next tile is off of the board, you should instead look in the direction opposite of your current facing
# as far as you can until you find the opposite edge of the board, then reappear there.
# To finish providing the password to this strange input device, you need to determine numbers for your final row,
# column, and facing as your final position appears from the perspective of the original map. Rows start from 1 at the
# top and count downward; columns start from 1 at the left and count rightward. (In the above example, row 1, column 1
# refers to the empty space with no tile on it in the top-left corner.) Facing is 0 for right (>), 1 for down (v), 2 for
# left (<), and 3 for up (^). The final password is the sum of 1000 times the row, 4 times the column, and the facing.
# Follow the path given in the monkeys' notes. What is the final password?

# Second star: description

import re

TURN_COUNT = {'R': 0, 'D': 1, 'L': 2, 'U': 3}
TURN = {'R': {'R': 'D', 'D': 'L', 'L': 'U', 'U': 'R'}, 'L': {'R': 'U', 'D': 'R', 'L': 'D', 'U': 'L'}}
MARKERS = {'R': '>', 'D': 'v', 'L': '<', 'U': '^'}


class MonkeyMap:
    def __init__(self, data):
        self.lines = [Line(definition) for definition in data]
        self.height = len(data)
        self.width = max([line.stop for line in self.lines])
        self.columns = [
            Line(definition)
            for definition in [
                ''.join([line[col] if col < len(line) else '' for line in data ])
                for col in range(self.width)
            ]
        ]
        self.drawing_map = [[x for x in definition] for definition in data]


class Line:
    def __init__(self, definition):
        line_in_list = [x for x in definition]
        search_map = re.search('[\.#]+', definition)
        self.start = search_map.start()
        self.stop = search_map.end()
        self.map = [x for x in line_in_list if x != ' ']
        self.length = self.stop - self.start


class Santa:
    def __init__(self, monkey_map):
        self.monkey_map = monkey_map
        self.y = 0
        self.x = monkey_map.lines[0].start
        self.orientation = 'R'

    def row(self):
        return self.monkey_map.lines[self.y]

    def col(self):
        return self.monkey_map.columns[self.x]

    def move(self, distance):
        if self.orientation == 'R':
            local_x = self.x - self.row().start
            if '#' in self.row().map:
                wall = (self.row().map + self.row().map)[local_x:].index('#')
                self.x = (local_x + min([distance, wall - 1])) % self.row().length + self.row().start
            else:
                self.x = (local_x + distance) % self.row().length + self.row().start
        elif self.orientation == 'L':
            local_x = self.x - self.row().start
            if '#' in self.row().map:
                tempo_line = [x for x in self.row().map + self.row().map]
                tempo_line.reverse()
                wall = tempo_line[(self.row().length - local_x - 1):].index('#')
                self.x = (local_x - min([distance, wall - 1]) + self.row().length) % self.row().length + self.row().start
            else:
                self.x = (local_x + self.row().length - distance % self.row().length) % self.row().length + self.row().start
        elif self.orientation == 'D':
            local_y = self.y - self.col().start
            if '#' in self.col().map:
                wall = (self.col().map + self.col().map)[local_y:].index('#')
                self.y = (local_y + min([distance, wall - 1])) % self.col().length + self.col().start
            else:
                self.y = (self.y + distance) % self.col().length + self.col().start
        elif self.orientation == 'U':
            local_y = self.y - self.col().start
            if '#' in self.col().map:
                tempo_col = [x for x in self.col().map + self.col().map]
                tempo_col.reverse()
                wall = tempo_col[(self.col().length - local_y - 1):].index('#')
                self.y = (local_y - min([distance, wall - 1]) + self.col().length) % self.col().length + self.col().start
            else:
                self.y = (local_y + self.col().length - distance % self.col().length) % self.col().length + self.col().start
        else:
            raise Exception(f"WTF is this orientation? ({self.orientation})")

    def turn(self, direction):
        self.orientation = TURN[direction][self.orientation]


def get_password(data):
    monkey_map = MonkeyMap(data[0])
    santa = Santa(monkey_map)
    distances = [int(x) for x in re.split('R|L', data[1])]
    turns = re.split('[0-9]+', data[1])[1:-1]
    for move in range(len(distances) - 1):
        last_position = [santa.x, santa.y]
        last_orientation = santa.orientation
        santa.move(distances[move])
        santa.turn(turns[move])
        monkey_map.update_path(last_position, [santa.x, santa.y], last_orientation)
    santa.move(distances[-1])
    line = santa.y + 1
    column = santa.x + 1
    orientation = santa.orientation
    return [[line, column, orientation], 1000 * line + 4 * column + TURN_COUNT[orientation]]


def run(data_dir, star):
    with open(f'{data_dir}/input-day22.txt', 'r') as fic:
        data = [x for x in fic.read().split('\n')[:-1]]
        data = [data[:data.index('')], data[-1]]

    if star == 1:  # The final answer is: # TODO: 189192, too high - 18512 too low - 76532 est faux
        solution = get_password(data)
    elif star == 2:  # The final answer is:
        solution = my_func(data)
    else:
        raise Exception('Star number must be either 1 or 2.')

    print(f'The solution (star {star}) is: {solution}')
    return solution
