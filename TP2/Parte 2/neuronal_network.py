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
# alfa = 0.9
# a = 0.5
# b = 0.2
# k = racha
def multilayer_perceptron(arquitecture,input,output,bias,beta,eta,error_cuad,fun,norm,alfa,a,b,k):

    np_input = np.array(input)

    if norm == 1:
        np_output = normalize(output, beta, fun)
    else:
        np_output = np.array(output)

    #1. Inicializo las matrices de pesos con valores random pequeños
    weights = initialize_weights(arquitecture)
    # esta es la lista de deltas previos que utilizo para el MOMENTUM
    deltas_prev = [0] * len(weights)
    # error cuadratico previo es el error del paso anterior que utilizo para el eta adaptativo.
    # en conjunto con el valor de k, voy deperminando si tengo que modificar el valor de eta
    ecm_prev = 0
    # k_counter es un contador para la CONSISTENCIA de la adaptacion del valor de eta
    k_counter = 0
    # guardo el valor de alfa en otra variable para cuando tenga que volvera su valor a alfa
    alfa_value_backup = alfa

    # esta es la lista de deltas previos auxiliar que utilizo para el eta adaptativo
    deltas_prev_aux = [0] * len(weights)
    error = 1

    # Array que lleva los valores de los errores cuadrático medios para cada patron
    errors = []

    it = 1
    not_reduce_eta = 1

    while error > error_cuad:
        print('COMIENZO DE CICLO')
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

                # Si estoy normalizando, los V de la capa final son g(h)
                if norm == 1:
                    if fun == 'exp':
                        vs.append(exp(hs[m], beta))
                    else:
                        vs.append(tan(hs[m], beta))
                # Si no estoy normalizando, los V de la capa final son h
                else:
                    # if m == (len(arquitecture) - 1):
                    #     vs.append(hs[m])
                    # else:
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
            #print('ECM del patron ' + str(u) + ': ' + str(ecm))


            if ecm_prev == 0:
                ecm_prev = ecm
                # good_step = 1
            else:
                if((ecm - ecm_prev) < 0 ):
                    k_counter = k_counter + 1
                    alfa = alfa_value_backup
                    if(k_counter >= k):
                        eta = eta + a
                    # good_step = 1
                    not_reduce_eta = 1
                elif((ecm - ecm_prev) > 0 and not_reduce_eta):
                    eta = eta - b*eta
                    alfa = 0
                    k_counter = 0
                    # good_step = 0
                    not_reduce_eta = 0
                # else:
                #     eta = 0
                ecm_prev = ecm

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
                new_weights[i], deltas_prev[i] = get_new_weights(weights[i],vs_copy,deltas_copy, deltas_prev[i], alfa)

            weights = new_weights

        errors.append(ecm)
        error = ecm
        print('ECM de corrida ' + str(it) + ': ' + str(ecm))
        it += 1

    print(errors)

    print('Salidas obtenida | Salidas esperada')
    for j in range(len(out)):
        print(str(out[j]),'||', str(output[j]))

    # plt.plot(range(1,it),errors)
    # plt.xlabel('Iteración')
    # plt.ylabel('Error cuadrático medio')
    # plt.title('Red neuronal con arquitectura ' + str(arquitecture) + ', cantidad de patrones: 20, función de activación: ' + fun)
    # plt.show()

    return errors, weights, out



def initialize_weights(arquitecture):
    weights = []

    i = 0
    while ( i + 1 ) < len(arquitecture):
        weights.append(np.random.rand(arquitecture[i] + 1, arquitecture[i+1]))
        i += 1
    print('pesos iniciales: ',weights)
    return weights

def h(vs,weights):
    return np.dot(vs, weights)

def normalize(array,beta,fun):
    normalized_out = np.array([])

    for i in range(0,len(array)):
        num = array[i]

        if fun == 'exp':
            normalized_out = np.append(normalized_out,1 / (1 + m.exp(- 2 * beta * num)))
        else:
            normalized_out = np.append(normalized_out, 1 / (1 + m.tanh(beta * num)))

    normalized_out = np.mat(normalized_out).transpose()
    return np.asarray(normalized_out)

def exp(hs,beta):
    l = np.array([(1 / (1 + m.exp(- 2 * beta * i))) for i in hs])
    return l

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

def get_new_weights(weights,vs,deltas, deltas_prev, alfa):
    vs_deltas_m = np.multiply(vs,deltas)
    delta_alfa = np.multiply(deltas_prev,alfa)
    # el termino delta_alfa es el termino de momentum
    return np.asarray(weights + vs_deltas_m + delta_alfa), vs_deltas_m

def neuronal_network():
   errors_tan = multilayer_perceptron([2,5,1],[[1,1],[2,1],[3,1],[4,1],[5,1],[6,1],[7,1],[8,1],[9,1],[10,1]],[[2],[3],[4],[5],[6],[7],[8],[9],[10],[11]],-1,0.5,0.3,0.0005,'tan',1)
   errors_exp = multilayer_perceptron([2, 5, 1], [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1], [10, 1]],[[2], [3], [4], [5], [6], [7], [8], [9], [10], [11]], -1, 0.5, 0.3, 0.0005, 'exp',1)

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

# FUNCION PARA PROBAR CON LOS PATRONES DE PRUEBA
# ==============================================
# COMO PARAMETRO RECIBE LOS PESOS(W) CALCULADOS
def mp_test(arquitecture, input, output, bias, beta, eta, error_cuad, fun, norm, weights):
   salidas_obtenidas = []
   np_input = np.array(input)

   # u : patron que estoy analizando
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

           # Si estoy normalizando, los V de la capa final son g(h)
           if norm == 1:
               if fun == 'exp':
                   vs.append(exp(hs[m], beta))
               else:
                   vs.append(tan(hs[m], beta))
           # Si no estoy normalizando, los V de la capa final son h
           else:
               if m == (len(arquitecture) - 1):
                   vs.append(hs[m])
               else:
                   if fun == 'exp':
                       vs.append(exp(hs[m], beta))
                   else:
                       vs.append(tan(hs[m], beta))

           m += 1

       # M : Ultima capa -> Capa de salida
       M = m - 1

   return

               # https: // mattmazur.com / 2015 / 03 / 17 / a - step - by - step - backpropagation - example /
# multilayer_perceptron([2,5,1],[[0.8010,0.8794],
#                                [0.8010,-0.1999],
#                                [-0.6339,-1.9764],
#                                [1.9191,0],
#                                [-1.4482,1.2694],
#                                [-0.9249,-1.7458],
#                                [1.3614,1.2694],
#                                [-1.9888,-0.1999],
#                                [0.4345,-1.8447],
#                                [-0.1989,-1.9764],
#                                [1.3085, -1.0446],
#                                [1.9191, 0.3689],
#                                [-0.1989, -0.3841],
#                                [0, -0.6568],
#                                [-0.6339, -1.1440],
#                                [1.5867, -0.6568],
#                                [-0.1989, 1.2694],
#                                [-1.0969, 1.9573],
#                                [-1.4482, 1.0199],
#                                [0.6109, -0.3841]],
#                             [[0.3579],[-0.2113],[-0.0256],[0],[0.0501],[-0.0394],[0.0624],[-0.0072],[-0.0535],[-0.0338],[-0.1049],[0.0145],[-0.6051],[-0.7215],[-0.3549],[-0.0621],[0.3555],[0.0127],[0.0675],[-0.4310]],-1,0.5,0.3,0.00001,'tan',0)