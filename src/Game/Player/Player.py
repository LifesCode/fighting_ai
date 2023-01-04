from src.Game.Animations import player_animations
from src.Game.Effects import FireEffect
from src.config.globals import MAP_SURFACE, WIDTH


class Player:
    frame_module = {"run": 10}
    player_states = ("run",)
    animations = player_animations(player_states, frame_module)

    def __init__(self, ai, name):
        self.name = name
        self.AI = ai
        self.frame = 0
        self.state = "run"
        self.x = 500
        self.y = 200
        self.speed = 20
        self.effect = FireEffect(200, (self.x+240, self.y+50))

    def update(self, dt):
        self.frame = (self.frame+1) % self.frame_module[self.state]
        self.x = (self.x + self.speed) % WIDTH

    def update_state(self, new_state):
        self.frame = 0
        self.state = new_state

    def apply_effect(self):
        pass

    def draw(self):
        # self.HUD.draw(MAP_SURFACE)
        MAP_SURFACE.blit(self.animations[self.state][self.frame], (self.x, self.y))
        self.effect.draw(MAP_SURFACE, [self.x+100, self.y])
