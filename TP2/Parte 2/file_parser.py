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
    #x1_vals = []
    #x2_vals = []
    #z_vals = out_values

    #for row in array_values:
    #    x1_vals.append(row[0])
    #    x2_vals.append(row[1])

    #fig = plt.figure()
    #ax = fig.add_subplot(111, projection='3d')
    #ax.scatter(x1_vals, x2_vals, z_vals, c='r', marker='o')
    #ax.set_xlabel('X1')
    #ax.set_ylabel('X2')
    #ax.set_zlabel('Z')
    #plt.show()
    #return
    x1_vals = []
    x2_vals = []
    z_vals = []
    # z_vals = out_values

    for i in range(0,len(array_values)):
        x1_vals.append(array_values[i][0])
        x2_vals.append(array_values[i][1])

    cols = len(out_values)

    for c in range(0,cols):
        z_vals.append(out_values[c])

    # fig = plt.figure()
    # ax = fig.add_subplot(111, projection='3d')
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.plot_trisurf(x1_vals, x2_vals, z_vals, cmap=cm.jet, linewidth=0.2)
    # ax.scatter(x1_vals, x2_vals, z_vals, c='r', marker='o')
    ax.set_xlabel('X1')
    ax.set_ylabel('X2')
    ax.set_zlabel('Z')
    plt.show()
    return

def plotOriginals(array_values, out_values):
    #x1_vals = []
    #x2_vals = []
    #z_vals = out_values

    #for row in array_values:
    #    x1_vals.append(row[0])
    #    x2_vals.append(row[1])

    #fig = plt.figure()
    #ax = fig.add_subplot(111, projection='3d')
    #ax.scatter(x1_vals, x2_vals, z_vals, c='r', marker='o')
    #ax.set_xlabel('X1')
    #ax.set_ylabel('X2')
    #ax.set_zlabel('Z')
    #plt.show()
    #return
    x1_vals = []
    x2_vals = []
    z_vals = []
    # z_vals = out_values

    for i in range(0,len(array_values)):
        x1_vals.append(array_values[i][0])
        x2_vals.append(array_values[i][1])

    cols = len(out_values)

    for c in range(0,cols):
        z_vals.append(out_values[c][0])

    # fig = plt.figure()
    # ax = fig.add_subplot(111, projection='3d')
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.plot_trisurf(x1_vals, x2_vals, z_vals, cmap=cm.jet, linewidth=0.2)
    # ax.scatter(x1_vals, x2_vals, z_vals, c='r', marker='o')
    ax.set_xlabel('X1')
    ax.set_ylabel('X2')
    ax.set_zlabel('Z')
    plt.show()
    return