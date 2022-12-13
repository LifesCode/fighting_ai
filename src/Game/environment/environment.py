from src.config.globals import SCREEN, BORDER_RADIUS, MAP_SURFACE, MAP_SURFACE_SIZE, MAP_SURFACE_POS, MAP_METER_SIZE
import pygame

class Environment:
    
    def __init__(self):
        self.border_display_adjust = 3
        self.map_list: list
        self.make_map_list()
        # self.show_map()
        
        self.environment_objects = {
            "0": lambda pos_x, pos_y : None,
            "1": self.draw_block
        }
        

    def make_map_list(self):
        self.map_list = []
        for line in open("./src/Game/environment/maps/map_1.txt", "r").readlines():
            self.map_list.append(line.strip().split(" "))
            
    def draw_map(self):
        x = 0
        y = 0
        for row in self.map_list:
            for colum in row:
                self.environment_objects[colum](x, y)
                pygame.draw.rect(
                    surface=MAP_SURFACE, 
                    color=(255, 255, 255),
                    rect=(
                        x,
                        y,
                        MAP_METER_SIZE,
                        MAP_METER_SIZE
                    ),
                    width=2
                )
                x += MAP_METER_SIZE
            x = 0
            y += MAP_METER_SIZE
        
    # def show_map(self) :
    #     for line in self.map_list:
    #         print(line)
    
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
        self.draw_map()
    
    def draw_block(self, pos_x, pos_y):
        pygame.draw.rect(
            surface=MAP_SURFACE, 
            color=(139,69,19),
            rect=(
                pos_x,
                pos_y,
                MAP_METER_SIZE,
                MAP_METER_SIZE
            ),
            border_radius=5
        )
