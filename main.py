import pygame
from sys import exit
import numpy as np
from graphics import update_graphics, pixel_xy_to_cell_xy
from gamestate import create_example_game, update_game_state, apply_action, Action


pygame.init()
FPS = 60
SCREEN_DIM = (800, 600)
CELL_WIDTH = 20
screen = pygame.display.set_mode(SCREEN_DIM)
clock = pygame.time.Clock()
game_state = create_example_game()
num_rows, num_cols = game_state.terrain_grid.shape


running = True


# Pretend you're player 0


while running:
	action_list = []
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
		if event.type == pygame.MOUSEBUTTONDOWN:
			pixel_x, pixel_y = event.pos
			game_x, game_y = pixel_xy_to_cell_xy(pixel_x, pixel_y, CELL_WIDTH)
			action_list.append(Action((game_x, game_y), team=0, action_type=0))
	for action in action_list:
		apply_action(game_state, action)
	update_game_state(game_state)
	update_graphics(screen, game_state, cell_width=CELL_WIDTH, margin=1)
	pygame.display.flip()
	clock.tick(FPS)

