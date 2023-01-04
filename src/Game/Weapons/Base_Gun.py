from math import sin, cos
from src.config.globals import MAP_SURFACE, ENTITIES
from src.Game.environment.Entities.Bullet import Bullet
import pygame


class BaseGun:
    def __init__(self, center, size=10, angle=0):
        self.center = center
        self.size = size
        self.angle = None
        self.x_end, self.y_end = None, None
        self.bullets_shot = []
        self.update(0, [center, angle])

    def shoot(self, angle, owner):
        new_bullet = Bullet(self.center, angle, owner)
        ENTITIES.append(new_bullet)
        self.bullets_shot.append(new_bullet)
        print(len(self.bullets_shot))

    def update(self, dt, info):
        # updating where the gun is located
        self.center, self.angle = info[0], info[1]
        # updating where the gun is pointing at
        self.x_end, self.y_end = self.center[0] + sin(self.angle)*self.size, self.center[1] + self.size*cos(self.angle)
        # updating bullets
        for i, bullet in enumerate(self.bullets_shot):
            if bullet.active:
                bullet.update(dt)
            else:
                ENTITIES.pop(ENTITIES.index(bullet))
                self.bullets_shot.pop(i)

    def draw(self):
        pygame.draw.line(MAP_SURFACE, (0, 0, 0), self.center, (self.x_end, self.y_end), 2)