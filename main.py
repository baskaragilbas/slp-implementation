import numpy as np
from module import SLP
from pathlib import Path

path = Path(__file__).parents[0]
file = str(path) + "\\Iris.csv"

data = np.genfromtxt(file, skip_header=True, delimiter=',')

slp1 = SLP(data,300,5,0.1) #data, epoch, k-fold, learning rate 0.1
slp2 = SLP(data,300,5,0.8) #data, epoch, k-fold, learning rate 0.8

#uncomment one only
#slp1.run()
slp2.run()