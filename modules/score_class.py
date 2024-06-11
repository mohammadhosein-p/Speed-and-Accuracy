import pygame as pg

class ScoreManager():
    def __init__(self, window) -> None:
        self.new_best_sound= pg.mixer.Sound("./source/new_best.mp3")
        self.font = pg.font.SysFont('comicsans', 30, True)
        self.current_score = 0
        self.new_best_score = False
        self.window = window
        self.new_best_counter = 0
        self.player_x = 0
        self.player_y = 0
        self.pop_up_counter = 0
        try:
            with open("./source/best_score.txt") as file:
                self.best_score = int(file.readline().split("\n")[0])
        except:
            self.best_score = 0
    
    def write_score(self):
        text = self.font.render(f"Best score: {self.best_score} Your score: {self.current_score}", False, (225, 240, 218))
        self.window.blit(text, (175, 50))

    def update_best_score(self):
        with open("./source/best_score.txt", 'w') as file:
            file.write(str(self.best_score))

    def add_score(self):
        self.current_score += 1
        if self.current_score > self.best_score:
            self.best_score += 1
            self.update_best_score()
            if not self.new_best_score:
                self.new_best_sound.play()
                self.new_best_counter = 180
                self.new_best_score = True
        self.write_score()
        
    def write_new_best(self):
        if self.new_best_counter > 0:
            text1 = self.font.render(f"NEW BEST SCORE!", False, (225, 240, 218))
            self.window.blit(text1, (245, 100))
            self.new_best_counter -= 1

    def reset_score(self):
        self.current_score = 0
        self.write_score()

    def active_add_score_pop_up(self, player_x, player_y):
        self.pop_up_counter = 15
        self.player_x = player_x
        self.player_y = player_y

    def write_pop_up(self):
        if self.pop_up_counter > 0:
            text1 = self.font.render(f"+1", False, (225, 240, 218))
            self.window.blit(text1, (self.player_x, self.player_y-60))
            self.pop_up_counter -= 1
