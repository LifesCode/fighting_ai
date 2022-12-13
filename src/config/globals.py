import pygame


pygame.init()

MAX_LIFE = 100
MAX_ENERGY = 100
BARS_POSITIONS = {"x": 50, "y": 40}
BORDER_RADIUS = 8
WIDTH, HEIGHT = 1280, 820
BG_COLOR = (0, 0, 0)  # default is (0, 150, 150)
GAME_SURFACE = pygame.Surface((WIDTH, HEIGHT))
GAME_SURFACE.fill(BG_COLOR)  # set screen with background color
FPS = 1
CLOCK = pygame.time.Clock()
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
