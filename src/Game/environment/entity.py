from src.config.globals import MAP_SURFACE_SIZE, MAP_SURFACE
from random import randint
import pygame


class Entity:
    
    def __init__(self) -> None:
        
        self.pos_x: int = randint(0, MAP_SURFACE_SIZE[0])
        self.pos_y: int = randint(0, MAP_SURFACE_SIZE[1])
    
    def draw(self):
        pass
    
    def is_inside(self, player_rect: pygame.Rect):
        pass