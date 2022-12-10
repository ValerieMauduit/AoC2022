# Day 10: Cathode-Ray Tube

# First star: It seems to be some kind of cathode-ray tube screen and simple CPU that are both driven by a precise clock
# circuit. The clock circuit ticks at a constant rate; each tick is called a cycle.
# Start by figuring out the signal being sent by the CPU. The CPU has a single register, X, which starts with the value
# 1. It supports only two instructions:
# - addx V takes two cycles to complete. After two cycles, the X register is increased by the value V. (V can be
#   negative.)
# - noop takes one cycle to complete. It has no other effect.
# The CPU uses these instructions in a program.
# Maybe you can learn something by looking at the value of the X register throughout execution. For now, consider the
# signal strength (the cycle number multiplied by the value of the X register) during the 20th cycle and every 40 cycles
# after that (that is, during the 20th, 60th, 100th, 140th, 180th, and 220th cycles). Find them. What is the sum of
# these six signal strengths?

# Second star: It seems like the X register controls the horizontal position of a sprite. Specifically, the sprite is 3
# pixels wide, and the X register sets the horizontal position of the middle of that sprite. (In this system, there is
# no such thing as "vertical position": if the sprite's horizontal position puts its pixels where the CRT is currently
# drawing, then those pixels will be drawn.)
# You count the pixels on the CRT: 40 wide and 6 high. This CRT screen draws the top row of pixels left-to-right, then
# the row below that, and so on. The left-most pixel in each row is in position 0, and the right-most pixel in each row
# is in position 39.
# Like the CPU, the CRT is tied closely to the clock circuit: the CRT draws a single pixel during each cycle.
# So, by carefully timing the CPU instructions and the CRT drawing operations, you should be able to determine whether
# the sprite is visible the instant each pixel is drawn. If the sprite is positioned such that one of its three pixels
# is the pixel currently being drawn, the screen produces a lit pixel (#); otherwise, the screen leaves the pixel dark
# (.).
# Render the image given by your program. What eight capital letters appear on your CRT?

def render_image(data):
    pixel_positions = run_cathode_tube(data)
    current_crt_row = ''
    for cycle in range(1, len(pixel_positions)):
        sprite_middle = pixel_positions[cycle][1] % 40
        sprite = [sprite_middle - 1, sprite_middle, sprite_middle + 1]
        # print(f"Sprite position: {''.join(['#' if n in sprite else '.' for n in range(40)])}")
        # print(f"During cycle  {cycle}: CRT draws pixel in position {cycle - 1}")
        if (cycle - 1) % 40 in sprite:
            current_crt_row += '#'
        else:
            current_crt_row += '.'
        # input(f"Current CRT row: {current_crt_row}")
    screen = [current_crt_row[(x * 40):((x + 1) * 40)] for x in range(6)]
    for line in screen:
        print(line)
    return screen


def run_cathode_tube(data):
    cycle, X = 0, 1
    signal = [(cycle, X)]
    for instruction in data:
        if instruction == 'noop':
            cycle += 1
            signal += [( cycle, X)]
        else:
            cycle += 1
            signal += [(cycle, X)]
            cycle += 1
            signal += [(cycle, X)]
            X += int(instruction[5:])
    return signal


def cathode_tube_scores(data):
    signal = run_cathode_tube(data)
    main_steps = [cycle[0] * cycle[1] for cycle in [signal[index] for index in [20, 60, 100, 140, 180, 220]]]
    return [main_steps, sum(main_steps)]


def run(data_dir, star):
    with open(f'{data_dir}/input-day10.txt', 'r') as fic:
        data = [x for x in fic.read().split('\n')[:-1]]

    if star == 1:  # The final answer is: 13680
        solution = cathode_tube_scores(data)
    elif star == 2:  # The final answer is: PZGPKPEB *BUT* actually my first column is not correct with the real dataset
        solution = render_image(data)
    else:
        raise Exception('Star number must be either 1 or 2.')

    print(f'The solution (star {star}) is: {solution}')
    return solution
