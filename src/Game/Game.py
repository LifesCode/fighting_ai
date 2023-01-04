from src.Game.Player.Car_Player import CarPlayer
from src.Game.environment.environment import Environment
from src.config.globals import SCREEN, CLOCK, MAP_SURFACE, MAP_SURFACE_POS, FPS, ENTITIES
from src.Game.Player.Effects import EFFECTS
import pygame


class Game:
    def __init__(self, AIs):
        self.environment = Environment()
        self.player_1 = CarPlayer(AIs[0], "Player 1")
        self.player_2 = CarPlayer(AIs[1], "Player 2")
        self.dt = 0

    def start(self):
        self.game_loop()

    def draw_background(self):
        SCREEN.fill((25, 25, 25))
        SCREEN.blit(MAP_SURFACE, MAP_SURFACE_POS)
        MAP_SURFACE.fill((100, 100, 100))

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
        self.environment.draw()
        self.player_1.draw()
        self.player_2.draw()
        pygame.display.update()

    def apply_effects(self):
        for entity in ENTITIES:
            EFFECTS[entity.get_effect(self.player_1)](self.player_1, self.player_2, entity)  # verify effects on player1
            EFFECTS[entity.get_effect(self.player_2)](self.player_2, self.player_1, entity)  # verify effects on player2

    def quit_game(self):
        print("Game Over")
        # 1-> create a summary/overview of each player
        # 2-> save the info
        pygame.quit()
        exit()

    def game_loop(self):
        while True:  # self.player_1.is_alive() and self.player_2.is_alive():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit_game()
                self.input(event)

            self.player_1.update(self.dt)
            self.player_2.update(self.dt)
            self.apply_effects()  # interactions between players and environment
            self.refresh()
            self.dt = CLOCK.tick(FPS)/1000
        self.quit_game()
