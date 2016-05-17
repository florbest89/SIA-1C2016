# Este metodo toma un archivo de entrada y corre el perpectron multicapa
import argparse
import neuronal_network as nn
from parseFile import parser
import matplotlib

# -I /Users/user/Documents/terrain/terrain4.txt -v -1

def parse_arguments():
	parser = argparse.ArgumentParser()
	parser.add_argument("-I", "--inputFile", type=str, help="FileInput", required=True)
	parser.add_argument("-v", "--values", type=int, help="number of values", required=True)
	return parser.parse_args()

def main():
    args = parse_arguments()

    # input_values, output_expected = parser.parserFile(args.inputFile, args.values)
    input_values,output_expected = parser.parserFile(args.inputFile, args.values)
    # err, w = nn.multilayer_perceptron([2,10,10,1], input_values, output_expected, 1, 0.5, 0.9, 0.000001,'tan',0,0.9,0,0,0)
    err, w, out = nn.multilayer_perceptron([2,5,5,1], input_values, output_expected, 1, 0.5, 0.6, 0.0001,'exp',0,0.9,0,0,0)
    # ESTA CONFIGURACION DE LA RED ME DIO UN RESULTADO MUY BUENO, con una entrada de 150
    # err,w = nn.multilayer_perceptron([2,10,10,10,1],input_values,output_expected,1, 0.5,0.6,0.0001,'tan',0,0.9,input_test,output_test)
    parser.plotX1X2Z(input_values, out)
if __name__ == "__main__": main()
