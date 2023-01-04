from src.config.globals import SHOCK_ABSORPTION_COEFFICIENT as SAC, WALL_HIT_DAMAGE as WHD
from src.config.globals import BULLET_ENERGY_RECOVERY as BER, BULLET_DAMAGE as BD
from src.config.car import MAX_LINEAR_SPEED
from src.Game.Player.Car_Player import CarPlayer as CarP
from src.Game.environment.Entities.Bullet import Bullet
from math import sin, cos


def do_nothing(protagonist=None, other_player=None, entity=None):
    pass


def wall_effect(protagonist: CarP, other_player=None, entity=None):
    # WHD/max_speed = damage/speed
    protagonist.hud.execute_life_actions("damage", WHD*abs(protagonist.car.linear_speed)/MAX_LINEAR_SPEED)
    # the car is thrown in the opposite direction of the impact but with lower speed
    protagonist.car.linear_speed *= -SAC
    # make car immediately distance himself from wall
    protagonist.car.x += protagonist.car.linear_speed * sin(protagonist.car.angle)*0.05
    protagonist.car.y += protagonist.car.linear_speed * cos(protagonist.car.angle)*0.05


def bullet_effect(protagonist: CarP, other_player: CarP, entity: Bullet):
    # increase shooter energy
    other_player.hud.execute_energy_actions("add", BER)  # shooting car receives energy for hitting the opponent's car
    # decrease player shot's life
    protagonist.hud.execute_life_actions("damage", BD)  # car hit receives damage for being hit


EFFECTS = {None: do_nothing, "wall": wall_effect, "bullet": bullet_effect}

#  useful in the future
#  hud.execute_life_actions("damage", WCD)  # for each frame in contact, the car looses a certain amount of life
