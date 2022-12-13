import pygame


pygame.init()

MAX_LIFE = 100
MAX_ENERGY = 100
BARS_POSITIONS = {"x": 50, "y": 40}
BORDER_RADIUS = 8
WIDTH, HEIGHT = 1080, 720
MAP_SURFACE_SIZE = (WIDTH-120, HEIGHT-180)
MAP_SURFACE_POS = (
    WIDTH / 2 - MAP_SURFACE_SIZE[0] / 2, 
    (HEIGHT / 2 - MAP_SURFACE_SIZE[1] / 2) + 60
)
MAP_SURFACE = pygame.Surface(MAP_SURFACE_SIZE)
FPS = 1
CLOCK = pygame.time.Clock()
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
