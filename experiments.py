from grid import GridWorld
from costs import CostModel
from search import (
    uniform_cost_search,
    greedy_best_first_search,
    a_star_search,
    reconstruct_path
)
from heuristics import manhattan, h_conf , h_inadmissible
from plots import (
    plot_node_expansions,
    plot_reexpansions,
    plot_pathological_behavior
)
import numpy as np


import random
random.seed(42)
np.random.seed(42)

def check_admissibility(grid, cost_model, heuristic):
    """
    Empirically verifies h(s) <= h*(s) for all reachable states,
    where h*(s) is the optimal cost from s to the goal,
    computed by running UCS from the goal.
    """

    # Run UCS with goal as start (reverse search)
    reversed_grid = GridWorld(
        width=grid.width,
        height=grid.height,
        obstacles=grid.obstacles,
        start=grid.goal,
        goal=grid.start
    )

    _, _, true_cost_to_goal, _ = uniform_cost_search(reversed_grid, cost_model)

    violations = []

    for state in true_cost_to_goal:
        h_val = heuristic(state, grid.goal)
        h_star = true_cost_to_goal[state]

        if h_val > h_star + 1e-6:
            violations.append((state, h_val, h_star))

    if len(violations) == 0:
        print("Heuristic is empirically admissible on this grid.")
    else:
        print("Admissibility violations found:")
        for v in violations:
            print(v)



# BASIC GRID

print("BASIC GRID TEST")

obstacles = {(1,1), (1,2), (2,1)}

grid = GridWorld(
    width=5,
    height=5,
    obstacles=obstacles,
    start=(0, 0),
    goal=(4, 4)
)

cost_model = CostModel(base_cost=1.0, delta=0.2)
print("\nAdmissibility Check for Noise-Aware Heuristic:")
check_admissibility(
    grid,
    cost_model,
    heuristic=lambda s, g: h_conf(s, g, cost_model.delta)
)



# UCS
print("\n UCS ")
came_u, obs_u, true_u, exp_u = uniform_cost_search(grid, cost_model)
path_u = reconstruct_path(came_u, grid.start, grid.goal)
print("Path:", path_u)
print("Expanded:", exp_u)


# GREEDY
print("\nGreedy ")
came_g, exp_g = greedy_best_first_search(grid)
path_g = reconstruct_path(came_g, grid.start, grid.goal)
print("Path:", path_g)
print("Expanded:", exp_g)


#  A* (Manhattan)
print("\n A* (Manhattan heuristic) ")
came_a, obs_a, true_a, exp_a, re_a = a_star_search(
    grid,
    cost_model,
    heuristic=lambda s, g: manhattan(s, g)
)

path_a = reconstruct_path(came_a, grid.start, grid.goal)
print("Path:", path_a)
print("Observed cost:", obs_a[grid.goal])
print("True cost:", true_a[grid.goal])
print("Expanded:", exp_a)
print("Re-expansions:", re_a)


# A* (Noise-aware heuristic)
print("\n A* (Noise-aware heuristic) ")
came_c, obs_c, true_c, exp_c, re_c = a_star_search(
    grid,
    cost_model,
    heuristic=lambda s, g: h_conf(s, g, cost_model.delta)
)

path_c = reconstruct_path(came_c, grid.start, grid.goal)
print("Path:", path_c)
print("Observed cost:", obs_c[grid.goal])
print("True cost:", true_c[grid.goal])
print("Expanded:", exp_c)
print("Re-expansions:", re_c)



# A* (Inadmissible heuristic - 1.5x Manhattan)
print("\n A* (Inadmissible heuristic - 1.5x Manhattan) ")
came_i, obs_i, true_i, exp_i, re_i = a_star_search(
    grid,
    cost_model,
    heuristic=lambda s, g: h_inadmissible(s, g)
)

path_i = reconstruct_path(came_i, grid.start, grid.goal)
print("Path:", path_i)
print("Observed cost:", obs_i[grid.goal])
print("True cost:", true_i[grid.goal])
print("Expanded:", exp_i)
print("Re-expansions:", re_i)



# PATHOLOGICAL GRID

print("\nPATHOLOGICAL GRID TEST")

obstacles_pathological = {
    (1,0),(1,1),(1,2),(1,3),(1,4),
    (3,1),(3,2),(3,3),(3,4)
}

pathological_grid = GridWorld(
    width=6,
    height=6,
    obstacles=obstacles_pathological,
    start=(0, 0),
    goal=(5, 0)
)

clean_cost_model = CostModel(base_cost=1.0, delta=0.0)


# UCS
print("\nUCS:")
_, _, _, exp_p_u = uniform_cost_search(pathological_grid, clean_cost_model)
print("Expanded:", exp_p_u)


#  GREEDY
print("\nGreedy:")
_, exp_p_g = greedy_best_first_search(pathological_grid)
print("Expanded:", exp_p_g)


# A*
print("\nA* (Manhattan):")
_, _, _, exp_p_a, re_p_a = a_star_search(
    pathological_grid,
    clean_cost_model,
    heuristic=lambda s, g: manhattan(s, g)
)
print("Expanded:", exp_p_a)
print("Re-expansions:", re_p_a)


print("\n  Plots ")
plot_node_expansions()
plot_reexpansions()
plot_pathological_behavior()
