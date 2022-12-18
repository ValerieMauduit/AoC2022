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


def get_external_surface(droplets):
    droplets.sort()
    for x in set([x[0] for x in droplets]):
        surface = get_surface()
    external_surface = 42
    return external_surface


def run(data_dir, star):
    with open(f'{data_dir}/input-day18.txt', 'r') as fic:
        data = [[int(y) for y in x.split(',')] for x in fic.read().split('\n')[:-1]]

    if star == 1:  # The final answer is: 3374
        solution = get_surface(data)
    elif star == 2:  # The final answer is:
        solution = my_func(data)
    else:
        raise Exception('Star number must be either 1 or 2.')

    print(f'The solution (star {star}) is: {solution}')
    return solution
