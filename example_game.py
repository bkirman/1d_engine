from engine.game_engine import BaseGame


class BouncingDotGame(BaseGame):
    """A tiny example game that moves a dot back and forth across a 1D display."""

    def __init__(self):
        self.position = 0
        self.direction = 1

    def init(self, engine):
        self.position = 0
        self.direction = 1

    def update(self, engine, dt):
        self.position += self.direction
        if self.position <= 0:
            self.position = 0
            self.direction = 1
        elif self.position >= engine.display.width - 1:
            self.position = engine.display.width - 1
            self.direction = -1

    def draw(self, engine, display):
        display.set_pixel(int(self.position), 1)
