import pygame

from src.config.globals import MAP_SURFACE
from random import randint
from src.Game.environment.Entities.entity import Entity
from src.config.globals import WIDTH, HEIGHT


class Wall(Entity):
    def __init__(self) -> None:
        super().__init__()
        self.x, self.y = randint(0, WIDTH - 200), randint(0, HEIGHT - 200)
        self.active = True
        self.image = pygame.image.load(f"assets/entities/walls/wall_{randint(1, 4)}.png").convert_alpha()
        self.rect = pygame.rect.Rect(self.x, self.y, self.image.get_size()[0], self.image.get_size()[1])

    def draw(self):
        MAP_SURFACE.blit(self.image, (self.x, self.y))
        # pygame.draw.rect(MAP_SURFACE, (139, 69, 19), self.rect, border_radius=4)

    def collision_condition(self, points):
        return self.rect.clipline(points[0], points[1]) or self.rect.clipline(points[1], points[2])\
               or self.rect.clipline(points[2], points[3]) or self.rect.clipline(points[0], points[3])

    def get_effect(self, player):
        if self.active and self.collision_condition(player.car.hit_box):
            self.active = False
            return "wall"
        self.active = True
        return None
