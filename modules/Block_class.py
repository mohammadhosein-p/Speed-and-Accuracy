import pygame as pg
import random as rd

class Block():
    def __init__(self, x, y) -> None:
        self.x, self.y = x, y

    def draw(self, pg_window, color):
        pg.draw.rect(pg_window, color, (self.x, self.y, 148, 98), border_radius=8)

class BlockManager():
    def __init__(self, starting_x, starting_y, pg_window) -> None:
        self.block_list = []*7
        self.starting_x = starting_x
        self.starting_y = starting_y
        self.pg_window = pg_window
        self.create_block_counter = 3
    
    def reset_block(self):
        self.block_list = []
        self.create_block_counter = 3
        for i in range(4):
            self.block_list.append(Block(self.starting_x + 150*i, self.starting_y))

    def create_new_block(self):
        has_collision = True
        while has_collision:
            all_posible_coordinate_list = [(self.block_list[len(self.block_list)-1].x+150, self.block_list[len(self.block_list)-1].y),
                (self.block_list[len(self.block_list)-1].x, self.block_list[len(self.block_list)-1].y +100),
                (self.block_list[len(self.block_list)-1].x, self.block_list[len(self.block_list)-1].y -100)]
            weights = [0.7, 0.15, 0.15]
            new_coordinate = rd.choices(all_posible_coordinate_list, weights)
            has_collision = False
            for block in self.block_list:
                if new_coordinate[0][0] == block.x and new_coordinate[0][1] == block.y:
                    has_collision = True
                    break
        self.block_list.append(Block(new_coordinate[0][0], new_coordinate[0][1]))


    def change_blocks_coordinate(self):
        if self.block_list[3-self.create_block_counter].x < self.block_list[4-self.create_block_counter].x:
            for block in self.block_list:
                block.x -= 150
        elif self.block_list[3-self.create_block_counter].y < self.block_list[4-self.create_block_counter].y:
            for block in self.block_list:
                block.y -= 100
        elif self.block_list[3-self.create_block_counter].y > self.block_list[4-self.create_block_counter].y:
            for block in self.block_list:
                block.y += 100

        if self.create_block_counter == 0:
            self.block_list.pop(0)
        else:
            self.create_block_counter -= 1


    def draw_blocks(self, using_palette):
        for index in range(len(self.block_list)-1, -1, -1):
            if (index < 4 and self.create_block_counter == 0) or (index < 4-self.create_block_counter and self.create_block_counter > 0):
                self.block_list[index].draw(self.pg_window, using_palette[0])
            elif (index == 4 and self.create_block_counter < 1) or (self.create_block_counter > 0 and index == 4 - self.create_block_counter):
                self.block_list[index].draw(self.pg_window, using_palette[1])
            else:
                self.block_list[index].draw(self.pg_window, using_palette[2])

