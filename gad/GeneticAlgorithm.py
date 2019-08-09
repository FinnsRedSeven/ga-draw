from gad.Population import Population

import cv2
from PIL import Image
import numpy as np
import skimage.measure as sk

class GeneticAlgorithm:





    def __init__(self, target, size):

        self.population = Population(size=size,shape=target.shape)
        self.target = target

    def selection(self):

        for agent in self.population.population:
            self.compute_fitness(agent)
        self.sort()



    def mutation(self):
        pass

    def cross_over(self):
        pass


    def start(self, generations):

        for _ in range(generations):
            self.selection()
            self.cross_over()
            self.mutation()

    def compute_fitness(self, agent):
        agent.fitness = sk.compare_mse(self.target,agent.render())

    def best(self):
        self.sort()
        return self.population.population[0]

    def images(self):
        self.sort()
        for agent in self.population.population:
            yield self.show_fitness(agent)

    def show_fitness(self, agent):
        font = cv2.FONT_HERSHEY_PLAIN
        fontScale = 1
        fontColor = (255, 255, 255)
        lineType = 1
        im = agent.render()
        cv2.putText(im,"MSE: "+str(agent.fitness)[0:9],(0,20),font,fontScale,fontColor,lineType)
        return im

    def sort(self):
        self.population.population.sort(key=lambda x: x.fitness)
