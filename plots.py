import matplotlib.pyplot as plt
import numpy as np

#1
def plot_node_expansions():
    algorithms = ['UCS', 'Greedy', 'A* Manhattan', 'A* Noise-aware']
    expansions = [24, 9, 9, 23]

    plt.figure()
    plt.bar(algorithms, expansions)
    plt.xlabel('Algorithm')
    plt.ylabel('Nodes Expanded')
    plt.title('Node Expansions Across Search Algorithms')
    plt.show()

#2
def plot_reexpansions():
    heuristics = ['Manhattan', 'Noise-aware']
    reexpansions = [0, 2]

    plt.figure()
    plt.plot(heuristics, reexpansions, marker='o')
    plt.xlabel('Heuristic Type')
    plt.ylabel('Number of Re-expansions')
    plt.title('Heuristic Consistency and Re-expansions')
    plt.show()

#3
def plot_pathological_behavior():
    algorithms = ['UCS', 'Greedy', 'A* Manhattan']
    expansions = [27, 16, 22]

    difficulty = np.arange(len(algorithms))

    plt.figure()
    plt.plot(difficulty, expansions, marker='o')
    plt.xticks(difficulty, algorithms)
    plt.xlabel('Algorithm')
    plt.ylabel('Nodes Expanded')
    plt.title('Algorithm Behavior in Pathological Environment')
    plt.show()
