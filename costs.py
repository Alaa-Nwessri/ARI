import random

class CostModel:
    def __init__(self, base_cost=1.0, delta=0.0):
        self.base_cost = base_cost
        self.delta = delta

    def true_cost(self, s, s_next):
        return self.base_cost

    def noisy_cost(self, s, s_next):
        noise = random.uniform(-self.delta, self.delta)
        return self.base_cost + noise
