import pygame as pg

class PaletteManager():
    def __init__(self, window) -> None:
        self.block_palette1 = [(157, 178, 191), (82, 109, 130), (39, 55, 77)]
        self.block_palette2 = [(185, 180, 199), (92, 84, 112), (53, 47, 68)]
        # self.block_palette3 = [(216, 239, 211), (149, 210, 179), (85, 173, 155)]
        self.block_palette3 = [(216, 239, 211), (149, 210, 179), (85, 173, 155)]
        self.using_palette = self.block_palette1
        self.window = window
        self.font = pg.font.SysFont('comicsans', 16, True)

    def change_theme(self, number):
        exec(f"self.using_palette = self.block_palette{number}")
    
    def draw_theme_tip(self):
        text1 = self.font.render(f"Tip: you can change theme with numbers", False, (225, 240, 218))
        self.window.blit(text1, (250, 535))