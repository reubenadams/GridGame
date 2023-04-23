# GridGame
Reuben and Calin's Massive Multiplayer Online Game


Grid-based.

Black squares are blocks.

Green/Blue squares are your/enemy characters.

Player clicks on a green square and an empty square, then the game moves green square to empty square. First ignore collisions (friendly and enemy) - squares pass through each other.

All player commands and game info should be stored on and reloaded from a json file. Every class should have a save_to_file method.

Make multiplayer (without collisions at first) by sending data between server and player computers.

Finally handle friendly and enemy collisions.

Each square has a health value and automatically attacks the closest enemy square within a maximum radius. Each square attacks at most one other.

Strategy is to pile onto lonely enemy squares.


Game state stored in json file:
1. Grid of terrain - boolean array (True = obstacle, False = empty)
2. List of units with their attributes, including latest move(s)
3. Each unit is dictionary with attributes: current_row, current_col, target_row, target_col, path, team, health, who_fighting, speed, time_until_next_move

In graphics:
1. Take in game state, read latest move(s), move pygame sprites
2. Returns new game state if necessary


Things to do in gridspace:
1. Function to generate the terrain
2. Function to get path for moving units
3. Function detecting whether to fight
4. Function calculating health reduction

Things to do in graphics:
1. Draw terrain and units
2. Detect where user has clicked and convert to grid cell
3. Later make unit motion smooth


Convention:
Pygame pixels: (x, y), x is horizontal, y is vertical (increasing downwards)
Game grid: To get row i, col j, lookup A[j, i], which corresponds to pixel coord (i * cell_width, j * cell_width)
which is top-left pixel of that grid cell.
