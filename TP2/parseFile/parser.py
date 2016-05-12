import sys
import re

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

def parserFile(infile, number_of_values):
    values = []
    out_expected = []
    val = []
    i = 0
    count = 0
    limit = number_of_values
    print('value file: ', infile)
    for line in open(infile, 'r'):
        val = re.findall('[a-zA-Z0-9\.-]+', line)
        if  i == 1 and  count < limit:
            values.append([float(val[0]), float(val[1])])
            out_expected.append(float(val[2]))
            count = count + 1
        if i == 1 and limit == -1:
            values.append([float(val[0]), float(val[1])])
            out_expected.append(float(val[2]))
        else:
            i = 1
    return values,out_expected

def plotX1X2Z(array_values, out_values):
    x1_vals = []
    x2_vals = []
    z_vals = out_values

    for row in array_values:
        x1_vals.append(row[0])
        x2_vals.append(row[1])

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x1_vals, x2_vals, z_vals, c='r', marker='o')
    ax.set_xlabel('X1')
    ax.set_ylabel('X2')
    ax.set_zlabel('Z')
    plt.show()
    return

# print('archivo de entrada:', sys.argv[1])
# valores, expected = parserFile(sys.argv[1], 100)
# plotX1X2Z(valores, expected)