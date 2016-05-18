import file_parser as fp
import backpropagation as bp
import matplotlib.pyplot as plt

def learn():
    inputs, outputs = fp.parse_file('terrain/terrain5-4.txt', 50)
    errors, epoch = bp.multilayer_perceptron([2, 10, 5, 1], inputs,outputs, -1, 0.5, 0.5, 0.005, 'tan')

    plt.plot(range(1, epoch), errors)
    plt.xlabel('Iteración')
    plt.ylabel('Error cuadrático medio')
    plt.title('Red neuronal con arquitectura ' + str([2, 10, 5, 1]) + ', cantidad de patrones: 20, función de activación: ' + 'exp')
    plt.show()

learn()