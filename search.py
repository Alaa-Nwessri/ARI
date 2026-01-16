import heapq
from heuristics import manhattan


def reconstruct_path(came_from, start, goal):
    path = []
    current = goal
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()
    return path


# UNIFORM COST SEARCH (UCS)

def uniform_cost_search(grid, cost_model):
    frontier = []
    heapq.heappush(frontier, (0, grid.start))

    came_from = {grid.start: None}
    observed_cost = {grid.start: 0}
    true_cost = {grid.start: 0}

    expanded = 0

    while frontier:
        current_obs_cost, current = heapq.heappop(frontier)
        expanded += 1

        if current == grid.goal:
            break

        for nxt in grid.neighbors(current):
            obs_step = cost_model.noisy_cost(current, nxt)
            true_step = cost_model.true_cost(current, nxt)

            new_obs_cost = observed_cost[current] + obs_step
            new_true_cost = true_cost[current] + true_step

            if nxt not in observed_cost or new_obs_cost < observed_cost[nxt]:
                observed_cost[nxt] = new_obs_cost
                true_cost[nxt] = new_true_cost
                heapq.heappush(frontier, (new_obs_cost, nxt))
                came_from[nxt] = current

    return came_from, observed_cost, true_cost, expanded



# GREEDY BEST-FIRST SEARCH

def greedy_best_first_search(grid):
    frontier = []
    heapq.heappush(frontier, (0, grid.start))

    came_from = {grid.start: None}
    expanded = 0

    while frontier:
        _, current = heapq.heappop(frontier)
        expanded += 1

        if current == grid.goal:
            break

        for nxt in grid.neighbors(current):
            if nxt not in came_from:
                priority = manhattan(nxt, grid.goal)
                heapq.heappush(frontier, (priority, nxt))
                came_from[nxt] = current

    return came_from, expanded



# A* SEARCH

def a_star_search(grid, cost_model, heuristic):
    frontier = []
    heapq.heappush(frontier, (0, grid.start))

    came_from = {grid.start: None}
    observed_cost = {grid.start: 0}
    true_cost = {grid.start: 0}

    expanded_states = set()
    expanded = 0
    reexpansions = 0

    while frontier:
        _, current = heapq.heappop(frontier)

        if current in expanded_states:
            reexpansions += 1
        expanded_states.add(current)
        expanded += 1

        if current == grid.goal:
            break

        for nxt in grid.neighbors(current):
            obs_step = cost_model.noisy_cost(current, nxt)
            true_step = cost_model.true_cost(current, nxt)

            new_obs_cost = observed_cost[current] + obs_step
            new_true_cost = true_cost[current] + true_step

            if nxt not in observed_cost or new_obs_cost < observed_cost[nxt]:
                observed_cost[nxt] = new_obs_cost
                true_cost[nxt] = new_true_cost

                h_val = heuristic(nxt, grid.goal)
                priority = new_obs_cost + h_val
                heapq.heappush(frontier, (priority, nxt))
                came_from[nxt] = current

    return came_from, observed_cost, true_cost, expanded, reexpansions
