import numpy as np
import cv2

class Gene:

    def __init__(self, length=3):
        self.length = length
        self.sequence = np.zeros(6)
        self.fill = tuple(np.random.uniform(0, 255, 3))
        self.expressed = False

    def new(self, shape):
        # x_points = np.random.uniform(0, shape[1], 3).astype(np.int32)
        # y_points = np.random.uniform(0, shape[0], 3).astype(np.int32)
        x_pt = np.random.uniform(0, shape[1], 1).astype(np.int32)
        y_pt = np.random.uniform(0, shape[0], 1).astype(np.int32)
        # self.sequence = (np.dstack((x_pt,y_pt))[0]).reshape(4)
        self.sequence = np.array([x_pt, y_pt,x_pt+1,y_pt+1]).flatten()
        self.fill = tuple(np.random.uniform(0, 255, 4).astype(np.uint8))
        self.expressed = np.random.rand() < .1
        return self

    def recombine(self, parent):
        self.sequence = np.random.choice(parent).sequence
        self.fill = np.random.choice(parent).fill
        self.expressed = np.random.choice(parent).expressed
        return self

    def mutate(self, rate):
        if self.expressed:
            self.sequence = np.array([p if np.random.rand() >= rate else int(p+np.random.normal(0, 1)) for p in self.sequence.flatten()]).astype(np.int32)
            self.fill = tuple([i if np.random.rand() >= rate else int(i+np.random.normal(0, 1)) for i in self.fill])
        self.expressed = self.expressed if np.random.rand() > rate else not self.expressed

    def express(self, genotype):
        if self.expressed:
            self.box(genotype)
        # if self.expressed:
            # cv2.rectangle(image, pt1=tuple(self.sequence[0:2]),pt2=tuple(self.sequence[2:4]), color=self.fill,thickness=-1)
        # transcription.rectangle(self.sequence,self.fill)


    def box(self, genotype):
        genotype[self.sequence[1]:self.sequence[3],self.sequence[0]:self.sequence[2]] = self.fill[0:3]

    def __str__(self) -> str:
        return self.sequence.__str__()

