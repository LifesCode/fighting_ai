from src.Game.Animations import player_animations
from src.Game.Effects import FireEffect
from src.config.globals import SCREEN, WIDTH
from math import cos, sin, pi
import pygame


class Player:
    frame_module = {"run": 10}
    player_states = ("run",)
    animations = player_animations(player_states, frame_module)

    def __init__(self, ai, num):
        self.AI = ai
        self.frame = 0
        self.state = "run"
        self.x = 500
        self.y = 200
        self.speed = 20
        self.effect = FireEffect(200, (self.x+240, self.y+50))

    def update(self, dt):
        self.frame = (self.frame+1) % self.frame_module[self.state]
        self.x = (self.x + self.speed) % WIDTH

    def update_state(self, new_state):
        self.frame = 0
        self.state = new_state

    def draw(self):
        # self.HUD.draw(SCREEN)
        SCREEN.blit(self.animations[self.state][self.frame], (self.x, self.y))
        self.effect.draw(SCREEN, [self.x+100, self.y])


class Car:
    original_image = pygame.image.load("assets/players/cars/car.png").convert_alpha()

    def __init__(self, x, y, angle=0.0, max_acceleration=5.0):
        self.x = 200
        self.y = 200
        self.radius = 50

        self.angle = 0
        self.linear_speed = 0  # a speed in pixels per second
        self.angular_speed = 10  # 0.0872638  # a speed in radians equivalent to 15 degrees/second
        self.steering_direction = 0

        self.max_l_speed = 1000  # max speed a car can move
        self.keep_steering = False  # current steering state
        self.keep_speeding = False  # keep speeding up status
        self.size = (self.original_image.get_size()[0], self.original_image.get_size()[1])
        self.image = pygame.transform.rotate(self.original_image, angle)
        self.center = (self.x+self.size[0], self.y+self.size[1])
        self.rect = self.image.get_rect()

        self.direction = 0
        self.brake = 0
        self.resistence = self.max_l_speed*0.25  # acceleration added to the car when no acceleration is added
        self.acceleration = self.max_l_speed*2+self.resistence  # current car acceleration
        self.brake_force = self.acceleration*0.9  # acceleration added to the car when steering

    def steer(self, dt):  # clockwise: direction=1  | counterclockwise: dir = -1 | no change: dir = 0
        self.angle = (self.angle+self.steering_direction*self.angular_speed*dt)  # % 2*pi

    def speed_up(self, dt):
        a = self.direction*self.acceleration  # acceleration
        movement_modulo = ((self.linear_speed > 0) - (self.linear_speed < 0))  # direction of the brakes (1/-1)
        r = movement_modulo*self.resistence + movement_modulo*self.brake*self.brake_force
        updated_speed = self.linear_speed + (a - r)*dt  # V = V0 + (a - resistance)*t
        self.linear_speed = min(self.max_l_speed, max(-self.max_l_speed, updated_speed))

    def activate_speeding(self, direction, speeding_state=True):
        self.keep_speeding = speeding_state
        self.direction = direction

    def activate_steering(self, direction, steering_state=True):
        self.keep_steering = steering_state
        self.steering_direction = direction

    def activate_brakes(self, state=1):
        self.brake = state

    def update(self, dt):
        self.inertia_direction = -self.linear_speed/self.linear_speed if self.linear_speed else 0
        self.steer(dt)
        self.speed_up(dt)
        self.x += self.linear_speed*sin(self.angle)*dt
        self.y += self.linear_speed*cos(self.angle)*dt
        self.update_image()

    def draw(self):
        # pygame.draw.circle(SCREEN, (22, 200, 250), self.center, self.radius, 15)
        SCREEN.blit(self.image, self.rect)

    def update_image(self):
        # offset from pivot to center
        image_rect = self.image.get_rect(topleft=(self.x - self.size[0]/2, self.y - self.size[1]/2))
        offset_center_to_pivot = pygame.math.Vector2((self.x, self.y)) - image_rect.center
        rotated_offset = offset_center_to_pivot.rotate(-self.angle)

        # rotated image center
        self.center = (self.x - rotated_offset.x/2, self.y - rotated_offset.y/2)

        # get a rotated image
        self.image = pygame.transform.rotate(self.original_image, self.angle*180/pi)
        self.rect = self.image.get_rect(center=self.center)


class Bullet:
    def __init__(self, center, angle, size=5, speed=1000):
        self.center = list(center)
        self.size = size
        self.speed_x = speed*sin(angle)
        self.speed_y = speed*cos(angle)

    def update(self, dt):
        self.center[0] += self.speed_x*dt
        self.center[1] += self.speed_y*dt

    def draw(self):
        pygame.draw.circle(SCREEN, (0, 0, 0), self.center, self.size, 5)


class BaseGun:
    def __init__(self, center, size=50, angle=0):
        self.center = center
        self.size = size
        self.angle = None
        self.x_end, self.y_end = None, None
        self.bullets = []
        self.update(0, [center, angle])

    def shoot(self, angle):
        self.bullets.append(Bullet(self.center, angle))

    def update(self, dt, info):
        self.center, self.angle = info[0], info[1]
        self.x_end, self.y_end = self.center[0] + sin(self.angle)*self.size, self.center[1] + self.size*cos(self.angle)
        [bullet.update(dt) for bullet in self.bullets]

    def draw(self):
        pygame.draw.line(SCREEN, (0, 0, 0), self.center, (self.x_end, self.y_end), 6)
        [bullet.draw(SCREEN) for bullet in self.bullets]


class CarPlayer(Player):
    def __init__(self, ai, num):
        super().__init__(ai, num)
        self.car = Car(200, 200)
        self.gun = BaseGun(self.car.center, angle=self.car.angle)
        self.image = pygame.image.load("assets/players/cars/car.png").convert_alpha()

    def update(self, dt):
        self.car.update(dt)
        self.gun.update(dt, [self.car.center, self.car.angle])

    def shoot(self):
        self.gun.shoot(self.car.angle)

    def draw(self):
        self.car.draw()
        self.gun.draw()
        # self.weapon.draw(SCREEN)
