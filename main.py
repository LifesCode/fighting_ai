from src.Game import Game
from src.AI import AIRaffaele, AIRoberto
import pygame
pygame.init()

WIDTH, HEIGHT = 1080, 720
BG_COLOR = (0, 0, 0)  # default is (0, 150, 150)
BG = pygame.Surface((WIDTH, HEIGHT))
BG.fill(BG_COLOR)  # set screen with background color
FPS = 1
CLOCK = pygame.time.Clock()
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Stick-Man A.I.")


def main():
    game = Game(SCREEN, CLOCK, [AIRaffaele, AIRoberto])
    game.start()


if __name__ == "__main__":
    main()
