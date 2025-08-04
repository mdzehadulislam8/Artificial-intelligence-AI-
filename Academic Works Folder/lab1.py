from collections import deque

class Location:
    def __init__(self, x, y, distance):
        self.x = x
        self.y = y
        self.distance = distance

class MazeSolver:
    def __init__(self):
        self.found_goal = False
        self.total_moves = 0
        self.trail = {}
        self.destination = None
        self.start_point = None
        self.directions = [(1, -1), (-1, 0), (-1, 0), (0, -1), (1, 1),(0, 1)]
        self.grid_size = 0


    def initialize(self):


        maze = [
            [1, 0, 1, 0, 1],
            [1, 0, 1, 1, 1],
            [1, 1, 1, 0, 1],
            [1, 1, 1, 1, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 1, 0, 0]
            
           
        ]
        self.grid_size = len(maze)
        start_x, start_y = 2, 0
        self.start_point = Location(start_x, start_y, 0)
        goal_x, goal_y = 4, 4
        self.destination = Location(goal_x, goal_y, 0)

        self.bfs_traversal(maze)

        if self.found_goal:
            print("Destination reached are moves => ", self.total_moves)
            self.display_path()
        else:
            print("Destination not reachable")

    def move_direction(self, dx, dy):
        if dx == 1 and dy == 0:
            return "Move Down"
        elif dx == -1 and dy == 0:
            return "Move Up"
        elif dx == 0 and dy == 1:
            return "Move Right"
        elif dx == 0 and dy == -1:
            return "Move Left"

    def bfs_traversal(self, maze):
        queue = deque()
        queue.append(self.start_point)
        self.trail[(self.start_point.x, self.start_point.y)] = None

        while queue:
            current = queue.popleft()
            for dx, dy in self.directions:
                new_x, new_y = current.x + dx, current.y + dy
                if 0 <= new_x < self.grid_size and 0 <= new_y < self.grid_size and maze[new_x][new_y] == 1:
                    new_distance = current.distance + 1
                    if (new_x, new_y) not in self.trail:
                        self.trail[(new_x, new_y)] = (current.x, current.y)

                    if new_x == self.destination.x and new_y == self.destination.y:
                        self.found_goal = True
                        self.total_moves = new_distance
                        return
                    maze[new_x][new_y] = 0  
                    next_location = Location(new_x, new_y, new_distance)
                    queue.append(next_location)

    def display_path(self):
        route = []
        current = (self.destination.x, self.destination.y)
        while current is not None:
            route.append(current)
            current = self.trail[current]
        route.reverse()
        print("Here Path -> to -> goal=", route)


if __name__ == "__main__":
    solver = MazeSolver()
    solver.initialize()