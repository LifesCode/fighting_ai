import random
from src.Game.HUD.HUD import HUD
from src.Game.Player import CarPlayer
from src.Game.player_1 import Player
from src.Game.environment.environment import Environment
from src.config.globals import SCREEN, CLOCK, MAP_SURFACE, MAP_SURFACE_POS
import pygame


class Game:
    def __init__(self, AIs): 
        self.hud_1 = HUD("Player 2")
        self.hud_2 = HUD("Player 1")
        self.player = Player()
        self.envirnment = Environment()
        # self.player_1 = CarPlayer(AIs[0], rand)
        # self.player_2 = Player(AIs[1], 1-rand)
        self.dt = 0

    def start(self):
        self.game_loop()

    def draw_background(self):
        SCREEN.fill((25, 25, 25))
        SCREEN.blit(MAP_SURFACE, (MAP_SURFACE_POS))
        MAP_SURFACE.fill((100, 100, 100))

    def draw_hud(self):
        pass

    def input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.player_1.car.activate_speeding(1)
            elif event.key == pygame.K_DOWN:
                self.player_1.car.activate_speeding(-1)
            elif event.key == pygame.K_b:
                self.player_1.shoot()
            elif event.key == pygame.K_SPACE:
                self.player_1.car.activate_brakes()
            elif event.key == pygame.K_RIGHT:
                self.player_1.car.activate_steering(-1, True)
            elif event.key == pygame.K_LEFT:
                self.player_1.car.activate_steering(1, True)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                self.player_1.car.activate_speeding(0, False)
            elif event.key == pygame.K_SPACE:
                self.player_1.car.activate_brakes(0)
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                self.player_1.car.activate_steering(0, False)

    def refresh(self):
        self.draw_background()
        # self.player_1.draw()
        self.player.draw()
        self.hud_1.draw()
        self.hud_2.draw()
        self.envirnment.draw()
        # self.player_2.draw(SCREEN)
        pygame.display.update()

    def game_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                # self.input(event)
                self.player.controller_player_moves(event=event)

            # self.player_1.update(self.dt)
            self.refresh()
            self.dt = CLOCK.tick()/1000
