#!/bin/bash
# -*- coding: utf-8 -*- 
# This script will be executed *after* all the other init scripts.
# You can put your own initialization stuff in here if you don't
# want to do the full Sys V style init stuff.

# Ejecutar el script de demo en cada arranque:
python neuronal_network.py -hl1 10 -hl2 4 -G exp -ecm 0.0001 -eta 0.5 -alpha 0.9 -a 0.0001 -b 0.0001 -k 25