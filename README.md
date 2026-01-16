ARI 5001 — Noisy Heuristic Search in GridWorld
Project Overview

This repository contains the implementation and experimental evaluation of classical search algorithms applied to a grid-based path planning problem with bounded noisy action costs.
The project investigates how heuristic properties such as admissibility, consistency, and robustness to noise affect search optimality and efficiency.

The work was completed as part of ARI 5001 – Introduction to Artificial Intelligence at Bahçeşehir University (BAU).

Problem Description
An agent navigates a finite 2D grid environment with obstacles.
The goal is to find a path from a start cell to a goal cell that minimizes the true path cost, while the agent observes noisy action costs during search.

The project evaluates:
* Uniform Cost Search (UCS)
* Greedy Best-First Search
* A* Search with different heuristics
under both normal and pathological grid configurations.

-Algorithms Implemented:

Uniform Cost Search (UCS)
Serves as the optimal baseline using accumulated path cost only.

Greedy Best-First Search
Uses only heuristic information and demonstrates suboptimal behavior.

A*
Combines path cost and heuristic guidance using:
Manhattan heuristic
Noise-aware admissible heuristic

- Heuristics :
* Manhattan Distance
Standard admissible and consistent heuristic for grid worlds.
* Noise-Aware Confidence Heuristic
A conservative heuristic designed to preserve admissibility under bounded cost noise.

-Experimental Evaluation:
The experiments measure
Number of expanded nodes
Re-expansions in A*
Path optimality under true cost
Behavior in pathological grid layouts
Results are visualized using simple plots to compare algorithm behavior.

## How to Run
1. Install required dependencies:
   pip install numpy matplotlib

2. Run the experiments:
   python experiments.py

