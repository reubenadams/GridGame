import pygame
from sys import exit

pygame.init()

SCREEN_DIM = (800, 600)
screen = pygame.display.set_mode(SCREEN_DIM)


running = True


while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()

	screen.fill('White')
	pygame.display.flip()
