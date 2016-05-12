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
	# print('valor 1ro: ', args.inputFile)
	# print('valor 2do: ',args[0])
	input_values,output_expected = parser.parserFile(args.inputFile, args.values)
	# print('salida: ', output_expected)
	print('size_input: ', len(input_values), ' output: ', len(output_expected))
	nn.multilayer_perceptron([2,5,1],input_values,output_expected,-1, 0.5,0.3,0.001,'linear',0)


if __name__ == "__main__": main()
