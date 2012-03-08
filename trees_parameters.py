# -----------------------------------------------------------------------------------------------------------------
# proof-of-concept dynamic object oriented tree generator 
# for terasology project
# written by cynthia kurtz
# -----------------------------------------------------------------------------------------------------------------

INDENT = '    '
DIRECTIONS = ["north", "east", "south", "west", "up", "down"]

SIZE_OF_SPACE_XY = 100
SIZE_OF_SPACE_Z = 200
GROUND_LEVEL = 100

PATCHY_SUN = True

PATCHY_WATER = True
NUM_WATER_PATCHES = 10
WATER_PATCH_RADIUS = 5

PATCHY_MINERALS = True
NUM_MINERAL_PATCHES = 10
MINERAL_PATCH_RADIUS = 5

# for all parameters that impact both stems and roots, the first in the list is stems, the second is roots

# MERISTEMS - BIOMASS, WATER, NUTRIENTS
START_MERISTEM_BIOMASS = [3, 3]
BIOMASS_TO_MAKE_ONE_PHYTOMER = [10, 15]
BIOMASS_USED_BY_MERISTEM_PER_DAY = [0.1, 0.1]
MERISTEM_DIES_IF_BIOMASS_GOES_BELOW = [0.5, 0.5]

START_MERISTEM_WATER = [1, 1]
WATER_TO_MAKE_ONE_PHYTOMER = [5, 5]
WATER_USED_BY_MERISTEM_PER_DAY = [0.1, 0.1]
DEATH_WATER_MERISTEM = [0.5, 0.5]

START_MERISTEM_MINERALS = [1, 1]
MINERALS_TO_MAKE_ONE_PHYTOMER = [5, 5]
MINERALS_USED_BY_MERISTEM_PER_DAY = [0.1, 0.1]
DEATH_MINERALS_MERISTEM = [0.5, 0.5]

# MERISTEMS - BRANCHING
AXILLARY_MERISTEMS_PER_INTERNODE = [2,2]
BRANCHING_PROBABILITY = [0.4, 0.6]
APICAL_DOMINANCE_EXTENDS_FOR = [5, 3]
MAX_NUM_INTERNODES_ON_PLANT_EVER = [50, 50] # this is a check on all the other parameters blowing up into a giant plant

# MERISTEMS - DRAWING
COLOR_MERISTEM = ["#7CFC00", "#000000"]
COLOR_MERISTEM_DEAD = ["#8B8B83", "#000000"]

# INTERNODES - BIOMASS, WATER, NUTRIENTS
START_INTERNODE_BIOMASS = [1, 1]
OPTIMAL_INTERNODE_BIOMASS = [6, 4]
BIOMASS_USED_BY_INTERNODE_PER_DAY = [0.2, 0.2]
INTERNODE_DIES_IF_BIOMASS_GOES_BELOW = [0.01, 0.01]
INTERNODES_SEEK_RADIUS = [2, 4]

BIOMASS_DISTRIBUTION_SPREAD_PERCENT = [60, 60]
BIOMASS_DISTRIBUTION_ORDER = [
							["root", "leafClusters",'branches', 'axillary meristems', "apical meristems", "child"],
							["above-ground plant", 'branches', 'axillary meristems', "apical meristems", "child"],
							]

START_INTERNODE_WATER = [1, 1]
OPTIMAL_INTERNODE_WATER = [6, 4]
WATER_USED_BY_INTERNODE_PER_DAY = [0.2, 0.2]
INTERNODE_DIES_IF_WATER_GOES_BELOW = [0.01, 0.01]

WATER_DISTRIBUTION_SPREAD_PERCENT = [60, 60]
WATER_DISTRIBUTION_ORDER = [
							["root", "leafClusters",'branches', 'axillary meristems', "apical meristems", "child"],
							["above-ground plant", 'branches', 'axillary meristems', "apical meristems", "child"],
							]

START_INTERNODE_MINERALS = [1, 1]
OPTIMAL_INTERNODE_MINERALS = [6, 4]
MINERALS_USED_BY_INTERNODE_PER_DAY = [0.2, 0.2]
INTERNODE_DIES_IF_MINERALS_GOES_BELOW = [0.01, 0.01]

MINERALS_DISTRIBUTION_SPREAD_PERCENT = [60, 60]
MINERALS_DISTRIBUTION_ORDER = [
							["root", "leafClusters",'branches', 'axillary meristems', "apical meristems", "child"],
							["above-ground plant", 'branches', 'axillary meristems', "apical meristems", "child"],
							]

# INTERNODES - PHOTOSYNTHESIS
BIOMASS_MADE_BY_FULL_SIZED_NON_WOODY_INTERNODE_PER_DAY_WITH_FULL_SUN = 2 # root not needed
INTERNODES_TURN_WOODY_AFTER_THIS_MANY_DAYS = 8 # root not needed

# INTERNODES - DRAWING
INTERNODE_LENGTH_AT_CREATION = [3, 2] # no less than 3, to have room for buds and leafClusters
INTERNODE_LENGTH_AT_FULL_SIZE = [12, 6]
INTERNODE_WIDTH_AT_CREATION = [1, 1]
INTERNODE_WIDTH_AT_FULL_SIZE = [3, 3]
ANGLE_BETWEEN_STEM_AND_BRANCH_OFF_TRUNK = [40, 40]
ANGLE_BETWEEN_STEM_AND_BRANCH_NOT_OFF_TRUNK = [20, 20]
RANDOM_INTERNODE_SWAY = [30, 10]
COLOR_INTERNODE_WOODY = "#CC7F32" # root not needed
COLOR_INTERNODE_NONWOODY = ["#8B7500", "#000000"]
COLOR_INTERNODE_DEAD = ["#292421", "#000000"]

# LEAF CLUSTERS - BIOMASS, WATER, NUTRIENTS
START_LEAF_CLUSTER_BIOMASS = 1
OPTIMAL_LEAF_CLUSTER_BIOMASS = 8
BIOMASS_USED_BY_LEAF_CLUSTER_PER_DAY = 0.5
DEATH_BIOMASS_LEAF_CLUSTER = 0.1

START_LEAF_CLUSTER_WATER = [1, 1]
OPTIMAL_LEAF_CLUSTER_WATER = [6, 4]
WATER_USED_BY_LEAF_CLUSTER_PER_DAY = [0.2, 0.2]
LEAF_CLUSTER_DIES_IF_WATER_GOES_BELOW = [0.01, 0.01]

START_LEAF_CLUSTER_MINERALS = [1, 1]
OPTIMAL_LEAF_CLUSTER_MINERALS = [6, 4]
MINERALS_USED_BY_LEAF_CLUSTER_PER_DAY = [0.2, 0.2]
LEAF_CLUSTER_DIES_IF_MINERALS_GOES_BELOW = [0.01, 0.01]

# LEAF CLUSTERS - PHOTOSYNTHESIS
BIOMASS_MADE_BY_FULL_SIZED_LEAF_CLUSTER_PER_DAY_OF_PHOTOSYNTHESIS_WITH_FULL_SUN = 10
SHADE_TOLERANCE = 10

# LEAF CLUSTERS - DRAWING
LEAF_CLUSTER_LENGTH_AT_FULL_SIZE = 6
LEAF_CLUSTER_LENGTH_AT_CREATION = 1
LEAF_CLUSTER_ANGLE_WITH_STEM = 40
LEAF_CLUSTER_SHAPE_ANGLE = 30
RANDOM_LEAF_CLUSTER_SWAY = 20
LEAF_CLUSTER_SHAPE_PATTERN = "1122"
COLOR_LEAF_CLUSTER = "#488214"
COLOR_LEAF_CLUSTER_DEAD = "#5E2605"


