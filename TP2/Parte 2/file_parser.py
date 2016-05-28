import re
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
# import msvcrt

def parse_file(infile, number_of_values):

    values = []
    out_expected = []

    i = 0
    count = 0
    limit = number_of_values
    for line in open(infile, 'r'):
        val = re.findall('[a-zA-Z0-9\.-]+', line)
        if i == 1 and count < limit:
            values.append([float(val[0]), float(val[1])])
            out_expected.append([float(val[2])])
            count += 1
        if i == 1 and limit == -1:
            values.append([float(val[0]), float(val[1])])
            out_expected.append([float(val[2])])
        else:
            i = 1
    return values, out_expected


def plotX1X2Z(array_values, out_values):
    x1_vals = []
    x2_vals = []
    z_vals = []

    for i in range(0,len(array_values)):
        x1_vals.append(array_values[i][0])
        x2_vals.append(array_values[i][1])


    cols = len(out_values)

    for c in range(0,cols):
        z_vals.append(out_values[c])

    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.plot_trisurf(x1_vals, x2_vals, z_vals, cmap=cm.jet, linewidth=0.2)
    ax.set_xlabel('X1')
    ax.set_ylabel('X2')
    ax.set_zlabel('Z')

    plt.show()
    # return

def plotOriginals(array_values, out_values):
    x1_vals = []
    x2_vals = []
    z_vals = []

    for i in range(0,len(array_values)):
        x1_vals.append(array_values[i][0])
        x2_vals.append(array_values[i][1])

    cols = len(out_values)

    for c in range(0,cols):
        z_vals.append(out_values[c][0])

    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.plot_trisurf(x1_vals, x2_vals, z_vals, cmap=cm.jet, linewidth=0.2)
    ax.set_xlabel('X1')
    ax.set_ylabel('X2')
    ax.set_zlabel('Z')
    plt.show()
    return

def plotTerrainAndErrors(array_values, out_values,errors):
    x1_vals = []
    x2_vals = []
    z_vals = []

    for i in range(0,len(array_values)):
        x1_vals.append(array_values[i][0])
        x2_vals.append(array_values[i][1])

    cols = len(out_values)

    for c in range(0,cols):
        z_vals.append(out_values[c])

    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.plot_trisurf(x1_vals, x2_vals, z_vals, cmap=cm.jet, linewidth=0.2)
    ax.set_xlabel('X1')
    ax.set_ylabel('X2')
    ax.set_zlabel('Z')

    ax2 = fig.add_subplot(122)
    ax2.plot(errors)
    ax2.set_xlabel('Iteracion')
    ax2.set_ylabel('Error cuadratico medio')
    plt.show()
    return

def doThePlot(array_values, out_values,errors,trisurf_frame,ax,ax2):
    x1_vals = []
    x2_vals = []
    z_vals = []

    for row in array_values:
        x1_vals.append(row[0])
        x2_vals.append(row[1])

    for r in out_values:
        z_vals.append(r)

    oldcol = trisurf_frame
    trisurf_frame = ax.plot_trisurf(x1_vals, x2_vals, z_vals, cmap=cm.jet, linewidth=0.2)

    ax2.clear()
    ax2.plot(errors)
    ax2.set_xlabel('Iteracion')
    ax2.set_ylabel('Error cuadratico medio')

    # Borra el grafico anterior
    if oldcol is not None:
        ax.collections.remove(oldcol)

    plt.pause(.01)
    #Este valor que retorna es para borrar el grafico anterior cuando vuelva a entrar a este metodo
    return trisurf_frame