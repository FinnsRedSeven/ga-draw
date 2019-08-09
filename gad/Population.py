from gad.Agent import Agent
import skimage.measure as sk


class Population:

    def __init__(self, size, target):
        self.target = target
        self.population = [Agent(genes_no=100, shape=target.shape).new() for _ in range(size)]

    @property
    def size(self):
        return len(self.population)

    def new_child(self, parents):
        self.population.append(Agent(shape=self.target.shape).crossover(parents=parents))

    def sort_mse(self, reverse=False):
        self.population.sort(key=lambda x: x.fitness, reverse=reverse)



    def cull(self, size):
        length = int(len(self.population)*size)
        self.population = self.population[0:length]

    def fitness_mse(self):
        for agent in self.population:
            agent.fitness = sk.compare_mse(self.target, agent.render())

    def fitness_ssim(self):
        for agent in self.population:
            agent.fitness = sk.compare_ssim(self.target, agent.render(), multichannel=True)

    def sort_ssim(self):
        self.population.sort(key=lambda x: x.fitness, reverse=True)