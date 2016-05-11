import sys
import re

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

def parseFile(infile):
    x1_vals = []
    x2_vals = []
    z_vals = []
    labels = 1
    for line in open(infile, 'r'):
        values = (re.findall('[a-zA-Z0-9\.-]+', line))
        if labels == 0:
            x1_vals.append(float(values[0]))
            x2_vals.append(float(values[1]))
            z_vals.append(float(values[2]))
        else:
            # no toma los labels
            labels = 0
    return x1_vals,x2_vals,z_vals

def plotX1X2Z(x1,x2,z):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x1, x2, z, c='r', marker='o')
    ax.set_xlabel('X1')
    ax.set_ylabel('X2')
    ax.set_zlabel('Z')
    plt.show()
    return

# print('archivo de entrada:', sys.argv[1])
# x1, x2, z = parseFile(sys.argv[1])
# plotX1X2Z(x1, x2, z)