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
