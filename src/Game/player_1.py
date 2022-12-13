import pygame
from src.config.globals import MAP_SURFACE,MAP_METER_SIZE


class Player:
    original_image = pygame.image.load("assets/players/shot_man/shot_man.png").convert_alpha()
    original_image = pygame.transform.scale(original_image, (MAP_METER_SIZE, MAP_METER_SIZE))
    
    def __init__(self) -> None:
        self.x = 0
        self.y = 0    
    
    def draw(self) -> None:
        MAP_SURFACE.blit(self.original_image, (self.x, self.y))
    
    def controller_player_moves(self, event) -> None:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.y -= MAP_METER_SIZE
            elif event.key == pygame.K_DOWN:
                self.y += MAP_METER_SIZE
            elif event.key == pygame.K_RIGHT:
                self.x += MAP_METER_SIZE
            elif event.key == pygame.K_LEFT:
                self.x -= MAP_METER_SIZE
                