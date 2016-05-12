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
    print('pase')
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

            vs.append(np_input[u])
            hs.append(np_input[u])

            # 3. Feed Forward
            # m : capa de la red
            m = 1
            while m < len(arquitecture):
                hs.append(h(np.append(np.array(vs[m-1]),bias),weights[m-1]))
                vs.append(g(hs[m],beta))
                m += 1

            # M : Ultima capa -> Capa de salida
            M = m - 1

            # Calculo del error
            deltas_error, ecm = error_quad(vs[M],np_output[u])
            errors.append(ecm)
            error = ecm

            # 4. Calculo los delta para la capa de salida
            m = M - 1
            deltas = [None] * M

            gs_derived = g_derived(hs[M],beta)
            deltas_output = [a * b for a,b in zip(gs_derived,deltas_error)]
            deltas[m] = deltas_output

            # 5. Calculo los deltas para capas anteriores
            while m - 1 >= 0:
                wt = weights_trans(weights[m])
                deltas[m-1] = get_deltas(hs[m],beta,deltas[m],wt)

            







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
    return np.array([(1 / (1 + m.exp(- 2 * beta * h))) for h in hs])

def g_derived(hs,beta):
    #g'(h) = 2βg(1 − g).
    gs = g(hs,beta)
    gs_g = g([(1 - x) for x in gs],beta)
    return np.array([(2 * beta * g) for g in gs_g])

def error_quad(out_obtained,out_expected):
    deltas_error = np.subtract(out_expected, out_obtained)
    pow_deltas = [(d ** 2) for d in deltas_error]
    sum_pow_deltas = np.sum(pow_deltas)
    return deltas_error, (1/2) * sum_pow_deltas

def weights_trans(weights):
    rows,cols = weights.shape
    aux = numpy.delete(weights, (rows - 1), axis=0)
    return aux.transpose()

def get_deltas(hs,beta,delta_upper,weights):
    gs = g_derived(hs,beta)
    dterm = np.dot(delta_upper, weights)
    return [a * b for a,b in zip(gs,dterm)]



# multilayer_perceptron([2,3,1],[[1,1],[1,0],[0,1],[0,0]],[[1],[1],[1],[0]],-1,0.5,0.001)





