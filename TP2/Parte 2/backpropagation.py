# -*- coding: utf-8 -*-
import copy
import argparse
import numpy as np
import numpy.matlib
import math as m
import matplotlib.pyplot as plt
import time
import file_parser as fp
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

# arquitecture : Arquitectura de la red -> Cantidad de nodos
# input : Array con valores de entrada
# output : Array con valores de salida esperadas
# bias : -1
# error_cuad : error cuadrático medio
# beta = 0.5
# alfa = 0.9

def train(arquitecture, input, output, bias, beta, eta, error_cuad, fun, alfa, a, b, k):
    bad_epoch = k

    # variables necesarias para plot en realtime
    fig = plt.figure(figsize=plt.figaspect(.2))
    # fig = plt.figure()
    ax = fig.add_subplot(1,2,1,projection='3d')
    # ax = fig.gca(projection='3d')
    trisurf_frame = None
    # ax2 = fig.add_subplot(122)
    ax2 = fig.add_subplot(1, 2, 2)

    start_time = time.time()

    np_input, np_output, max = normalize(input,output,fun)

    #1. Inicializo las matrices de pesos con valores random pequeños
    weights = initialize_weights(arquitecture)
    out_weights = copy.copy(weights)

    # esta es la lista de deltas previos que utilizo para el MOMENTUM
    deltas_prev = [0] * len(weights)


    # error cuadratico previo es el error del paso anterior que utilizo para el eta adaptativo.

    # En conjunto con el valor de k, voy determinando si tengo que modificar el valor de eta
    # k_counter es un contador para la CONSISTENCIA de la adaptacion del valor de eta
    k_counter = 0
    ecm_prev = 0

    # guardo el valor de alfa en otra variable para cuando tenga que volvera su valor a alfa
    alfa_value_backup = alfa

    error = 1

    # Array que lleva los valores de los errores cuadrático medios para cada patron
    errors = []

    epoch = 1

    while error > error_cuad:


        # Guardo los valores de los pesos en caso que hay que hacer backtracking
        weights_prev = copy.copy(weights)
        deltas_prev_aux = copy.copy(deltas_prev)
        deltas_prev_good_epoch = deltas_prev

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
                new_weights[i], deltas_prev[i] = get_new_weights(weights[i], vs_copy, deltas_copy, deltas_prev[i], alfa)

            out_weights = copy.copy(weights)
            weights = new_weights

        dt, ecm_epoch = error_quad(out, np_output)
        errors.append(ecm_epoch)
        error = ecm_epoch

        # INICIO eta_adaptativo
        if a > 0 and b > 0 and k > 0:
            if ecm_prev == 0:
                ecm_prev = ecm_epoch

            else:
                delta_error = ecm_epoch - ecm_prev
                if delta_error < 0:
                    k_counter += 1
                    alfa = alfa_value_backup
                    ecm_prev = ecm_epoch
                    bad_epoch = k
                    if k_counter == k:
                        k_counter = 0
                        eta += a
                        print('valor eta SUBE:', eta)
                elif delta_error > 0:
                    bad_epoch -= 1
                    alfa = 0
                    k_counter = 0
                    if bad_epoch == 0:
                        # alfa = 0
                        k_counter = 0
                        eta += - b * eta
                        bad_epoch = 6
                        weights = weights_prev
                        deltas_prev = deltas_prev_good_epoch
                        # ecm_prev = ecm_epoch
                        print('valor eta BAJA:', eta)
        # FIN eta_adaptativo

        # if a == 0 or b == 0:
        #     # errors.append(ecm_epoch)

        # CODIGO QUE PROBAMOS CON FLOR/MAX/YO
        # # inicio eta adaptativo
        # if ecm_prev > 0:
        #     derror = error - errors[epoch - 2]
        #
        #     # En caso de una epoca mala, debo decrementar el eta
        #     if derror > 0:
        #         eta += - b * eta
        #         alfa = 0
        #         k_counter = 0
        #         print('BAJA ETA. Eta = ' + str(eta))
        #
        #         # Hago backtracking
        #         weights = copy.copy(weights_prev)
        #         deltas_prev = deltas_prev_aux
        #         epoch -= 1
        #
        #     # En caso de una epoca buena, analizo si debo aumentar eta
        #     else:
        #
        #         k_counter += 1
        #         alfa = alfa_value_backup
        #         errors.append(ecm_epoch)
        #         ecm_prev = ecm_epoch
        #
        #         if k_counter == k:
        #             eta += a
        #             k_counter = 0
        #             print('SUBE ETA . Eta = ' + str(eta))
        # else:
        #     ecm_prev = error
        #     errors.append(ecm_epoch)
        # # fin eta adaptativo

        print('ECM de corrida ' + str(epoch) + ': ' + str(error))
        epoch += 1

        # Desnormalizo
        out_un = unnormalize(out, output, max, fun)
        trisurf_frame = fp.doThePlot(input, out_un,errors,trisurf_frame,ax,ax2)
        # fp.plotTerrainAndErrors(input, out_un, errors)

    end_time = time.time()
    print('TIEMPO DE EJECUCION: ' + str(end_time - start_time) + ' segundos.')

    # Desnormalizo
    # out_un = unnormalize(out,output,max,fun)

    return errors, epoch, out_un, out_weights

# TESTEO
def test(arquitecture, input, output, bias, beta, eta, fun,trained_weights):
    start_time = time.time()

    np_input, np_output, max = normalize(input, output, fun)

    # 1. Inicializo las matrices de pesos con valores random pequeños
    weights = trained_weights

    out = np.array([])

    # u : patron que estoy calculando
    limit, col = np_input.shape
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
            hs.append(h(np.append(np.array(vs[m - 1]), bias), weights[m - 1]))

            if fun == 'exp':
                vs.append(exp(hs[m], beta))
            else:
                vs.append(tan(hs[m], beta))

            m += 1

        # M : Ultima capa -> Capa de salida
        M = m - 1

        # Agrego la salida obtenida al conjunto de salida
        out = np.insert(out, u, vs[M])

    end_time = time.time()



    print('TIEMPO DE TESTEO: ' + str(end_time - start_time) + ' segundos.')

    # Desnormalizo
    out_un = unnormalize(out, output, max, fun)

    return out_un

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

   max_val = max([max_x,max_y,max_z])

   for i in range(0,limit):
       x = inputs[i][0] / max_val
       y = inputs[i][1] / max_val
       z = outputs[i][0] / max_val
       if fun == 'exp' :
           x = x * np.sign(x)
           y = y * np.sign(y)
           z = z * np.sign(z)

       norm_in.append([x,y])
       norm_out.append([z])

   return np.array(norm_in), np.array(norm_out), max_val

def unnormalize(obtained,expected,max,fun):
    out_unnorm = []

    for i in range(0,len(expected)):
        o = obtained[i] * max

        if fun == 'exp':
            o = o * np.sign(expected[i][0])

        out_unnorm.append(o)

    return out_unnorm

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

    N = len(out_expected)

    out_expected_copy = out_expected.copy()
    out_expected_copy = np.mat(out_expected_copy).transpose()
    deltas_error = np.subtract(out_expected_copy, out_obtained)
    deltas_error = np.asarray(deltas_error)
    deltas_error = deltas_error[0]
    pow_deltas = [(d ** 2) for d in deltas_error]
    sum_pow_deltas = np.sum(pow_deltas)
    return deltas_error, sum_pow_deltas / (2 * N)

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
    # deltas_copy = deltas.copy()
    deltas_copy = copy.copy(deltas)
    deltas_copy = [(d * eta) for d in deltas_copy]
    # aux = deltas_copy.copy()
    aux = copy.copy(deltas_copy)

    rows_count = 1

    while rows_count != rows:
        deltas_copy = numpy.vstack([deltas_copy, aux])
        rows_count += 1

    return deltas_copy

def get_new_weights(weights, vs, deltas, deltas_prev, alfa):
    vs_deltas_m = np.multiply(vs, deltas)
    delta_alfa = np.multiply(deltas_prev, alfa)
    # print(deltas_prev)
    # delta_alfa = np.array([(d * alfa) for d in deltas_prev])
    # el termino delta_alfa es el termino de momentum
    return np.asarray(weights + vs_deltas_m + delta_alfa), vs_deltas_m
    # return np.asarray(weights + vs_deltas_m)

def get_max_values(inputs,outputs):
    max_x = 0.0
    max_y = 0.0
    max_z = 0.0

    limit = len(outputs)

    for i in range(0,limit):

        x = abs(inputs[i][0])
        y = abs(inputs[i][1])
        z = abs(outputs[i][0])

        if x > max_x :
            max_x = x

        if y > max_y :
            max_y = y

        if z > max_z :
            max_z = z

    # | x | , | y | , | z |
    return abs(max_x), abs(max_y) , abs(max_z)


    # INICIO eta_adaptativo
    # if a > 0 and b > 0 and k > 0:
    #     if ecm_prev == 0:
    #         ecm_prev = ecm_epoch
    #         # deltas_prev_aux = deltas_prev
    #     else:
    #         delta_error = ecm_epoch - ecm_prev
    #         if delta_error < 0:
    #             k_counter += 1
    #             ecm_prev = ecm_epoch
    #             alfa = alfa_value_backup
    #             # deltas_prev_aux = deltas_prev
    #             if k_counter > k:
    #                 k_counter = 0
    #                 eta += a
    #                 alfa = alfa_value_backup
    #                 print('valor eta SUBE:', eta)
    #         elif delta_error > 0:
    #             eta += - b * eta
    #             alfa = 0
    #             k_counter = 0
    #             weights = weights_prev
    #             # deltas_prev = deltas_prev_aux
    #             print('valor eta BAJA:', eta)
    # FIN eta_adaptativo