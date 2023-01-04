from src.Game.Player.Player import Player
from src.Game.HUD.HUD import HUD
from src.Game.Weapons.Base_Gun import BaseGun
from src.config.globals import MAP_SURFACE, WIDTH, HEIGHT
from src.config.car import *
from math import cos, sin, pi
import pygame
from random import randint


class Car:
    # original_image = pygame.transform.scale(original_image, (26, 41))
    def __init__(self, x=randint(0, WIDTH), y=randint(0, HEIGHT), angle=0.0):
        self.x = x
        self.y = y
        self.radius = 23
        self.angle = 0
        self.image = pygame.transform.rotate(IMAGE, angle)
        self.rect = self.image.get_rect()
        self.center = (self.x + SIZE[0], self.y + SIZE[1])
        self.hit_box = []

        self.linear_speed = 0  # a speed in pixels per second
        self.steering_direction: int = 0
        self.direction: int = 0  # 1: forward; -1: backwards; 0: no movement
        self.brake: int = 0  # if braking is activated it is set to 1 and makes the car brake (stop)

        self.keep_steering = False  # current steering state. Keeps steering in the steering direction if True
        self.keep_speeding = False  # keep speeding up status. Keeps speeding up in the current direction if True

    def steer(self, dt):  # clockwise: direction=1  | counterclockwise: dir = -1 | no change: dir = 0
        self.angle = (self.angle + self.steering_direction * ANGULAR_SPEED * dt)  # % 2*pi

    def speed_up(self, dt):
        a = self.direction * ACCELERATION  # acceleration
        movement_modulo = ((self.linear_speed > 0) - (self.linear_speed < 0))  # direction of the brakes (1/-1)
        r = movement_modulo * RESISTENCE + movement_modulo * self.brake * BRAKE_FORCE
        updated_speed = self.linear_speed + (a - r) * dt  # V = V0 + (a - resistance)*t
        self.linear_speed = min(MAX_LINEAR_SPEED, max(-MAX_LINEAR_SPEED, updated_speed))

    def activate_speeding(self, direction, speeding_state=True):
        self.keep_speeding = speeding_state
        self.direction = direction

    def activate_steering(self, direction, steering_state=True):
        self.keep_steering = steering_state
        self.steering_direction = direction

    def activate_brakes(self, state=1):
        self.brake = state

    def update_hit_box(self):
        rect = IMAGE.get_rect(center=self.center)
        pivot = pygame.math.Vector2(self.center)
        angle = -self.angle * 180 / pi
        self.hit_box = [(pygame.math.Vector2(rect.topleft) - pivot).rotate(angle) + pivot,
                        (pygame.math.Vector2(rect.topright) - pivot).rotate(angle) + pivot,
                        (pygame.math.Vector2(rect.bottomright) - pivot).rotate(angle) + pivot,
                        (pygame.math.Vector2(rect.bottomleft) - pivot).rotate(angle) + pivot]

    def update(self, dt):
        self.steer(dt)
        self.speed_up(dt)
        self.x += self.linear_speed * sin(self.angle) * dt
        self.y += self.linear_speed * cos(self.angle) * dt
        self.update_image()
        self.update_hit_box()

    def draw(self):
        # pygame.draw.circle(MAP_SURFACE, (22, 200, 250), self.center, self.radius, 1)
        pygame.draw.lines(MAP_SURFACE, (255, 255, 0), True, self.hit_box, 1)  # hit-box of the car
        MAP_SURFACE.blit(self.image, self.rect)

    def update_image(self):
        # offset from pivot to center
        image_rect = self.image.get_rect(topleft=(self.x - SIZE[0] / 2, self.y - SIZE[1] / 2))
        offset_center_to_pivot = pygame.math.Vector2((self.x, self.y)) - image_rect.center
        rotated_offset = offset_center_to_pivot.rotate(-self.angle)

        # rotated image center
        self.center = (self.x - rotated_offset.x / 2, self.y - rotated_offset.y / 2)

        # get a rotated image
        self.image = pygame.transform.rotate(IMAGE, self.angle * 180 / pi)
        self.rect = self.image.get_rect(center=self.center)


class CarPlayer(Player):
    def __init__(self, ai, name):
        super().__init__(ai, name)
        self.hud = HUD(name)
        self.car = Car(200, 200)
        self.gun = BaseGun(self.car.center, angle=self.car.angle)
        self.is_alive = lambda: self.hud.life > 0
        self.car.update(0)

    def update(self, dt):
        self.car.update(dt)
        self.gun.update(dt, [self.car.center, self.car.angle])

    def shoot(self):
        self.gun.shoot(self.car.angle, self.name)

    def draw(self):
        self.hud.draw()
        self.car.draw()
        self.gun.draw()
        #  self.weapon.draw(MAP_SURFACE)
