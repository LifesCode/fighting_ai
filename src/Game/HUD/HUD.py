from src.Game.HUD.rects import Rects
from src.config.globals import MAX_ENERGY, MAX_LIFE, BARS_POSITIONS, SCREEN
import math



class HUD:
    
    life = MAX_LIFE
    energy = MAX_ENERGY
    
    def __init__(self, player_name):
        self.player_name = player_name  # information if it is player one or player 2
        self.bar_position = "right" if self.player_name == "Player 1" else "left"
        self.bar_containers = {
            "life": {
                "rect": Rects(
                    rect_type="life",  
                    max_value=MAX_LIFE,
                    height=26, 
                    x=BARS_POSITIONS["x"],
                    y=BARS_POSITIONS["y"], 
                    color=(0, 255, 0), 
                    bar_position=self.bar_position
                ),
                "max": MAX_LIFE,
                "current_value": lambda: self.life,
            },
            "energy": {
                "rect": Rects(
                    rect_type="energy", 
                    max_value=MAX_ENERGY,
                    height=18, 
                    x=BARS_POSITIONS["x"],
                    y=BARS_POSITIONS["y"]+30, 
                    color=(0, 255, 0), 
                    bar_position=self.bar_position
                ),
                "max": MAX_ENERGY,
                "current_value": lambda: self.energy,
            }
        }   
        self.hud_actions = {
            "damage": lambda percentage : self.life - MAX_LIFE * percentage if (self.life >= MAX_LIFE * percentage) else 0,
            "heal": lambda percentage : self.life + MAX_LIFE * percentage if (self.life + MAX_LIFE * percentage <= MAX_LIFE) else MAX_LIFE,
            "add": lambda percentage : self.energy + MAX_ENERGY * percentage if (self.energy + MAX_ENERGY * percentage <= MAX_ENERGY) else MAX_ENERGY,
            "remove": lambda percentage : self.energy - MAX_ENERGY * percentage if (self.energy >= MAX_ENERGY * percentage) else 0
        }     

    def execute_life_actions(self, action: str, percentage: float) -> None:
        self.life = self.hud_actions[action](percentage)
    
    def execute_energy_actions(self, action: str, percentage: float) -> None:
        self.energy = self.hud_actions[action](percentage)

    def draw_HUD_bars(self) -> None:
        self.bar_containers["life"]["rect"].draw_bars(
            color_index=math.floor((self.bar_containers["life"]["current_value"]() / 20) - 6)*-1, 
            current_bar_value=self.bar_containers["life"]["current_value"](), 
            max_value=self.bar_containers["life"]["max"]
        )
        
        self.bar_containers["energy"]["rect"].draw_bars(
            color_index=7, 
            current_bar_value=self.bar_containers["energy"]["current_value"](), 
            max_value=self.bar_containers["energy"]["max"]
        )

    def damage(self) -> None:
        self.energy = self.hud_actions["damage"](0.1)
        self.life = self.hud_actions["damage"](0.25)

    def draw(self):
        self.draw_HUD_bars()
