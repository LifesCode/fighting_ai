from src.config.globals import SCREEN, BORDER_RADIUS, MAP_SURFACE, MAP_SURFACE_SIZE, MAP_SURFACE_POS
import pygame

class Environment:
    
    def __init__(self):
        self.border_display_adjust = 3
        self.map_list: list
        self.make_map_list()
        self.show_map()

    def make_map_list(self):
        self.map_list = []
        for line in open("./src/Game/environment/maps/map_1.txt", "r").readlines():
            self.map_list.append(line.strip().split(" "))
        
    def show_map(self) :
        for line in self.map_list:
            print(line)
    
    def draw(self):
        pygame.draw.rect(
            surface=SCREEN, 
            color=(139,69,19),
            rect=(
                MAP_SURFACE_POS[0] - self.border_display_adjust,
                MAP_SURFACE_POS[1] - self.border_display_adjust,
                MAP_SURFACE_SIZE[0] + self.border_display_adjust * 2,
                MAP_SURFACE_SIZE[1] + self.border_display_adjust * 2
            ),
            width=6,
            border_radius=BORDER_RADIUS + 6
        )
    
    def draw_block(self):
        pass
