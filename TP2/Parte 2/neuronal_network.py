import file_parser as fp
import backpropagation as bp
import matplotlib.pyplot as plt
import time

def learn():
    inputs, outputs = fp.parse_file('terrain/terrain5-1.txt', 50)
    start_time = time.time()
    print('INICIO DE ENTRENAMIENTO: ', start_time)
    errors, epoch = bp.multilayer_perceptron([2, 10, 5, 1], inputs,outputs, -1, 0.5, 0.6, 0.001, 'tan',0.9, 0.002, 0.005,10)
    print('FIN DE ENTRENAMIENTO: ', (time.time()-start_time))

    plt.plot(range(1, epoch), errors)
    plt.xlabel('Iteración')
    plt.ylabel('Error cuadrático medio')
    plt.title('Red neuronal con arquitectura ' + str([2, 10, 5, 1]) + ', cantidad de patrones: 20, función de activación: ' + 'tan')
    plt.show()

learn()