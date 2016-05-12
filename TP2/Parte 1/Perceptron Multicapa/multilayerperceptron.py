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

def multilayer_perceptron(arquitecture,input,output,bias,fun,eta,error_cuad):
    np_input = np.array(input)
    np_output = np.array(output)

    #1. Inicializo las matrices de pesos con valores random pequeños
    weights = initialize_weights(arquitecture)

    error = 1

    # Array que lleva los valores de los errores cuadrático medios para cada patron
    errors = []

    while error > error_cuad:
        print('error: ', error, 'error_cuad: ',error_cuad)
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
                hs.append(h(np.append(np.array(vs[m-1]), bias), weights[m-1]))

                if fun == 'sgm':
                    vs.append(sigm(hs[m]))
                elif fun == 'esc':
                    vs.append(escalon(hs[m]))
                elif fun == 'linear':
                    vs.append(linear(hs[m]))

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

            gs_derived = np.array([])

            if fun == 'sgm':
                gs_derived = sigm_derived(hs[M])
            elif fun == 'esc':
                gs_derived = escalon_derived(hs[M])
            elif fun == 'linear':
                gs_derived = linear_derived(hs[M])

            deltas_output = [a * b for a,b in zip(gs_derived,deltas_error)]
            deltas[m] = deltas_output

            # 5. Calculo los deltas para capas anteriores
            while m - 1 >= 0:
                wt = weights_trans(weights[m])
                deltas[m-1] = get_deltas(hs[m],fun,deltas[m],wt)
                m -= 1

            # 6. Actualizo los pesos
            m = M - 1

            new_weights = [None] * len(weights)

            for i in range(0,M):
                rows, cols = weights[i].shape
                vs_copy = create_vs_transpose(vs[i], bias, cols)
                deltas_copy = create_deltas_matrix(deltas[i],eta,rows)
                new_weights[i] = get_new_weights(weights[i],vs_copy,deltas_copy)

            weights = new_weights

        errors.append(ecm)
        error = ecm
        print('ecm = ' + str(error))

    print('Expected output')
    print(np_output)
    print('Obtained output')
    print(out)
    plt.plot(errors)
    plt.show()



def initialize_weights(arquitecture):
    weights = []

    i = 0
    while ( i + 1 ) < len(arquitecture):
        weights.append(np.random.rand(arquitecture[i] + 1, arquitecture[i+1]))
        i += 1

    return weights

def h(vs,weights):
    return np.dot(vs, weights)

def sigm(hs):
    return np.array([(1 / (1 + m.exp(-i))) for i in hs])

def sigm_derived(hs):
    s = sigm(hs)
    s_s = sigm([(1 - x) for x in s])
    return np.array(s_s)

def escalon(hs):
    # = np.array([])

    #for i in hs:
        #f i > 0.5:
            #result = np.append(result,1)
        #else:
            #result = np.append(result,0)

    #return result
    ex = np.sign(hs)

    return np.sign(hs)

def escalon_derived(hs):
    return np.array([(1) for i in hs])

def linear(hs):
    return hs

def linear_derived(hs):
    return np.array([(1) for i in hs])

def g(hs,beta):
    return np.array([(1 / (1 + m.exp(- 2 * beta * i))) for i in hs])

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

def get_deltas(hs,fun,delta_upper,weights):
    gs_derived = np.array([])

    if fun == 'sgm':
        gs_derived = sigm_derived(hs)
    elif fun == 'esc':
        gs_derived = escalon_derived(hs)
    elif fun == 'linear':
        gs_derived = linear_derived(hs)

    dterm = np.dot(delta_upper, weights)
    return [a * b for a,b in zip(gs_derived,dterm)]

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


# multilayer_perceptron([3,5,1],[[1,1,1],[0,0,1],[0,1,1],[0,0,0]],[[0],[0],[1],[1]],-1,'linear',0.3,0.0001)






