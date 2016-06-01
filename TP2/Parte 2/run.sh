#!/bin/bash
# -*- coding: utf-8 -*- 
# This script will be executed *after* all the other init scripts.
# You can put your own initialization stuff in here if you don't
# want to do the full Sys V style init stuff.

# Ejecutar el script de demo en cada arranque:
#python neuronal_network.py -hl1 15 -hl2 5 -G exp -ecm 0.001 -eta 0.5 -alpha 0.9 -a 0 -b 0 -k 0
#python3 neuronal_network.py -hl1 10 -hl2 4 -G tan -ecm 0.0005 -eta 0.5 -alpha 0.9 -a 0.1 -b 0.02 -k 3
##python3 neuronal_network.py -hl1 10 -hl2 4 -G tan -ecm 0.0005 -eta 0.5 -alpha 0.9 -a 0 -b 0 -k 0
python3 neuronal_network.py -hl1 10 -hl2 4 -G tan -ecm 0.0005 -eta 0.03 -alpha 0.9 -a 0.01 -b 0.005 -k 3
#python3 neuronal_network.py -hl1 10 -hl2 4 -G tan -ecm 0.0005 -eta 0.3 -alpha 0.9 -a 0 -b 0. -k 0

#python3 neuronal_network.py -hl1 10 -hl2 4 -G tan -ecm 0.0001 -eta 0.5 -alpha 0.9 -a 0.05 -b 0.001 -k 3

