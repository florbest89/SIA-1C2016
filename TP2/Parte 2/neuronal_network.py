import file_parser as fp
import backpropagation as bp
import matplotlib.pyplot as plt

import numpy as np


def learn():

    # 1. Obtengo los patrones de entrenamiento
    inputs, outputs = fp.parse_file('terrains/terrain4-train-1.txt', -1)

    patterns = len(outputs)
    arquitecture = [2, 9, 4, 1]
    fun = 'exp'
    ecm = 0.001
    eta = 0.7

    # 2. Entreno la red
    #multilayer_perceptron(arquitecture, input, output, bias, beta, eta, error_cuad, fun, alfa, a, b, k):
    errors, epoch, out, weights = bp.train(arquitecture, inputs, outputs, -1, 0.5, eta, ecm, fun, 0, 0,0,0)
    fp.plotX1X2Z(inputs, out)
    #fp.plotOriginals(inputs,outputs)

    # 3. Obtengo los patrones de testeo
    inputs, outputs = fp.parse_file('terrains/terrain4-test-1.txt', -1)

    # 4. Testeo la red
    out = bp.test(arquitecture, inputs, outputs, -1, 0.5, eta, fun, weights)
    # 5. Calculo porcentaje de aciertos y aproximaciones
    hit_p, apprx_p = percentage(outputs, out, ecm)

    print('Porcentaje de aciertos: ' + "%.2f" % round(hit_p,2) + '% - Porcentaje de aproximaciones: ' + "%.2f" % round(apprx_p,2) + '%')


    fp.plotX1X2Z(inputs, out)
    #fp.plotOriginals(inputs, outputs)


    plt.plot(range(1, epoch), errors)
    plt.xlabel('Epoca')
    plt.ylabel('Error cuadrático medio')

    plt.title('Red neuronal con arquitectura ' + str(arquitecture) + ', cantidad de patrones: ' + str(patterns) + ', función de activación: ' + fun)
    plt.show()

    return


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

def percentage(out_expected, out_obtained, error):

    hits = 0;
    approx = 0;

    total = len(out_expected)

    for i in range(0,total):
        delta = out_expected[i][0] - out_obtained[i]

        if delta < error:
            hits += 1
        else:
            approx += 1

    return (hits / total) * 100, (approx / total) * 100

learn()