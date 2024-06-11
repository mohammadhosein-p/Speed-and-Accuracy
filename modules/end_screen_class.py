import pygame as pg

class EndScreen():
    def __init__(self, final_score):
        pg.init()
        self.end_win = pg.display.set_mode((800, 600))
        pg.display.set_caption("End Game")
        self.clock = pg.time.Clock()
        self.font = pg.font.SysFont('comicsans', 30, True)
        self.run = True
        self.result = None
        while self.run:
            self.clock.tick(60)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.run = False
                    self.result = 'exit'
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_w:
                        self.run = False
                        self.result = 'restart'
                    if event.key == pg.K_e:
                        self.run = False
                        self.result = 'exit'
            self.draw_end_screen(final_score)

    def draw_end_screen(self, final_score):
        self.end_win.fill((0, 0, 0))
        text1 = self.font.render(f"Your final score: {final_score}", False, (225, 240, 218))
        text2 = self.font.render("Press E to exit or W to restart", False, (225, 240, 218))
        self.end_win.blit(text1, (260, 180))
        self.end_win.blit(text2, (165, 250))
        pg.display.update()
  