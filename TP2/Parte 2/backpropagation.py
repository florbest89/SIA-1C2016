import argparse
import numpy as np
import numpy.matlib
import math as m
import matplotlib.pyplot as plt
import time

# arquitecture : Arquitectura de la red -> Cantidad de nodos
# input : Array con valores de entrada
# output : Array con valores de salida esperadas
# bias : -1
# error_cuad : error cuadrático medio
# beta = 0.5
def multilayer_perceptron(arquitecture, input, output, bias, beta, eta, error_cuad, fun):

    start_time = time.time()

    #np_input = normalize(input, beta, fun)
    #np_output = normalize(output, beta, fun)
    np_input, np_output = normalize(input,output,fun)

    #1. Inicializo las matrices de pesos con valores random pequeños
    weights = initialize_weights(arquitecture)

    error = 1

    # Array que lleva los valores de los errores cuadrático medios para cada patron
    errors = []

    epoch = 1
    while error > error_cuad:
        print('COMIENZO DE EPOCA')
        out = np.array([])

        # u : patron que estoy analizando
        limit,col = np_input.shape
        for u in range(0, limit):

            # 2. El patron de entrada seran los primeros V
            vs = []
            hs = []

            vs.append(np_input[u])
            hs.append(np_input[u])

            # 3. Feed Forward
            # m : capa de la red
            m = 1
            while m < len(arquitecture):
                hs.append(h(np.append(np.array(vs[m-1]), bias), weights[m-1]))

                # Si estoy normalizando, los V de la capa final son g(h)
                if fun == 'exp':
                    vs.append(exp(hs[m], beta))
                else:
                    vs.append(tan(hs[m], beta))

                m += 1

            # M : Ultima capa -> Capa de salida
            M = m - 1

            out = np.insert(out, u, vs[M])

            # Calculo del error
            deltas_error = calc_delta(vs[M], np_output[u])
            #print('ECM del patron ' + str(u) + ': ' + str(ecm))

            # 4. Calculo los delta para la capa de salida
            m = M - 1
            deltas = [None] * M

            if fun == 'exp':
                gs_derived = exp_derived(hs[M], beta)
            else:
                gs_derived = tan_derived(hs[M], beta)

            deltas_output = [a * b for a, b in zip(gs_derived,deltas_error)]
            deltas[m] = deltas_output

            # 5. Calculo los deltas para capas anteriores
            while m - 1 >= 0:
                wt = weights_trans(weights[m])
                deltas[m-1] = get_deltas(hs[m], beta, deltas[m], wt, fun)
                m -= 1

            # 6. Actualizo los pesos
            m = M - 1

            new_weights = [None] * len(weights)

            for i in range(0, M):
                rows, cols = weights[i].shape
                vs_copy = create_vs_transpose(vs[i], bias, cols)
                deltas_copy = create_deltas_matrix(deltas[i], eta, rows)
                new_weights[i] = get_new_weights(weights[i], vs_copy, deltas_copy)

            weights = new_weights

        dt, ecm_epoch = error_quad(out, np_output)
        errors.append(ecm_epoch)
        error = ecm_epoch
        print('ECM de corrida ' + str(epoch) + ': ' + str(ecm_epoch))
        print('Cantidad de patrones ' + str(u + 1))
        epoch += 1

    #print('Expected output')
    #print(np_output)
    #print('Obtained output')
    #print(out)
    print(errors)
    end_time = time.time()

    print('TIEMPO DE EJECUCION: ' + str(end_time - start_time) + 'segundos.')

    print('Salidas esperadas: ' + str(output))
    print('Salidas obtenidas: ' + str(out))

    return errors, epoch


def initialize_weights(arquitecture):
    weights = []

    i = 0
    while ( i + 1 ) < len(arquitecture):
        weights.append(np.random.rand(arquitecture[i] + 1, arquitecture[i+1]))
        i += 1

    return weights


def h(vs, weights):
    return np.dot(vs, weights)

def normalize(inputs, outputs, fun):
   max_x, max_y , max_z = get_max_values(inputs,outputs)

   norm_in = []
   norm_out = []

   limit = len(outputs)

   for i in range(0,limit):

       x = inputs[i][0] / max_x
       y = inputs[i][0] / max_y
       z = outputs[i][0] / max_z

       if fun == 'exp' :
           x = x * np.sign(x)
           y = y * np.sign(y)
           z = z * np.sign(z)

       norm_in.append([x,y])
       norm_out.append([z])

   return np.array(norm_in), np.array(norm_out)

def exp(hs,beta):
    return np.array([(1 / (1 + m.exp(- 2 * beta * i))) for i in hs])



def exp_derived(hs, beta):
    gs = exp(hs,beta)
    return np.array([(2 * beta * g * (1 - g)) for g in gs])


def tan(hs,beta):
    return np.array([(m.tanh(beta * x)) for x in hs])


def tan_derived(hs, beta):
    gs = tan(hs, beta)
    gs_pow = [(x ** 2) for x in gs]
    return np.array([(beta * (1 - x)) for x in gs_pow])


def calc_delta(out_obtained, out_expected):
    deltas_error = np.subtract(out_expected, out_obtained)
    return deltas_error


def error_quad(out_obtained, out_expected):
    out_expected_copy = out_expected.copy()
    out_expected_copy = np.mat(out_expected_copy).transpose()
    deltas_error = np.subtract(out_expected_copy, out_obtained)
    deltas_error = np.asarray(deltas_error)
    deltas_error = deltas_error[0]
    pow_deltas = [(d ** 2) for d in deltas_error]
    sum_pow_deltas = np.sum(pow_deltas)
    return deltas_error, (1/2) * sum_pow_deltas


def weights_trans(weights):
    rows,cols = weights.shape
    aux = numpy.delete(weights, (rows - 1), axis=0)
    return aux.transpose()


def get_deltas(hs,beta,delta_upper,weights,fun):
    if fun == 'exp':
        gs = exp_derived(hs, beta)
    else:
        gs = tan_derived(hs, beta)

    dterm = np.dot(delta_upper, weights)
    return [a * b for a,b in zip(gs,dterm)]


def create_vs_transpose(vs, bias, cols):
    vs_copy = vs.copy()

    vs_copy = np.append(vs_copy,bias)
    aux = vs_copy

    cols_count = 1

    while cols_count != cols:
        vs_copy = numpy.vstack([vs_copy, aux])
        cols_count += 1

    return np.mat(vs_copy).transpose()


def create_deltas_matrix(deltas,eta,rows):
    deltas_copy = deltas.copy()
    deltas_copy = [(d * eta) for d in deltas_copy]
    aux = deltas_copy.copy()

    rows_count = 1

    while rows_count != rows:
        deltas_copy = numpy.vstack([deltas_copy, aux])
        rows_count += 1

    return deltas_copy


def get_new_weights(weights, vs, deltas):
    vs_deltas_m = np.multiply(vs, deltas)
    #return np.add(weights, vs_deltas_m)
    return np.asarray(weights + vs_deltas_m)

def get_max_values(inputs,outputs):
    max_x = 0.0
    max_y = 0.0
    max_z = 0

    limit = len(outputs)

    for i in range(0,limit):

        x = inputs[i][0]
        y = inputs[i][1]
        z = outputs[i][0]

        if x > max_x :
            max_x = x

        if y > max_y :
            max_y = y

        if z > max_z :
            max_z = z

    # | x | , | y | , | z |
    return abs(max_x), abs(max_y) , abs(max_z)