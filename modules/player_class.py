import math
import pygame as pg

class Player():
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.radius = 15
        self.angle = 0
        self.rotation_radius = 80
        self.starting_x = self.x
        self.starting_y = self.y
        self.direction = 1
        self.speed = 3

    def move(self, window, score):
        self.angle += self.direction * (math.sqrt((0.05) * score)+2)
        if self.angle >= 360:
            self.angle = 0
        elif self.angle < 0:
            self.angle = 359
        
        rad = math.radians(self.angle)
        
        self.x = self.rotation_radius * math.cos(rad) + self.starting_x
        self.y = self.rotation_radius * math.sin(rad) + self.starting_y
        self.draw(window)
            
    def draw(self, window):
        pg.draw.circle(window, (196, 180, 84), (int(self.x), int(self.y)), self.radius)

    def reset_speed(self):
        self.speed = 3
    
    def change_direction(self, new_direcrtion):
        self.direction = new_direcrtion