from src.Game.Animations import player_animations
from src.Game.Effects import FireEffect


class Player:
    frame_module = {"run": 10}
    player_states = ("run",)
    animations = player_animations(player_states, frame_module)

    def __init__(self, ai, num):
        self.AI = ai
        self.frame = 0
        self.state = "run"
        self.x = 500
        self.y = 200
        self.speed = 40
        self.effect = FireEffect(200, (self.x+240, self.y+50))

    def update(self):
        self.frame = (self.frame+1) % self.frame_module[self.state]
        self.x = (self.x + self.speed) % 1080

    def update_state(self, new_state):
        self.frame = 0
        self.state = new_state

    def draw(self, screen):
        self.update()
        screen.blit(self.animations[self.state][self.frame], (self.x, self.y))
        self.effect.draw(screen, [self.x+140, self.y])
