import random
from src.Game.Player import Player
from src.Game.HUD.HUD import HUD

import pygame


class Game:
    def __init__(self, screen, clock, AIs):
        self.screen: pygame.Surface = screen
        self.clock = clock
        rand = random.choice([1, 0])   # alternate between player 1 and 2
        self.player_1 = Player(AIs[0], rand)
        self.player_2 = Player(AIs[1], 1-rand)
        self.hud = HUD("Player 2", self.screen)

    def start(self):
        self.game_loop()

    def draw_background(self):
        self.screen.fill((255, 255, 255))
        pygame.draw.line(self.screen, (0, 255, 255), (0, 480), (1080, 480))

    def draw_hud(self):
        pass

    def refresh(self):
        self.draw_background()
        self.player_1.draw(self.screen)
        self.player_2.draw(self.screen)
        self.hud.draw()
        pygame.display.update()

    def game_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                    
                elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:  # mouse click
                    self.hud.damage()
                    
            self.refresh()
            self.screen.fill((0, 0, 0))
            self.clock.tick(30)
