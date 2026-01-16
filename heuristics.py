def manhattan(state, goal):
    x, y = state
    gx, gy = goal
    return abs(x - gx) + abs(y - gy)


def h_conf(state, goal, delta):
    base = manhattan(state, goal)
    d = base  # minimum remaining steps
    return max(0, base - delta * d)
