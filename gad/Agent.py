
from gad.Gene import Gene
from PIL import Image, ImageDraw
import numpy as np
import cv2

class Agent:


    def __init__(self, genes_no=5, shape=None):
        self.genes_no = genes_no
        self.fitness = np.inf
        self.shape = shape

    def new(self):
        self.genes = [Gene().new(self.shape) for _ in range(self.genes_no)]
        return self

    def crossover(self, parents):
        self.genes = [Gene().recombine(p) for p in zip(parents[0].genes,parents[1].genes)]
        return self

    def mutate(self, rate):
        [gene.mutate(rate=rate) for gene in self.genes]

    def render(self):
        phenotype = np.zeros(self.shape, dtype=np.uint8)+255
        # [cv2.fillPoly(image,[gene.sequence.reshape(3, 2)], gene.fill) for gene in self.genes]
        [gene.express(phenotype) for gene in self.genes]
        return np.array(phenotype, dtype=np.uint8)

    def __str__(self) -> str:
        return str(self.fitness)

