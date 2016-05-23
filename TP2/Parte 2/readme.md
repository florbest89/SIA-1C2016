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

En terminal, posicionarse sobre la directorio /TP2/Parte2 y ejecutar el archivo run.sh para ejecutar la red neuronal.

   $ ./run.sh

A continuacion se muestra un ejemplo con datos de ejecucion que se encuantre dentro de dicho archivo.
Estos parametros pueden ser cambiados segun que se desee realizar.

python neuronal_network.py -hl1 10 -hl2 4 -G tan -ecm 0.001 -eta 0.0005 -alpha 0.9 -a 0 -b 0 -k 0

*********************************
PARAMETROS
*********************************

HL1: Hidden Layer 1

HL2: Hidden Layer 2

G: Funcion

ECM: Error cuadratico medio de corte

ETA: Factor de aprendizaje

Alpha: Constante para Momentum

A: Constante para incrementar ETA

B: Constante para reducir ETA

K: Cantidad de epocas en que el ECM se reduce

*********************************
EJEMPLOS DE EJECUCION
*********************************

neuronal_network.py -hl1 10 -hl2 4 -G exp -ecm 0.0005 -eta 0.0005 -alpha 0.9 -a 0.0001 -b 0.0001 -k 25
