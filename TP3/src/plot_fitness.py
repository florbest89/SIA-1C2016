import re
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm

def doThePlot(fitness_per_generation, avg_fitness_per_generation,ax,ax2):
    ax.clear()
    ax.plot(fitness_per_generation)
    ax.set_xlabel('Generación')
    ax.set_ylabel('Mejor fitness')
    ax.set_title('Mejor fitness por generacion')

    ax2.clear()
    ax2.plot(avg_fitness_per_generation)
    ax2.set_xlabel('Generación')
    ax2.set_ylabel('Promedio de fitness')
    ax2.set_title('Promedio de fitness por generacion')

    plt.pause(.01)
