import numpy as np
from queue import PriorityQueue
from math import sqrt

def heuristic(a, b):
    return sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

diagonal_cost = sqrt(2)

def compute_path(terrain_grid, position, target_position):
    # Initialize the open set with the start position
    open_set = PriorityQueue()
    open_set.put((0, position))
    
    # Initialize the came_from and cost_so_far dictionaries
    came_from = {}
    cost_so_far = {position: 0}
    
    # Define possible moves (including diagonals)
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

    while not open_set.empty():
        _, current = open_set.get()

        if current == target_position:
            path = []
            while current != position:
                path.append(current)
                current = came_from[current]
            path.reverse()
            return path

        for move in moves:
            neighbor = (current[0] + move[0], current[1] + move[1])
            
            # Check if the neighbor is within the grid and is not a wall
            if 0 <= neighbor[0] < terrain_grid.shape[1] and 0 <= neighbor[1] < terrain_grid.shape[0] and not terrain_grid[neighbor[1], neighbor[0]]:
                new_cost = cost_so_far[current] + 1 if abs(move[0]) + abs(move[1]) == 1 else cost_so_far[current] + diagonal_cost

                if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                    cost_so_far[neighbor] = new_cost
                    priority = new_cost + heuristic(neighbor, target_position)
                    open_set.put((priority, neighbor))
                    came_from[neighbor] = current

    return None

# Test
if __name__ == "__main__":
    terrain_grid = np.array([
        [False, False, False, False, False],
        [False,  True,  True,  True, False],
        [False,  True, False,  True, False],
        [False,  True, False,  True, False],
        [False, False, False, False, False]
    ])

    position = (0, 0)
    target_position = (4, 4)

    path = compute_path(terrain_grid, position, target_position)
    print(path)