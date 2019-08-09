from gad.Agent import Agent


class Population:


    def __init__(self, size, shape):
        self.shape = shape
        self.population = [Agent(genes=5,shape=shape) for _ in range(size)]
