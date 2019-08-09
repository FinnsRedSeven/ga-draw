import numpy as np
from PIL import Image

class Gene:

    def __init__(self, length=3):
        self.length = length

    def new(self,shape):
        x_points = np.random.uniform(0,shape[1],(3,1)).astype(np.int32)
        y_points = np.random.uniform(0,shape[0],(3,1)).astype(np.int32)
        self.sequence = np.concatenate([x_points,y_points],axis=1)
        self.fill = tuple(np.random.uniform(0,255,3))
        return self
