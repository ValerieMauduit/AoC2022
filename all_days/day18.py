# Day 18: Boiling Boulders

# First star: You take a quick scan of a droplet as it flies past you (your puzzle input). Because of how quickly the
# lava is moving, the scan isn't very good; its resolution is quite low and, as a result, it approximates the shape of
# the lava droplet with 1x1x1 cubes on a 3D grid, each given as its x,y,z position.
# To approximate the surface area, count the number of sides of each cube that are not immediately connected to another
# cube. What is the surface area of your scanned lava droplet?

# Second star: Something seems off about your calculation. The cooling rate depends on exterior surface area, but your
# calculation also included the surface area of air pockets trapped in the lava droplet.
# Instead, consider only cube sides that could be reached by the water and steam as the lava droplet tumbles into the
# pond. The steam will expand to reach as much as possible, completely displacing any air on the outside of the lava
# droplet but never expanding diagonally. What is the exterior surface area of your scanned lava droplet?

def get_surface(droplets):
    taken = []
    surface = 0
    for droplet in droplets:
        surface += (
                6
                - 2 * ([droplet[0] + 1, droplet[1], droplet[2]] in taken)
                - 2 * ([droplet[0] - 1, droplet[1], droplet[2]] in taken)
                - 2 * ([droplet[0], droplet[1] + 1, droplet[2]] in taken)
                - 2 * ([droplet[0], droplet[1] - 1, droplet[2]] in taken)
                - 2 * ([droplet[0], droplet[1], droplet[2] + 1] in taken)
                - 2 * ([droplet[0], droplet[1], droplet[2] - 1] in taken)
        )
        taken += [droplet]
    return surface


def get_bubbles(droplets):
    bubbles = []
    for xb in range(min([n[0] for n in droplets]), max([n[0] for n in droplets]) + 1):
        for yb in range(min([n[1] for n in droplets]), max([n[1] for n in droplets]) + 1):
            for zb in range(min([n[2] for n in droplets]), max([n[2] for n in droplets]) + 1):
                if [xb, yb, zb] not in droplets:
                    xx = [d[0] for d in droplets if (d[2] == zb) & (d[1] == yb)]
                    yy = [d[1] for d in droplets if (d[0] == xb) & (d[2] == zb)]
                    zz = [d[2] for d in droplets if (d[0] == xb) & (d[1] == yb)]
                    if (
                            (len(xx) > 0) & (min(xx, default=10000) < xb) & (max(xx, default=-10000) > xb) &
                            (len(yy) > 0) & (min(yy, default=10000) < yb) & (max(yy, default=-10000) > yb) &
                            (len(zz) > 0) & (min(zz, default=10000) < zb) & (max(zz, default=-10000) > zb)
                    ):
                        xl = max([n for n in xx if n < xb])
                        xr = min([n for n in xx if n > xb])
                        yl = max([n for n in yy if n < yb])
                        yr = min([n for n in yy if n > yb])
                        zl = max([n for n in zz if n < zb])
                        zr = min([n for n in zz if n > zb])
                        test_xl = len(set([
                            f'{d[1]}, {d[2]}'
                            for d in droplets
                            if (d[1] > yl) & (d[1] < yr) & (d[2] > zl) & (d[2] < zr) & (d[0] < xb)
                        ])) == (zr - zl - 1) * (yr - yl - 1)
                        test_xr = len(set([
                            f'{d[1]}, {d[2]}'
                            for d in droplets
                            if (d[1] > yl) & (d[1] < yr) & (d[2] > zl) & (d[2] < zr) & (d[0] > xb)
                        ])) == (zr - zl - 1) * (yr - yl - 1)
                        test_yl = len(set([
                            f'{d[0]}, {d[2]}'
                            for d in droplets
                            if (d[0] > xl) & (d[0] < xr) & (d[2] > zl) & (d[2] < zr) & (d[1] < yb)
                        ])) == (xr - xl - 1) * (zr - zl - 1)
                        test_yr = len(set([
                            f'{d[0]}, {d[2]}'
                            for d in droplets
                            if (d[0] > xl) & (d[0] < xr) & (d[2] > zl) & (d[2] < zr) & (d[1] > yb)
                        ])) == (xr - xl - 1) * (zr - zl - 1)
                        test_zl = len(set([
                            f'{d[0]}, {d[1]}'
                            for d in droplets
                            if (d[0] > xl) & (d[0] < xr) & (d[1] > yl) & (d[1] < yr) & (d[2] < zb)
                        ])) == (xr - xl - 1) * (yr - yl - 1)
                        test_zr = len(set([
                            f'{d[0]}, {d[1]}'
                            for d in droplets
                            if (d[0] > xl) & (d[0] < xr) & (d[1] > yl) & (d[1] < yr) & (d[2] > zb)
                        ])) == (xr - xl - 1) * (yr - yl - 1)
                        if test_xl & test_xr & test_yl & test_yr & test_zl & test_zr:
                            bubbles += [[xb, yb, zb]]
    return bubbles


def get_external_surface(droplets):
    total_surface = get_surface(droplets)
    bubbles = get_bubbles(droplets)
    bubbles_surface = get_surface(bubbles)
    return [bubbles, total_surface - bubbles_surface]


def run(data_dir, star):
    with open(f'{data_dir}/input-day18.txt', 'r') as fic:
        data = [[int(y) for y in x.split(',')] for x in fic.read().split('\n')[:-1]]

    if star == 1:  # The final answer is: 3374
        solution = get_surface(data)
    elif star == 2:  # The final answer is: 1716 - too low
        solution = get_external_surface(data)
    else:
        raise Exception('Star number must be either 1 or 2.')

    print(f'The solution (star {star}) is: {solution}')
    return solution
