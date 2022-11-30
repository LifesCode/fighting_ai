import pygame

SCREEN = pygame.display.set_mode((1080, 720))


def load_animation(name, frames):
    animation = []
    for i in range(frames):
        animation.append(pygame.image.load(f"assets/animations/{name}/{i}.png").convert_alpha())
    return animation


def player_animations(states, frames):
    return {state: load_animation(state, frames[state]) for state in states}
