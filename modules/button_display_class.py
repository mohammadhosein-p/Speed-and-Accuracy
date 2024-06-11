import pygame as pg

class ButtonDisplay():
    def __init__(self, letter, x, y, window) -> None:
        self.font = pg.font.SysFont('comicsans', 30, True)
        self.letter = letter
        self.window = window
        self.x = x
        self.y = y
        self.counter = 0

    def active(self):
        self.counter = 20

    def draw(self):
        if self.counter > 0:
            self.counter -= 1
            color = (237, 241, 214)
        else:
            color = (52, 76, 100)
        text = self.font.render(self.letter, False, color)
        self.window.blit(text, (self.x, self.y))
