import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import imread

np.random.seed(0)
x = [720.281573781,76.0382837186,52.6171444847 ]
y = [ 440.436162917,340.420376302, 262.707477827]
center = [100,200];
img = imread("data/USA_Counties.png")
plt.scatter(x,y,zorder=1, cmap = plt.get_cmap("viridis"))

for i in range(len(x)):
    k = [x[i],center[0]]
    j = [y[i],center[1]]
    plt.plot(k,j, marker = 'o', color = "green")
plt.scatter(center[0],center[1], s = 100, color="green")
plt.imshow(img,zorder=0)
plt.show()
