from src.Game.HUD.rect import Rects
from src.Game.HUD.hud_actions import HUDActions
import math

MAX_LIFE = 240
MAX_ENERGY = 100
CONTAINERS_POSITIONS = {"Player 1": {
    "x": 20, "y": 20}, "Player 2": {"x": 300, "y": 20}}


class HUD:
    def __init__(self, player_name, screen):
        self.player_name = player_name  # information if it is player one or player 2
        self.screen = screen
        self.life = 240
        self.energy = 100
        self.bar_containers = {
            "life": {
                "rect": Rects(self.screen, self.life,
                              12, CONTAINERS_POSITIONS[self.player_name]["x"],
                              CONTAINERS_POSITIONS[self.player_name]["y"], (0, 255, 0)),
                "max": MAX_LIFE,
                "current_value": lambda: self.life,
            },
            "energy": {
                "rect": Rects(self.screen, self.energy,
                              12, CONTAINERS_POSITIONS[self.player_name]["x"],
                              CONTAINERS_POSITIONS[self.player_name]["y"]+50, (0, 255, 0)),
                "max": MAX_ENERGY,
                "current_value": lambda: self.energy,
            }
        }
        self.hud_actions = {
            "damage": lambda life, percentage: life - life * percentage if (life >= life * percentage) else 0,
            "life": lambda life, percentage: life + life * percentage if (life + life * percentage <= MAX_LIFE) else MAX_LIFE,
            "addEnergy": lambda energy, percentage: energy + energy * percentage if (energy + energy * percentage <= MAX_ENERGY) else MAX_ENERGY,
            "removeEnergy": lambda energy, percentage: energy - energy * percentage if (energy >= energy * percentage) else 0
        }

    def execute_hud_action(self, hub_action: dict[str, float]) -> None:
        [self.hub_actions[actionValue[0]](actionValue[1])
         for actionValue in hub_action.items()]

    def draw_HUD_bars(self) -> None:
        for box in self.bar_containers.keys():
            bar_value = self.bar_containers[box]["current_value"]()
            if (bar_value >= 0): 
                self.bar_containers[box]["rect"].drawGradientEffect(
                    math.floor((bar_value / 40) - 6)*-1, bar_value)

    def damage(self) -> None:
        self.life -= 5

    def draw_energy_bar(self) -> None:
        pass

    def draw(self):
        self.draw_HUD_bars()
        pass
