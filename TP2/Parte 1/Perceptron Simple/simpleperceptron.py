import argparse
import numpy as np
import numpy.matlib
import math as m

def simple_perceptron(args):
    bias = -1
    beta = 0.5

    inputs = np.array(transform_into_matrix(args.inputs))
    outputs = np.array(transform_into_matrix(args.outputs))

    print('Cantidad de entradas ' + str(inputs[0].size))
    print('Cantidad de patrones ' + str(inputs.itemsize))

    #Matriz de pesos
    weights = np.random.rand(inputs[0].size + 1, outputs[0].size)

    for i in range(0,args.iterations):
        out = np.zeros((inputs.itemsize,outputs[0].size))
        for j in range(0,inputs.itemsize):
            values = np.append(inputs[j],bias)
            h_val = h(values,weights)
            out[j] = g(h_val[0],beta)
            delta = outputs[j] - out[j]
            weights = new_weights(args.eta,delta,values,weights)
    print('Salidas obtenidas')
    print(out)
    print('Matriz de pesos')
    print(weights)
    return

def h(neurons,weights):
    return np.dot(neurons,weights)

def g(h,beta):
    return 1 / (1 + m.exp(- 2 * beta * h))

def new_weights(eta,delta,neurons,weights):
    neurons_aux = np.mat(neurons).transpose()
    return weights + neurons_aux * eta * delta

def transform_into_matrix(str_vals):
    rows = str_vals.split(';')
    matrix = []
    for i in range(0,len(rows)):
        int_list = transform_int(rows[i])
        matrix.append(int_list)
    return matrix


def transform_int(row):
    items = row.split(' ')
    return list(map(int,items))

def parse_arguments():
	parser = argparse.ArgumentParser()
	parser.add_argument("-I", "--inputs", type=str,  help="Entradas", required=True)
	parser.add_argument("-O", "--outputs", type=str , help="Salidas esperadas", required=True)
	parser.add_argument("-G", "--g_fun", type=str, help="Funcion de transferencia",choices=['escalon', 'sigmoidea', 'umlogico'],  required=True)
	parser.add_argument("-It", "--iterations", type=int, help="Cantidad de iteraciones", required=True)
	parser.add_argument("-eta", "--eta", type=float, help="Coeficiente de aprendizaje", required=True)

	return parser.parse_args()

def main():
	args = parse_arguments()
	simple_perceptron(args)


if __name__ == "__main__": main()

