class GridWorld:
    def __init__(self, width, height, obstacles, start, goal):
        self.width = width
        self.height = height
        self.obstacles = set(obstacles)
        self.start = start
        self.goal = goal

    def in_bounds(self, state):
        x, y = state
        return 0 <= x < self.width and 0 <= y < self.height

    def passable(self, state):
        return state not in self.obstacles

    def neighbors(self, state):
        x, y = state
        actions = [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]
        results = []
        for s in actions:
            if self.in_bounds(s) and self.passable(s):
                results.append(s)
        return results
