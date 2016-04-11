# SIA-1C2016

SISTEMAS DE INTELIGENCIA ARTIFICIAL
PRIMER CUATRIMESTRE 2016

TRABAJO PRACTICO 1
METODOS DE BUSQUEDA NO INFORMADOS E INFORMADOS

**********************************
INTEGRANTES
**********************************
Maximiliano J. Valverde (51158)
Ma. Florencia Besteiro (51117)
Matias L. Rivas (51274)

*********************************
INSTRUCCIONES DE EJECUCION
*********************************

java -jar 0hh1game.jar HEURISTIC STRATEGY [[SIZE]] BOARD

*********************************
PARAMETROS
*********************************

HEURISTIC: SwapsPerRow OR ColumnColorFix

STRATEGY: bfs OR dfs OR iterative OR greedy OR astar

SIZE: 4 OR 6

BOARD: 1 OR 2

*********************************
EJEMPLOS DE EJECUCION
*********************************

java -jar 0hh1game.jar SwapsPerRow ASTAR 6 1

java -jar 0hh1game.jar ColumnColorFix ASTAR 6 1

java -jar 0hh1game.jar ColumnColorFix DFS 4 2

java -jar 0hh1game.jar SwapsPerRow BFS 4 1



