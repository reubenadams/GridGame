import pygame


def update_graphics(screen, game_state, cell_width, margin):
	screen.fill('White')
	terrain_grid = game_state.terrain_grid
	units = game_state.units
	draw_terrain(screen, terrain_grid, cell_width, margin)
	draw_units(screen, units, cell_width, margin)
	# user_cell_click()


def draw_terrain(screen, terrain_grid, cell_width, margin):
	game_height, game_width = terrain_grid.shape
	for game_y in range(game_height):
		for game_x in range(game_width):
			cell_is_occupied = terrain_grid[game_y, game_x]
			if cell_is_occupied:
				rect = cell_to_rect(cell_coord=(game_x, game_y), cell_width=cell_width, margin=margin)
				pygame.draw.rect(screen, 'Black', rect)


def draw_units(screen, units, cell_width, margin):
	for unit in units:
		game_x, game_y = unit.position
		rect = cell_to_rect(cell_coord=(game_x, game_y), cell_width=cell_width, margin=margin)
		if unit.team == 1:
			color = 'Green'
		elif unit.team == 0:
			color = 'Red'
		else:
			raise ValueError(f"Unrecognised team: {unit.team}. Should be 0 or 1.")
		pygame.draw.rect(screen, color, rect)


def pixel_xy_to_cell_xy(pixel_x, pixel_y, cell_width):
	return pixel_x // cell_width, pixel_y // cell_width


def cell_to_rect(cell_coord, cell_width, margin):
	x, y = cell_coord
	left = x * cell_width + margin
	top = y * cell_width + margin
	width, height = cell_width - 2 * margin, cell_width - 2 * margin
	return left, top, width, height


