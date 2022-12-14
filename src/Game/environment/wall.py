import pygame
from src.config.globals import MAP_METER, MAP_SURFACE
from random import randint
from src.Game.environment.entity import Entity


class Wall(Entity):

    def __init__(self) -> None:
        super().__init__()
        self.rect: int
        self.width = randint(MAP_METER * 3, MAP_METER * 20)
        self.height = randint(MAP_METER * 3, MAP_METER * 20)

    def draw(self):
        pygame.draw.rect(
            MAP_SURFACE,
            (139, 69, 19),
            pygame.Rect(
                self.pos_x,
                self.pos_y,
                self.width,
                self.height
            ),
            border_radius=4
        )
