
from gad.Gene import Gene
from PIL import Image, ImageDraw
import numpy as np
import cv2


class Agent:

    def __init__(self, genes=3, shape=None):
        self.shape = shape
        self.genes = [Gene(3).new(shape) for _ in range(genes)]
        self.fitness = 0

    def mutate(self,rate):
        pass

    def render(self):

        image = np.zeros(self.shape,dtype=np.uint8)
        [cv2.fillPoly(image,[gene.sequence], gene.fill) for gene in self.genes]

        return image