import numpy as np

class UnitState():
	def __init__(self, team, position, target_position, path, position_fraction, speed):
		super().__init__()
		self.team = team
		self.position = position
		self.target_position = target_position
		self.path = path
		self.position_fraction = position_fraction


class GameState():
	def __init__(self, terrain_grid, units):
		super().__init__()
		self.terrain_grid = terrain_grid
		self.units = units


def empty_grid(n_rows, n_cols):
	return np.full((n_rows, n_cols), False)

def example_grid():
	map_string = """
	................................
	................................
	................................
	................................
	................................
	................................
	............XXXXXXXXXXXXXXXX....
	............XXXXXXXXXXXXXXXX....
	................................
	................................
	............XXXXXXXXXXXXXXXX....
	............XXXXXXXXXXXXXXXX....
	................................
	................................
	................................
	................................
	................................
	................................
	................................
	................................
	................................
	................................
	................................
	................................
	................................
	................................
	................................
	................................
	................................
	................................
	................................
	................................
	"""

	# Remove newline characters and create a single string
	map_string = map_string.strip().replace("\n", "").replace(" ", "")

	# Convert the string to a boolean array
	bool_map = np.array([c == 'X' for c in map_string], dtype=bool)

	# Reshape the array to a 2D 32x32 grid
	bool_map = bool_map.reshape(32, 32)

	return bool_map

def example_unit():
	return UnitState(
		team=0,
		position=(0, 0),
		target_position=(5, 0),
		path=[(1, 0), (2, 0), (3, 0), (4, 0), (5, 0)],
		position_fraction=0.0,
		speed=4.0,
	)



def create_example_game():
	terrain_grid = example_grid()
	example_units = [example_unit()]
	return GameState(terrain_grid, example_units)
	

# Update game logic at exactly 60 frames per second, regardless of frame rate.
update_interval = 1.0 / 60.0

def update_unit(unit, game_state):
	if unit.target_position == None or unit.path == None:
		unit.position_fraction = 0.0

	else:

		unit.position_fraction += update_interval * unit.speed

		while unit.position_fraction >= 1.0:
			unit.position_fraction -= 1.0

			# If there's a target then we must've calculated a path to it.
			assert len(unit.path) > 0

			unit.position = unit.path.pop(0)

			# If we've reached the target then stop moving.
			if unit.position == unit.target_position:
				unit.path = None
				unit.target_position = None
				break


def update_game_state(game_state):
	for unit in game_state.units:
		update_unit(unit, game_state)
