# Day 19: Not Enough Minerals

# First star: To collect the obsidian from the bottom of the pond, you'll need waterproof obsidian-collecting robots.
# Fortunately, there is an abundant amount of clay nearby that you can use to make them waterproof.
# In order to harvest the clay, you'll need special-purpose clay-collecting robots. To make any type of robot, you'll
# need ore, which is also plentiful but in the opposite direction from the clay.
# Collecting ore requires ore-collecting robots with big drills. Fortunately, you have exactly one ore-collecting robot
# in your pack that you can use to kickstart the whole operation.
# Each robot can collect 1 of its resource type per minute. It also takes one minute for the robot factory (also
# conveniently from your pack) to construct any type of robot, although it consumes the necessary resources available
# when construction begins.
# The robot factory has many blueprints (your puzzle input) you can choose from, but once you've configured it with a
# blueprint, you can't change it. You'll need to work out which blueprint is best. The robot factory's actual assortment
# of blueprints are provided one blueprint per line.
# The elephants are starting to look hungry, so you shouldn't take too long; you need to figure out which blueprint
# would maximize the number of opened geodes after 24 minutes by figuring out which robots to build and when to build
# them.
# Determine the quality level of each blueprint by multiplying that blueprint's ID number with the largest number of
# geodes that can be opened in 24 minutes using that blueprint. What do you get if you add up the quality level of all
# of the blueprints in your list?

# Second star: description

BLUEPRINTS = [
    {
        'ore_robot': {'ore': 3}, 'clay_robot': {'ore': 3}, 'obs_robot': {'ore': 3, 'clay': 19},
        'geo_robot': {'ore': 3, 'obs': 17}
    }, {
        'ore_robot': {'ore': 3}, 'clay_robot': {'ore': 4}, 'obs_robot': {'ore': 3, 'clay': 17},
        'geo_robot': {'ore': 3, 'obs': 8}
    }, {
        'ore_robot': {'ore': 2}, 'clay_robot': {'ore': 3}, 'obs_robot': {'ore': 3, 'clay': 16},
        'geo_robot': {'ore': 2, 'obs': 11}
    }, {
        'ore_robot': {'ore': 4}, 'clay_robot': {'ore': 4}, 'obs_robot': {'ore': 2, 'clay': 14},
        'geo_robot': {'ore': 4, 'obs': 15}
    }, {
        'ore_robot': {'ore': 4}, 'clay_robot': {'ore': 3}, 'obs_robot': {'ore': 2, 'clay': 17},
        'geo_robot': {'ore': 3, 'obs': 16}
    }, {
        'ore_robot': {'ore': 4}, 'clay_robot': {'ore': 3}, 'obs_robot': {'ore': 3, 'clay': 7},
        'geo_robot': {'ore': 2, 'obs': 7}
    }, {
        'ore_robot': {'ore': 4}, 'clay_robot': {'ore': 3}, 'obs_robot': {'ore': 4, 'clay': 19},
        'geo_robot': {'ore': 4, 'obs': 12}
    }, {
        'ore_robot': {'ore': 4}, 'clay_robot': {'ore': 4}, 'obs_robot': {'ore': 2, 'clay': 10},
        'geo_robot': {'ore': 3, 'obs': 14}
    }, {
        'ore_robot': {'ore': 4}, 'clay_robot': {'ore': 4}, 'obs_robot': {'ore': 4, 'clay': 8},
        'geo_robot': {'ore': 3, 'obs': 19}
    }, {
        'ore_robot': {'ore': 2}, 'clay_robot': {'ore': 3}, 'obs_robot': {'ore': 2, 'clay': 14},
        'geo_robot': {'ore': 3, 'obs': 20}
    }, {
        'ore_robot': {'ore': 4}, 'clay_robot': {'ore': 4}, 'obs_robot': {'ore': 2, 'clay': 11},
        'geo_robot': {'ore': 3, 'obs': 14}
    }, {
        'ore_robot': {'ore': 3}, 'clay_robot': {'ore': 4}, 'obs_robot': {'ore': 3, 'clay': 6},
        'geo_robot': {'ore': 4, 'obs': 11}
    }, {
        'ore_robot': {'ore': 4}, 'clay_robot': {'ore': 3}, 'obs_robot': {'ore': 4, 'clay': 20},
        'geo_robot': {'ore': 4, 'obs': 8}
    }, {''
        'ore_robot': {'ore': 3}, 'clay_robot': {'ore': 4}, 'obs_robot': {'ore': 3, 'clay': 19},
        'geo_robot': {'ore': 3, 'obs': 8}
        }, {
        'ore_robot': {'ore': 2}, 'clay_robot': {'ore': 4}, 'obs_robot': {'ore': 4, 'clay': 13},
        'geo_robot': {'ore': 3, 'obs': 11}
    }, {
        'ore_robot': {'ore': 4}, 'clay_robot': {'ore': 4}, 'obs_robot': {'ore': 2, 'clay': 17},
        'geo_robot': {'ore': 3, 'obs': 11}
    }, {
        'ore_robot': {'ore': 4}, 'clay_robot': {'ore': 3}, 'obs_robot': {'ore': 2, 'clay': 7},
        'geo_robot': {'ore': 3, 'obs': 8}
    }, {
        'ore_robot': {'ore': 2}, 'clay_robot': {'ore': 4}, 'obs_robot': {'ore': 4, 'clay': 15},
        'geo_robot': {'ore': 2, 'obs': 15}
    }, {
        'ore_robot': {'ore': 3}, 'clay_robot': {'ore': 4}, 'obs_robot': {'ore': 3, 'clay': 18},
        'geo_robot': {'ore': 4, 'obs': 16}
    }, {
        'ore_robot': {'ore': 4}, 'clay_robot': {'ore': 4}, 'obs_robot': {'ore': 3, 'clay': 5},
        'geo_robot': {'ore': 3, 'obs': 18}
    }, {
        'ore_robot': {'ore': 4}, 'clay_robot': {'ore': 3}, 'obs_robot': {'ore': 4, 'clay': 6},
        'geo_robot': {'ore': 3, 'obs': 11}
    }, {
        'ore_robot': {'ore': 4}, 'clay_robot': {'ore': 4}, 'obs_robot': {'ore': 3, 'clay': 19},
        'geo_robot': {'ore': 4, 'obs': 15}
    }, {
        'ore_robot': {'ore': 2}, 'clay_robot': {'ore': 3}, 'obs_robot': {'ore': 2, 'clay': 17},
        'geo_robot': {'ore': 3, 'obs': 19}
    }, {
        'ore_robot': {'ore': 4}, 'clay_robot': {'ore': 3}, 'obs_robot': {'ore': 3, 'clay': 18},
        'geo_robot': {'ore': 4, 'obs': 8}
    }, {
        'ore_robot': {'ore': 3}, 'clay_robot': {'ore': 4}, 'obs_robot': {'ore': 4, 'clay': 17},
        'geo_robot': {'ore': 4, 'obs': 16}
    }, {
        'ore_robot': {'ore': 2}, 'clay_robot': {'ore': 4}, 'obs_robot': {'ore': 3, 'clay': 17},
        'geo_robot': {'ore': 4, 'obs': 20}
    }, {
        'ore_robot': {'ore': 4}, 'clay_robot': {'ore': 3}, 'obs_robot': {'ore': 3, 'clay': 10},
        'geo_robot': {'ore': 3, 'obs': 10}
    }, {
        'ore_robot': {'ore': 4}, 'clay_robot': {'ore': 3}, 'obs_robot': {'ore': 2, 'clay': 10},
        'geo_robot': {'ore': 4, 'obs': 10}
    }, {
        'ore_robot': {'ore': 2}, 'clay_robot': {'ore': 3}, 'obs_robot': {'ore': 2, 'clay': 14},
        'geo_robot': {'ore': 3, 'obs': 8}
    }, {
        'ore_robot': {'ore': 4}, 'clay_robot': {'ore': 4}, 'obs_robot': {'ore': 2, 'clay': 11},
        'geo_robot': {'ore': 4, 'obs': 8}
    },
]


def get_geodes(blueprint, time, robots_pack, reserve=None, space=''):
    space += '  '
    if reserve is None:
        reserve = {'ore': 0, 'clay': 0, 'obs': 0, 'geo': 0}
    if time == 24:
        print(f"{space}Times up. Geodes: {reserve['geo']}")
        return reserve['geo']
    print(f"{space}Time: {time}")
    print(f"{space}My robots are: {robots_pack}")
    print(f"{space}My reserve is: {reserve}")
    # Are you able to build some robots?
    # TODO: list of new possible robots
    possible_robots = [{'ore_robot': 0, 'clay_robot': 1, 'obs_robot': 0, 'geo_robot': 0}]
    possible_robots = []


    for n in range(len(possible_robots)):
        for robot in possible_robots[n]:
            possible_robots[n][robot] += robots_pack[robot]
    # The robots collect their products
    for robot in robots_pack:
        reserve[robot.split('_')[0]] += robots_pack[robot]
    return max([geodes for robots in possible_robots for geodes in get_geodes(blueprint, time + 1, robots, reserve)])


def quality_level(data):
    for blueprint in data:
        max_geodes = get_geodes(blueprint, 0, {'ore_robot': 1})
    return data


def run(data_dir, star):
    data = BLUEPRINTS

    if star == 1:  # The final answer is:
        solution = my_func(data)
    elif star == 2:  # The final answer is:
        solution = my_func(data)
    else:
        raise Exception('Star number must be either 1 or 2.')

    print(f'The solution (star {star}) is: {solution}')
    return solution
