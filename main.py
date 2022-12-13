from src.Game import Game
from src.AI import AIRaffaele, AIRoberto
import pygame


pygame.display.set_caption("Stick-Man A.I.")


def main():
    game = Game([AIRaffaele, AIRoberto])
    game.start()


if __name__ == "__main__":
    main()
