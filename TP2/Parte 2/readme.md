# SIA-1C2016

SISTEMAS DE INTELIGENCIA ARTIFICIAL
PRIMER CUATRIMESTRE 2016

TRABAJO PRACTICO 2
REDES NEURONALES

**********************************
INTEGRANTES
**********************************
Maximiliano J. Valverde (51158)
Ma. Florencia Besteiro (51117)
Matias L. Rivas (51274)

*********************************
INSTRUCCIONES DE EJECUCION
*********************************

neuronal_network.py -hl1 HL1 -hl2 HL2 -G FUNC -ecm ECM -eta ETA -alpha ALPHA -a A -b B -k K

*********************************
PARAMETROS
*********************************

HL1: Hidden Layer 1

HL2: Hidden Layer 2

G: Funcion

ECM: Error cuadratico medio de corte

ETA: Factor de aprendizaje

Alpha:

A:

B:

K:

*********************************
EJEMPLOS DE EJECUCION
*********************************

neuronal_network.py -hl1 10 -hl2 4 -G exp -ecm 0.0005 -eta 0.0005 -alpha 0.9 -a 0.0001 -b 0.0001 -k 25
