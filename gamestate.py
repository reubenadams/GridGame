import numpy as np

from pathfinding import compute_path

# Game logic update frequency in updates per seconds.
update_rate = 60.0

class UnitState():
	def __init__(self, team, position, target_position, path, position_fraction, speed):
		super().__init__()
		self.team = team
		self.position = position  # (x, y) on game grid, e.g. (5, 0) -> row 0, col 5
		self.target_position = target_position
		self.path = path
		self.position_fraction = position_fraction
		self.speed = speed


class GameState():
	def __init__(self, terrain_grid, units):
		super().__init__()
		self.terrain_grid = terrain_grid  # terrain_grid[0, 5] -> row 0, col 5 in game, which is (5, 0), i.e. (x, y). terrain_grid.shape = (num_rows, num_cols)
		self.units = units


class Action():
	def __init__(self, target_position, team, action_type):
		self.target_position = target_position
		self.team = team
		self.action_type = action_type


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
	map_string = map_string.strip().replace("\n", "").replace(" ", "").replace("	", "")

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
update_interval = 1.0 / update_rate

def reset_unit_target(unit):
	unit.target_position = None
	unit.path = None
	unit.position_fraction = 0.0

def update_unit(unit, game_state):
	if unit.target_position == None:
		unit.position_fraction = 0.0

	else:
		if unit.path == None:
			unit.path = compute_path(game_state.terrain_grid, unit.position, unit.target_position)
			# Ignore the command if we didn't get a valid path.
			# TODO: clicking on an occupied tile should move the unit to the closest unoccupied tile.
			if unit.path == None or len(unit.path) == 0:
				reset_unit_target(unit)

		unit.position_fraction += update_interval * unit.speed

		while unit.position_fraction >= 1.0:
			unit.position_fraction -= 1.0

			unit.position = unit.path.pop(0)

			# If we've reached the target then stop moving.
			if unit.position == unit.target_position:
				reset_unit_target(unit)
				break


def update_game_state(game_state):
	for unit in game_state.units:
		update_unit(unit, game_state)


def apply_action(game_state, action):
	# TODO: don't hardcode a single unit
	unit = game_state.units[0]
	unit.target_position = action.target_position
	unit.path = None
	

if __name__ == "__main__":
	game_state = create_example_game()

	for _ in range(int(update_rate) * 2):
		update_game_state(game_state)
		print(game_state.units[0].position)