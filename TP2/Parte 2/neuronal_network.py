# -*- coding: utf-8 -*-
import file_parser as fp
import backpropagation as bp
import matplotlib.pyplot as plt
import argparse

import numpy as np

def learn(args):

    # 1. Obtengo los patrones de entrenamiento
    inputs, outputs = fp.parse_file('terrains/terrain4-train-1.txt', -1)

    patterns = len(outputs)
    arquitecture = [2, args.hl1, args.hl2, 1]
    fun = args.g_fun
    ecm = args.ecm
    eta = args.eta
    alfa = args.alpha
    #los valores a,b,k en cero desactiva el eta adaptativo
    a = args.a
    b = args.b
    k = args.k

    # 2. Entreno la red
    #multilayer_perceptron(arquitecture, input, output, bias, beta, eta, error_cuad, fun, alfa, a, b, k):

    errors, epoch, out, weights = bp.train(arquitecture, inputs, outputs, -1, 0.5, eta, ecm, fun, alfa, a, b, k)
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
    plt.ylabel('Error cuadratico medio')

    plt.title('Red neuronal con arquitectura ' + str(arquitecture) + ', cantidad de patrones: ' + str(patterns) + ', función de activacion: ' + fun)
    plt.show()

    return


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-hl1", "--hl1", type=int, help="Arquitectura", required=True)
    parser.add_argument("-hl2", "--hl2", type=int, help="Arquitectura", required=True)
    parser.add_argument("-G", "--g_fun", type=str, help="Funcion de transferencia", choices=['exp', 'tan'],  required=True)
    parser.add_argument("-ecm", "--ecm", type=float, help="Error cuadratico medio", required=True)
    parser.add_argument("-eta", "--eta", type=float, help="Coeficiente de aprendizaje", required=True)
    parser.add_argument("-alpha", "--alpha", type=float, help="Momentum", required=True)
    parser.add_argument("-a", "--a", type=float, help="Eta adaptativo", required=True)
    parser.add_argument("-b", "--b", type=float, help="Eta adaptativo", required=True)
    parser.add_argument("-k", "--k", type=int, help="Eta adaptativo", required=True)
    return parser.parse_args()


def percentage(out_expected, out_obtained, error):

    hits = 0
    approx = 0

    total = len(out_expected)

    for i in range(0, total):
        delta = out_expected[i][0] - out_obtained[i]

        if delta < error:
            hits += 1
        else:
            approx += 1

    return (hits / total) * 100, (approx / total) * 100


def main():
    args = parse_arguments()
    learn(args)


if __name__ == "__main__":
    main()
