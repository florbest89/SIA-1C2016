import file_parser as fp
import backpropagation as bp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from matplotlib import cm
import numpy as np


def learn():
    inputs, outputs = fp.parse_file('terrain/terrain5-1.txt', -1)

    fig = plt.figure()
    ax = fig.gca(projection='3d')
    x, y = getXandY(inputs)
    x, y = np.meshgrid(x, y)
    z = getZ(outputs)
    surf = ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap=cm.coolwarm,
                           linewidth=0, antialiased=False)
    ax.set_zlim(-1.01, 1.01)

    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

    fig.colorbar(surf, shrink=0.5, aspect=5)

    plt.show()

    errors, epoch = bp.multilayer_perceptron([2, 10, 5, 1], inputs, outputs, -1, 0.5, 0.5, 0.001, 'tan')

    plt.plot(range(1, epoch), errors)
    plt.xlabel('Iteración')
    plt.ylabel('Error cuadrático medio')
    plt.title('Red neuronal con arquitectura ' + str([2, 10, 5, 1]) + ', cantidad de patrones: 20, función de activación: ' + 'tan')
    plt.show()


def getXandY(input):
    x = []
    y = []
    size = len(input)

    for i in range(0, size):
        x.append(input[i][0])
        y.append(input[i][1])

    x = np.array(x)
    y = np.array(y)
    return x, y


def getZ(input):
    z = []
    size = len(input)

    for i in range(0, size):
        z.append(input[i][0])

    z = np.array(z)
    return z


learn()