# Algoritmos Genéticos

Sistemas de Inteligencia Artificial <br />
Trabajo Practico 3


## Integrantes

Ma. Florencia Besteiro <br />
Maximiliano J. Valverde <br />
Leandro Matias Rivas

### Ejecución

Por consola, ubicarse dentro en TP3/src/ y ejecutar el siguiente comando <br />

```
python3 genetic_algorithm.py
```

Una vez terminada la corrida, se mostrará los gráficos de mejor fitness por generación y promedio de fitness por generación.

### Configuración

Dentro de la carpeta TP£/src/ se encuentra el archivo de configuración config.txt. En el mismo se poede variar todos los parametros de selecion, mutation, cruza y metodo de reemplazo. <br />
El archivo en cuestion es el siguiente:

```
** PARAMETROS DE CONFIGURACION **
# N: Cantidad de individuos de la población
# T: Temperatura (Bolztmann)
# m : Parámetro para métodos de Selección (Torneo Determinístico).usalmente toma el valor 2 o 3
# L : Longitud del cromosoma (En nuestro caso es 6. Indices de 0 a 5)
# pm : probabilidad de mutación
# pc : probabilidad de cruza
# T : Temperatura
# P : Presion
# m : Individuos en torneo
# SP : Presion selectiva
#
# En general :
#	N : [20 , 200]
#	pm : [0.001, 0.01]
#	pc: [0.6, 0.95]
# 	G : [0.6, 1]
#   SP : [1.0, 2.0]
#
# Selection methods: elite, universal, roulette, ranking, boltzmann, deterministic_tournament, probabilistic_tournament
# Cross methods: cross_1P, cross_2P, cross_annular, cross_uniform
# Mutation methods: classic, not_uniform
# Replacement methods: replacement_one, replacement_two, replacement_three, replacement_gengap, replacement_mixed
# Replacement selection methods : elite, universal, roulette, ranking, boltzmann, deterministic_tournament, probabilistic_tournament
# If replacement method is "replacement_mixed", then values are two selection methods
#
# Methods
selection universal boltzmann
cross cross_1P
mutation not_uniform
replacement replacement_three
rep_selection probabilistic_tournament roulette
#
# Parameters
N 50
pm 0.005
pc 0.6
G 0.3
T 150
SP 0
m 2
a 1.5
A 0.5
B 0.5
#
# Multipliers
sm 1.3
dm 0.6
em 0.6
rm 1.2
hm 1.1
# Stop criterias: generations, structure, optimum, content
#Stop
structure 0.9
```
