import pygame


def update_graphics(screen, game_state, cell_width, margin):
	terrain_grid = game_state.terrain_grid
	units = game_state.units
	draw_terrain(screen, terrain_grid, cell_width, margin)
	draw_units(screen, units, cell_width, margin)
	# user_cell_click()


def draw_terrain(screen, terrain_grid, cell_width, margin):
	num_rows, num_cols = terrain_grid.shape
	for row in range(num_rows):
		for col in range(num_cols):
			cell_is_occupied = terrain_grid[row, col]
			if cell_is_occupied:
				rect = cell_to_rect(cell_coord=(col, row), cell_width=cell_width, margin=margin)
				pygame.draw.rect(screen, 'Black', rect)


def draw_units(screen, units, cell_width, margin):
	for unit in units:
		row, col = unit.position
		rect = cell_to_rect(cell_coord=(col, row), cell_width=cell_width, margin=margin)
		if unit.team == 1:
			color = 'Green'
		elif unit.team == 0:
			color = 'Red'
		else:
			raise ValueError(f"Unrecognised team: {unit.team}. Should be 0 or 1.")
		pygame.draw.rect(screen, color, rect)


def user_cell_click(events):
	pass


def cell_to_rect(cell_coord, cell_width, margin):
	x, y = cell_coord
	left = x * cell_width + margin
	top = y * cell_width + margin
	width, height = cell_width - 2 * margin, cell_width - 2 * margin
	return left, top, width, height


