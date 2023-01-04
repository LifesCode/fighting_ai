import pygame

pygame.init()

# SCREEN ---------------------------------------------------------------------------------------------------------------
WIDTH, HEIGHT = 1080, 720  # Width and height of the screen
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
MAP_SURFACE_SIZE = (WIDTH-120, HEIGHT-160)  # Width and height of the environment
# position of the environment relative to the screen
MAP_SURFACE_POS = (WIDTH / 2 - MAP_SURFACE_SIZE[0] / 2, (HEIGHT / 2 - MAP_SURFACE_SIZE[1] / 2) + 60)
MAP_SURFACE = pygame.Surface(MAP_SURFACE_SIZE)  # environment surface

# GAME -----------------------------------------------------------------------------------------------------------------
ENTITIES = []
MAP_METER = 10  # pixel equivalent of a meter in the environment
FPS = 1000  # frame rate
CLOCK = pygame.time.Clock()

# WALL ENTITY ----------------------------------------------------------------------------------------------------------
SHOCK_ABSORPTION_COEFFICIENT = 0.25  # percentage of remaining speed when a car hits a wall
MIN_WALL_NUMBER = 7  # Min Number of walls that can be generated for a map
MAX_WALL_NUMBER = 11  # Max Number of walls that can be generated for a map
WALL_HIT_DAMAGE = 0.1  # percentage of damage a car receives for hitting a wall at maximum speed
# WALL_CONTACT_DAMAGE = 0.001  # percentage of damage a car receives at each frame from being in contact with a wall

# HUD ------------------------------------------------------------------------------------------------------------------
BARS_POSITIONS = {"x": 50, "y": 40}  # coordinates of hud bars display
BORDER_RADIUS = 8   # border radius of the hud bars

# WEAPONS --------------------------------------------------------------------------------------------------------------
BULLET_ENERGY_RECOVERY = 0.05
BULLET_DAMAGE = 0.03
