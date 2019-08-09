from sklearn.preprocessing import normalize
from gad.Population import Population

import cv2
from PIL import Image
import numpy as np


class GeneticAlgorithm:

    population: Population

    def __init__(self, target, population_size):
        self.target_population_size = population_size
        self.population = Population(size=population_size, target=target)
        self.cull = .4
        self.target = target
        self.generation = 0
        self.p = np.array([1/n for n in range(5,5+int(population_size*self.cull))])/np.sum([1/n for n in range(5,5+int(population_size*self.cull))])

    def next_generation(self):
        self.generation += 1
        self.selection()
        self.population.cull(self.cull)
        self.cross_over()
        self.mutation()

    def selection(self):
        self.population.fitness_mse()
        self.population.sort_mse()

    def cross_over(self):
        pairs = [self.select_parents() for _ in range(self.target_population_size - self.population.size)]
        for pair in pairs:
            self.population.new_child(pair)

    def mutation(self):
        for agent in self.population.population:
            agent.mutate(0.05)



    def best(self):
        self.selection()
        return self.show_fitness(self.population.population[0])

    def images(self):
        self.population.sort_mse(reverse=True)
        for agent in self.population.population:
            yield self.show_fitness(agent)

    def select_parents(self):
        return list(np.random.choice(self.population.population,
                                     size=2,
                                     replace=False,
                                     p=self.p))

    def show_fitness(self, agent):
        font = cv2.FONT_HERSHEY_PLAIN
        fontScale = 1
        fontColor = (0,0,0)
        lineType = 1
        im = agent.render()
        cv2.putText(im,"Gen: " + str(self.generation) +" Fitness: " + str(agent.fitness)[0:9], (0, 20), font, fontScale, fontColor, lineType)
        return im
