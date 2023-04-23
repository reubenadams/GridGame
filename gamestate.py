import numpy

class GameState():
	def __init__(self, terrain_grid):
		super().__init__()
		self.terrain_grid = terrain_grid


def empty_grid(n_rows, n_cols):
	return np.full((n_rows, n_cols), False)

