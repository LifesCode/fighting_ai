import pygame

# CAR ------------------------------------------------------------------------------------------------------------------
MAX_LIFE = 100  # maximum amount of health a car can have
MAX_ENERGY = 100  # maximum amount of energy a car can have
MAX_LINEAR_SPEED = 700  # maximum speed of the car
IMAGE = pygame.image.load("assets/players/cars/car_1.png").convert_alpha()  # image of the car
RESISTENCE = MAX_LINEAR_SPEED * 0.25  # acceleration added to the car when no acceleration is added
ACCELERATION = MAX_LINEAR_SPEED * 2 + RESISTENCE  # current car acceleration
BRAKE_FORCE = ACCELERATION * 0.9  # acceleration added to the car when steering
SIZE = IMAGE.get_size()
ANGULAR_SPEED: int = 6  # speed at which the car rotates expressed in degrees/second
