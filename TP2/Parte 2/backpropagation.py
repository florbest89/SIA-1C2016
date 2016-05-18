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
# alfa = 0.9
# a = 0.5
# b = 0.2
# k = racha
def multilayer_perceptron(arquitecture, input, output, bias, beta, eta, error_cuad, fun,alfa,a,b,k):

    start_time = time.time()

    np_input = normalize(input, beta, fun)
    np_output = normalize(output, beta, fun)
    #np_output = normalize_out(output, beta, fun)

    #1. Inicializo las matrices de pesos con valores random pequeños
    weights = initialize_weights(arquitecture)

    # esta es la lista de deltas previos que utilizo para el MOMENTUM
    deltas_prev = [0] * len(weights)
    deltas_good_epoch = deltas_prev
    # error cuadratico previo es el error del paso anterior que utilizo para el eta adaptativo.
    # en conjunto con el valor de k, voy deperminando si tengo que modificar el valor de eta
    ecm_prev = 0
    # k_counter es un contador para la CONSISTENCIA de la adaptacion del valor de eta
    k_counter = 0
    # guardo el valor de alfa en otra variable para cuando tenga que volvera su valor a alfa
    alfa_value_backup = alfa

    # esta es la lista de deltas previos auxiliar que utilizo para el eta adaptativo
    weights_prev_aux = [0] * len(weights)

    error = 1

    # Array que lleva los valores de los errores cuadrático medios para cada patron
    errors = []

    epoch = 1
    not_reduce_eta = 1

    # me guardo los pesos para luego cuando tenga que reducir el eta, coloco el peso
    # de la epoca anterior
    weights_prev_aux = weights

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
                # new_weights[i] = get_new_weights(weights[i], vs_copy, deltas_copy)
                new_weights[i], deltas_prev[i] = get_new_weights(weights[i], vs_copy, deltas_copy, deltas_good_epoch[i], alfa)

            weights = new_weights

        dt, ecm_epoch = error_quad(out, np_output)
        errors.append(ecm_epoch)
        error = ecm_epoch

        if ecm_prev == 0:
            ecm_prev = ecm_epoch
            # good_step = 1
        else:
            if ((ecm_epoch - ecm_prev) < 0):
                k_counter = k_counter + 1
                alfa = alfa_value_backup
                not_reduce_eta = 1
                weights_prev_aux = weights
                ecm_prev = ecm_epoch
                deltas_good_epoch = deltas_prev
                if (k_counter >= k):
                    eta = eta + a
                    print('k_counter: ', k_counter, ' valor eta: ', eta)
                # good_step = 1
            elif ((ecm_epoch - ecm_prev) > 0):
            # elif ((ecm_epoch - ecm_prev) > 0 and not_reduce_eta):
                eta = eta - b * eta
                print('valor de eta:', eta)
                alfa = 0
                k_counter = 0
                # good_step = 0
                weights = weights_prev_aux
                not_reduce_eta = 0
            elif (ecm_epoch - ecm_prev) > 0.000001:
                print('errores iguales')
            # else:
            #     eta = 0
            # ecm_prev = ecm_epoch


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

    plt.plot(range(1,epoch),errors)
    plt.xlabel('Iteración')
    plt.ylabel('Error cuadrático medio')
    plt.title('Red neuronal con arquitectura ' + str(arquitecture) + ', cantidad de patrones: 20, función de activación: ' + fun)
    plt.show()

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


def normalize(array, beta, fun):
    normalized_input = np.array([])

    num = array[0]

    if fun == 'exp':
        normalized_input = np.append(normalized_input, [(1 / (1 + m.exp(- 2 * beta * x))) for x in num])
    else:
        normalized_input = np.append(normalized_input, [(m.tanh(beta * x)) for x in num])

    for i in range(1, len(array)):
        num = array[i]

        if fun == 'exp':
            normalized_input = np.vstack([normalized_input,[(1 / (1 + m.exp(- 2 * beta * x))) for x in num]])
        else:
            normalized_input = np.vstack([normalized_input, [(m.tanh(beta * x)) for x in num]])

    return normalized_input


def exp(hs,beta):
    return np.array([(1 / (1 + m.exp(- 2 * beta * i))) for i in hs])


def exp_derived(hs, beta):
    #g'(h) = 2βg(1 − g).
    gs = exp(hs,beta)
    gs_g = exp([(1 - x) for x in gs],beta)
    return np.array([(2 * beta * g) for g in gs_g])


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

def get_new_weights(weights,vs,deltas, deltas_prev, alfa):
    vs_deltas_m = np.multiply(vs,deltas)
    delta_alfa = np.multiply(deltas_prev,alfa)
    # el termino delta_alfa es el termino de momentum
    return np.asarray(weights + vs_deltas_m + delta_alfa), vs_deltas_m