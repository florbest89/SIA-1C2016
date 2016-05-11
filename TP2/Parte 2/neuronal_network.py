import argparse
import numpy as np
import numpy.matlib
import math as m
import matplotlib.pyplot as plt

# arquitecture : Arquitectura de la red -> Cantidad de nodos
# input : Array con valores de entrada
# output : Array con valores de salida esperadas
# bias : -1
# error_cuad : error cuadrático medio
# beta = 0.5
def multilayer_perceptron(arquitecture,input,output,bias,beta,eta,error_cuad,fun):

    np_input = np.array(input)
    #np_output = np.array(output)
    np_output = normalize(output,beta,fun)

    #1. Inicializo las matrices de pesos con valores random pequeños
    weights = initialize_weights(arquitecture)

    error = 1

    # Array que lleva los valores de los errores cuadrático medios para cada patron
    errors = []

    while error > error_cuad:
        #out = np.zeros((np_input.itemsize,np_output[0].size))
        out = np.array([])

        # u : patron que estoy analizando
        limit,col = np_input.shape
        for u in range(0,limit):

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

                if fun == 'exp':
                    vs.append(exp(hs[m], beta))
                else:
                    vs.append(tan(hs[m], beta))

                m += 1

            # M : Ultima capa -> Capa de salida
            M = m - 1

            out = np.insert(out,u,vs[M])

            # Calculo del error
            deltas_error, ecm = error_quad(vs[M],np_output[u])
            print(ecm)

            # 4. Calculo los delta para la capa de salida
            m = M - 1
            deltas = [None] * M

            if fun == 'exp':
                gs_derived = exp_derived(hs[M], beta)
            else:
                gs_derived = tan_derived(hs[M], beta)

            deltas_output = [a * b for a,b in zip(gs_derived,deltas_error)]
            deltas[m] = deltas_output

            # 5. Calculo los deltas para capas anteriores
            while m - 1 >= 0:
                wt = weights_trans(weights[m])
                deltas[m-1] = get_deltas(hs[m],beta,deltas[m],wt,fun)
                m -= 1

            # 6. Actualizo los pesos
            m = M - 1

            new_weights = [None] * len(weights)

            #while m >= 0:
                #rows, cols = weights[m].shape
                #vs_copy = create_vs_transpose(vs[m], bias, cols)
                #deltas_copy = create_deltas_matrix(deltas[m],eta,rows)
                #new_weights[m] = get_new_weights(weights[m],vs_copy,deltas_copy)
                #m-=1
            for i in range(0,M):
                rows, cols = weights[i].shape
                vs_copy = create_vs_transpose(vs[i], bias, cols)
                deltas_copy = create_deltas_matrix(deltas[i],eta,rows)
                new_weights[i] = get_new_weights(weights[i],vs_copy,deltas_copy)

            weights = new_weights

        errors.append(ecm)
        error = ecm

    #print('Expected output')
    #print(np_output)
    #print('Obtained output')
    #print(out)
    #plt.plot(errors)
    #plt.show()

    return errors



def initialize_weights(arquitecture):
    weights = []

    i = 0
    while ( i + 1 ) < len(arquitecture):
        weights.append(np.random.rand(arquitecture[i] + 1, arquitecture[i+1]))
        i += 1

    return weights

def h(vs,weights):
    return np.dot(vs, weights)

def normalize(array,beta,fun):
    normalized_out = np.array([])

    for i in range(0,len(array)):
        num = array[i][0]

        if fun == 'exp':
            normalized_out = np.append(normalized_out,1 / (1 + m.exp(- 2 * beta * num)))
        else:
            normalized_out = np.append(normalized_out, 1 / (1 + m.tanh(beta * num)))

    normalized_out = np.mat(normalized_out).transpose()
    return np.asarray(normalized_out)

def exp(hs,beta):
    return np.array([(1 / (1 + m.exp(- 2 * beta * i))) for i in hs])

def exp_derived(hs,beta):
    #g'(h) = 2βg(1 − g).
    gs = exp(hs,beta)
    gs_g = exp([(1 - x) for x in gs],beta)
    return np.array([(2 * beta * g) for g in gs_g])

def tan(hs,beta):
    return np.array([(m.tanh(beta * x)) for x in hs])

def tan_derived(hs,beta):
    gs = tan(hs,beta)
    gs_pow = [( x ** 2) for x in gs]
    return np.array([(beta * (1 - x)) for x in gs_pow])

def error_quad(out_obtained,out_expected):
    deltas_error = np.subtract(out_expected, out_obtained)
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

def get_new_weights(weights,vs,deltas):
    vs_deltas_m = np.multiply(vs,deltas)
    #return np.add(weights, vs_deltas_m)
    return np.asarray(weights + vs_deltas_m)

def neuronal_network():
   errors_tan = multilayer_perceptron([2,5,1],[[1,1],[2,1],[3,1],[4,1],[5,1],[6,1],[7,1],[8,1],[9,1],[10,1]],[[2],[3],[4],[5],[6],[7],[8],[9],[10],[11]],-1,0.5,0.3,0.0005,'tan')
   errors_exp = multilayer_perceptron([2, 5, 1], [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1], [10, 1]],[[2], [3], [4], [5], [6], [7], [8], [9], [10], [11]], -1, 0.5, 0.3, 0.0005, 'exp')

   plt.plot(range(1,len(errors_tan) +1),errors_tan, 'magenta')
   plt.xlabel('Iteraciones')
   plt.ylabel('Error cuadratico medio')
   plt.title('Funcion de activacion: tanh')
   plt.show()

   plt.plot(range(1,len(errors_exp) +1),errors_exp, 'magenta')
   plt.xlabel('Iteraciones')
   plt.ylabel('Error cuadratico medio')
   plt.title('Funcion de activacion: exp')
   plt.show()

neuronal_network()