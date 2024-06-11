import pygame as pg
from modules.player_class import Player
from modules.Block_class import BlockManager
from modules.score_class import ScoreManager
from modules.button_display_class import ButtonDisplay
from modules.end_screen_class import EndScreen
from modules.palette_changer import PaletteManager


pg.init()
window = pg.display.set_mode((800, 600))
pg.display.set_caption("Speed and Accuracy")
clock = pg.time.Clock()

button_sound = pg.mixer.Sound("./source/hit.mp3")
game_over_sound = pg.mixer.Sound("./source/game_over.mp3")
game_start_sound = pg.mixer.Sound("./source/start.mp3")

starting_x = 100
starting_y = 250
run = True

score_manager = ScoreManager(window)
player = Player(starting_x + 150, starting_y + 50)
block_manager = BlockManager(starting_x, starting_y, window)
e_display = ButtonDisplay("E", 650, 520, window)
w_display = ButtonDisplay("W", 130, 520, window)
palette_changer = PaletteManager(window)

block_manager.reset_block()
game_start_sound.play()

def check_matching():
    target_block = block_manager.block_list[4-block_manager.create_block_counter]
    if target_block.x <= player.x <= target_block.x + 148 and target_block.y <= player.y <= target_block.y + 98:
        block_manager.change_blocks_coordinate()
        block_manager.create_new_block()
        score_manager.add_score()
        score_manager.active_add_score_pop_up(player.x, player.y)
    else:
        game_over_sound.play()
        end_screen = EndScreen(score_manager.current_score)
        if end_screen.result == 'exit':
            pg.quit()
            exit()
        elif end_screen.result == 'restart':
            pg.display.set_caption("Speed and Accuracy")
            game_start_sound.play()
            score_manager.new_best_score = False
            score_manager.reset_score()
            block_manager.reset_block()
            player.reset_speed()

def update_display():
    window.fill((0, 0, 0))
    block_manager.draw_blocks(palette_changer.using_palette)
    player.move(window, score_manager.current_score)
    score_manager.write_score()
    score_manager.write_new_best()
    score_manager.write_pop_up()
    e_display.draw()
    w_display.draw()
    palette_changer.draw_theme_tip()
    pg.display.update()

while run:
    clock.tick(60)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_w:
                player.change_direction(+1)
                button_sound.play()
                w_display.active()
                check_matching()

            if event.key == pg.K_e:
                player.change_direction(-1)
                button_sound.play()
                e_display.active()
                check_matching()
            
            if event.key == pg.K_1:
                palette_changer.change_theme("1")
            if event.key == pg.K_2:
                palette_changer.change_theme("2")
            if event.key == pg.K_3:
                palette_changer.change_theme("3")

    update_display()

pg.quit()

