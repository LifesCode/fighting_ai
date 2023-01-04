from math import sin, cos
from src.config.globals import MAP_SURFACE
from src.config.car import SIZE
from src.Game.environment.Entities.entity import Entity
import pygame


class Bullet(Entity):
    def __init__(self, center: (int, int), angle: float, owner: str, size=3, speed=3000):
        super().__init__()
        self.active = True
        self.x, self.y = center[0], center[1]
        self.size = size
        self.owner = owner
        self.speed_x = speed*sin(angle)
        self.speed_y = speed*cos(angle)
        self.rect = pygame.rect.Rect(self.x, self.y, self.size, self.size)

    def update(self, dt):
        self.x += self.speed_x*dt
        self.y += self.speed_y*dt
        self.rect = pygame.rect.Rect(self.x, self.y, self.size, self.size)
        return self.active

    def collision_condition(self, car):
        return (self.x - car.x)**2 + (self.y - car.y)**2 < SIZE[0]**2

    def get_effect(self, player):
        if player.name != self.owner and self.active and self.collision_condition(player.car):
            self.active = False
            return "bullet"
        return None

    def draw(self):
        pygame.draw.circle(MAP_SURFACE, (255, 255, 0), (self.x, self.y), self.size)
