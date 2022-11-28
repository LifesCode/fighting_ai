from src.Game.HUD import HUD


class Player:
    def __init__(self, ai, num):
        self.AI = ai
        self.HUD = HUD(num)

    def draw(self, screen):
        self.HUD.draw(screen)
