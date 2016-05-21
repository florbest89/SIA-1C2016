import file_parser as fp
import backpropagation as bp
import matplotlib.pyplot as plt

import numpy as np


def learn():

    inputs, outputs = fp.parse_file('terrain/terrain4.txt', 10)

    # Para graficar terreno
    #x, y = get_x_y(inputs)
    #z = get_z(outputs)

    #multilayer_perceptron(arquitecture, input, output, bias, beta, eta, error_cuad, fun, alfa, a, b, k):
    errors, epoch = bp.multilayer_perceptron([2, 20, 15, 1], inputs, outputs, -1, 0.5, 0.5, 0.03, 'exp', 0.9, 0,0,0)

    plt.plot(range(1, epoch), errors)
    plt.xlabel('Iteración')
    plt.ylabel('Error cuadrático medio')

    plt.title('Red neuronal con arquitectura ' + str([2, 20, 15, 1]) + ', cantidad de patrones: 150, función de activación: ' + 'tan')
    plt.show()


def get_x_y(input):
    x = []
    y = []
    size = len(input)

    for i in range(0, size):
        x.append(input[i][0])
        y.append(input[i][1])

    x = np.array(x)
    y = np.array(y)
    return x, y


def get_z(input):
    z = []
    size = len(input)

    for i in range(0, size):
        z.append(input[i][0])

    z = np.array(z)
    return z

learn()