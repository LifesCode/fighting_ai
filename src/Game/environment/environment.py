from src.config.globals import BORDER_RADIUS, MAP_SURFACE, MAP_SURFACE_SIZE, MAP_SURFACE_POS, MAP_METER, ENTITIES, SCREEN
from src.Game.environment.wall import Wall
import pygame


class Environment:

    def __init__(self):
        self.border_display_adjust = 3
        self.map_list: list
        self.make_map_list()
        # self.show_map()

        self.environment_objects = {
            "0": lambda pos_x, pos_y: None,
            "1": self.draw_block
        }
        [ENTITIES.append(Wall()) for _ in range(5)]

    def make_map_list(self):
        self.map_list = []

    def draw_map(self):
        x = 0
        y = 0
        for row in self.map_list:
            for colum in row:
                self.environment_objects[colum](x, y)
                # pygame.draw.rect(
                #     surface=MAP_SURFACE,
                #     color=(255, 255, 255),
                #     rect=(
                #         x,
                #         y,
                #         MAP_METER,
                #         MAP_METER
                #     ),
                #     width=2
                # )
                x += MAP_METER
            x = 0
            y += MAP_METER

    # def show_map(self):
    #     for line in self.map_list:
    #         print(line)

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
        self.draw_map()
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
