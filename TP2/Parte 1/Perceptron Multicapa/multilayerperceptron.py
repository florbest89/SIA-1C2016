import argparse
import numpy as np
import numpy.matlib
import math as m

# arquitecture : Arquitectura de la red -> Cantidad de nodos
# input : Array con valores de entrada
# output : Array con valores de salida esperadas
# bias : -1
# error_cuad : error cuadrático medio
# beta = 0.5
def multilayer_perceptron(arquitecture,input,output,bias,beta,error_cuad):

    np_input = np.array(input)
    np_output = np.array(output)

    #1. Inicializo las matrices de pesos con valores random pequeños
    weights = initialize_weights(arquitecture)

    error = 1

    # Array que lleva los valores de los errores cuadrático medios para cada patron
    errors = []

    while error > error_cuad:
        out = np.zeros((np_input.itemsize,np_output[0].size))

        # u : patron que estoy analizando
        for u in range(0,np_input.itemsize):

            # 2. El patron de entrada seran los primeros V
            vs = []
            hs = []

            vs[0] = np_input[u]

            # 3. Feed Forward
            # m : capa de la red
            m = 1
            while m <= len(arquitecture):
                hs[m] = h(np.append(np.array(vs[m-1]),bias),weights[m-1])
                vs[m] = g(hs[m],beta)
                m += 1

            # M : Ultima capa -> Capa de salida
            M = m - 1

            # Calculo del error
            deltas_error, ecm = error(vs[M],np_output[u])
            errors.append(ecm)
            error = ecm


def initialize_weights(arquitecture):
    weights = []

    i = 0
    while ( i + 1 ) < len(arquitecture):
        weights.append(np.random.rand(arquitecture[i] + 1, arquitecture[i+1]))
        i += 1

    return weights

def h(vs,weights):
    return np.dot(vs, weights)

def g(hs,beta):
    return ((1 / (1 + m.exp(- 2 * beta * h))) for h in hs)

def error(out_obtained,out_expected):
    deltas_error = np.substract(out_expected, out_obtained)
    pow_deltas = ((d ** 2) for d in deltas_error)
    sum_pow_deltas = np.sum(pow_deltas)
    return deltas_error, (1/2) * sum_pow_deltas


multilayer_perceptron([2,3,1])





