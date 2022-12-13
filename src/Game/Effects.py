import pygame.draw
from random import choice, randrange
import math


class Particle:
    def __init__(self, position, existence_radius):
        self.position = self.calculate_position(position, existence_radius)
        self.radius = choice(range(0, 14, 2))
        self.color = choice([(255, 0, 0), (255, 255, 0), (220, 100, 0)])
        self.radius = choice([10, 8, 6, 4, 2])
        self.width = randrange(1, 3)

    @staticmethod
    def calculate_position(position, existence_radius):
        angle = randrange(90)
        x = position[0] + randrange(existence_radius) * math.sin(angle) * choice([-1, 1])
        y = position[1] + randrange(existence_radius) * math.cos(angle) * choice([-1, 1])
        return x, y

    def draw(self, screen, position, existance_radius):
        pygame.draw.circle(screen, self.color, self.position, self.radius, self.width)
        self.radius = (self.radius + 1) % 10
        if self.radius == 0:
            self.position = self.calculate_position(position, existance_radius)


class FireEffect:
    def __init__(self, particles_number, position):
        self.particles = [Particle(position, 100) for _ in range(particles_number)]

    """def calculate_positions(self, number, position):
        positions = []
        for x in range(number + 1):
            x = math.cos(2 * 3.1415 / number * x)*100 + position[0]
            y = math.sin(2 * 3.1415 / number * x)*100 + position[1]
            positions.append((x, y))
        return positions"""

    def draw(self, screen, position):
        [particle.draw(screen, position, 100) for particle in self.particles]
