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


def get_geodes(blueprint):
    reserve = {'ore': 0, 'clay': 0, 'obs': 0, 'geo': 0}
    robots_ready = {'ore_robot': 0, 'clay_robot': 0, 'obs_robot': 0, 'geo_robot': 0}
    for time in range(25):
        print(f"Time: {time}")
        print(f"My robots are: {robots_ready}")
        print(f"My reserve is: {reserve}")
        # Find the best robots to create
        new_robots = {'ore_robot': 0, 'clay_robot': 0, 'obs_robot': 0, 'geo_robot': 0}
        # How many geo_robots to make?
        new_geo_robots = min([reserve[product] // blueprint['geo_robot'][product] for product in ['obs', 'ore']])
        new_robots['geo_robot'] += new_geo_robots
        reserve['obs'] -= new_geo_robots * blueprint['geo_robot']['obs']
        reserve['ore'] -= new_geo_robots * blueprint['geo_robot']['ore']
        # How many obs_robots to make?
        new_obs_robots = max([min(
            # possible to create
            [reserve[product] // blueprint['obs_robot'][product] for product in ['clay', 'ore']] +
            # interesting for the geo_robots
            [reserve['ore'] // blueprint['geo_robot']['ore'] * blueprint['geo_robot']['obs'] - reserve['obs']]
        ), 0])
        new_robots['obs_robot'] += new_obs_robots
        reserve['clay'] -= new_obs_robots * blueprint['obs_robot']['clay']
        reserve['ore'] -= new_obs_robots * blueprint['obs_robot']['ore']




        # est-ce que j'ai + besoin d'obs que d'ore pour faire des goe robots? faire le maxi de obs-rob nécessaire (dans la limite de ce que je peux faire)
        # même chose avec clay pour obs robot
        # compléter avec des ore robots
        # The robots collect their products
        for robot in robots_ready:
            reserve[robot.split('_')[0]] += robots_ready[robot]
        robots_ready = {robot: robots_ready[robot] + new_robots[robot] for robot in robots_ready}
    return reserve['geo']


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
