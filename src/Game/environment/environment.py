from src.config.globals import BORDER_RADIUS, MAP_SURFACE, MAP_SURFACE_SIZE,\
    MAP_SURFACE_POS, MAP_METER, ENTITIES, SCREEN, MIN_WALL_NUMBER, MAX_WALL_NUMBER
from src.Game.environment.Entities.wall import Wall
import pygame
from random import randint


class Environment:

    def __init__(self):
        self.border_display_adjust = 3
        self.map_list = []

        self.environment_objects = {
            "0": lambda pos_x, pos_y: None,
            "1": self.draw_block
        }
        [ENTITIES.append(Wall()) for _ in range(randint(MIN_WALL_NUMBER, MAX_WALL_NUMBER))]

    def draw(self):
        pygame.draw.rect(
            surface=SCREEN,
            color=(139, 69, 19),
            rect=(
                MAP_SURFACE_POS[0] - self.border_display_adjust,
                MAP_SURFACE_POS[1] - self.border_display_adjust,
                MAP_SURFACE_SIZE[0] + self.border_display_adjust * 2,
                MAP_SURFACE_SIZE[1] + self.border_display_adjust * 2
            ),
            width=6,
            border_radius=BORDER_RADIUS + 6
        )
        [entity.draw() for entity in ENTITIES]

    def draw_block(self, pos_x, pos_y):
        pygame.draw.rect(
            surface=MAP_SURFACE,
            color=(139, 69, 19),
            rect=(
                pos_x,
                pos_y,
                MAP_METER,
                MAP_METER
            ),
            border_radius=5
        )
