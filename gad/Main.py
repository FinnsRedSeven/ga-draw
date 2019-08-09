import gad
import cv2
from PIL import Image
import numpy as np


# 4 stages
# 1. populations
# 2. selection
# 3. crossover
# 4. mutation



def load_image(path, width, height):
    image = Image.open(path,'r')
    image.thumbnail((width, height), Image.ANTIALIAS)
    numpy_image = np.array(image)
    rbg_reversed = cv2.cvtColor(numpy_image, cv2.COLOR_RGB2BGR)
    return rbg_reversed



if __name__ == '__main__':
    image = load_image("images/image_two_mona_lisa.jpg", 500, 500)
    ga = gad.GeneticAlgorithm.GeneticAlgorithm(image,size=10)
    ga.start(1)
    cv2.imshow("Comparisons", np.concatenate([image, ga.show_fitness(ga.best())], axis=1))
    cv2.waitKey()

