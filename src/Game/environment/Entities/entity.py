from src.config.globals import MAP_SURFACE_SIZE
from random import randint


class Entity:
    
    def __init__(self) -> None:
        self.x: int = randint(0, MAP_SURFACE_SIZE[0])
        self.y: int = randint(0, MAP_SURFACE_SIZE[1])
    
    def draw(self):
        pass

    def get_effect(self, player):
        pass
