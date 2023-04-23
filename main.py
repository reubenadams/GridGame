import pygame
from sys import exit
import numpy as np
from graphics import update_graphics
from gamestate import create_example_game, update_game_state


pygame.init()
FPS = 60
SCREEN_DIM = (800, 600)
screen = pygame.display.set_mode(SCREEN_DIM)
clock = pygame.time.Clock()
example_game_state = create_example_game()



running = True


while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
	# update_gamestate()
	update_graphics(screen, example_game_state, cell_width=100, margin=4)
	clock.tick(FPS)

