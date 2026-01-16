
import math

def manhattan(state, goal):
    """Standard Manhattan distance - admissible and consistent"""
    x, y = state
    gx, gy = goal
    return abs(x - gx) + abs(y - gy)

def h_conf(state, goal, delta):
    """Noise-aware confidence heuristic - admissible but weaker"""
    base = manhattan(state, goal)
    d = base  # minimum remaining steps
    return max(0, base - delta * d)

def h_inadmissible(state, goal):
    """Intentionally overestimates by 50% - NOT admissible!"""
    return manhattan(state, goal) * 1.5
