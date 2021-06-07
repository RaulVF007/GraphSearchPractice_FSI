# Search methods

import search

ab = search.GPSProblem('A', 'B'
                       , search.romania)
#Nuevo práctica 2:Nuevos caminos para comparar métodos ramificación y acotación con ramificación y acotación con
#subestimación:
bc = search.GPSProblem('B', 'C'
                       , search.romania)
ad = search.GPSProblem('A', 'D'
                       , search.romania)
br = search.GPSProblem('B', 'R'
                       , search.romania)
ad = search.GPSProblem('A', 'D'
                       , search.romania)
cs = search.GPSProblem('C', 'S'
                       , search.romania)

cf = search.GPSProblem('C', 'F'
                       , search.romania)

#print(search.breadth_first_graph_search(ab).path())
#print(search.depth_first_graph_search(ab).path())

print("Camino de A a B:")
print("Búsqueda por ramificación y acotación:", search.branch_and_bround_graph_search(ab)[0].path())
print("-> Coste del camino:", search.branch_and_bround_graph_search(ab)[0].path_cost)
print("-> Nodos visitados:", search.branch_and_bround_graph_search(ab)[1])
print("Búsqueda por ramificación y acotación con subestimación:", search.branch_and_bround_with_underestimation_graph_search(ab)[0].path())
print("-> Coste del camino:", search.branch_and_bround_with_underestimation_graph_search(ab)[0].path_cost)
print("-> Nodos visitados:", search.branch_and_bround_with_underestimation_graph_search(ab)[1])

print("\nCamino de B a C:")
print("Búsqueda por ramificación y acotación:", search.branch_and_bround_graph_search(bc)[0].path())
print("-> Coste del camino:", search.branch_and_bround_graph_search(bc)[0].path_cost)
print("-> Nodos visitados:", search.branch_and_bround_graph_search(bc)[1])
print("Búsqueda por ramificación y acotación con subestimación:", search.branch_and_bround_with_underestimation_graph_search(bc)[0].path())
print("-> Coste del camino:", search.branch_and_bround_with_underestimation_graph_search(bc)[0].path_cost)
print("-> Nodos visitados:", search.branch_and_bround_with_underestimation_graph_search(bc)[1])

print("\nCamino de A a D:")
print("Búsqueda por ramificación y acotación:", search.branch_and_bround_graph_search(ad)[0].path())
print("-> Coste del camino:", search.branch_and_bround_graph_search(ad)[0].path_cost)
print("-> Nodos visitados:", search.branch_and_bround_graph_search(ad)[1])
print("Búsqueda por ramificación y acotación con subestimación:", search.branch_and_bround_with_underestimation_graph_search(ad)[0].path())
print("-> Coste del camino:", search.branch_and_bround_with_underestimation_graph_search(ad)[0].path_cost)
print("-> Nodos visitados:", search.branch_and_bround_with_underestimation_graph_search(ad)[1])

print("\nCamino de B a R:")
print("Busqueda por ramificacion y acotacion:", search.branch_and_bround_graph_search(br)[0].path())
print("-> Coste del camino:", search.branch_and_bround_graph_search(br)[0].path_cost)
print("-> Nodos visitados:", search.branch_and_bround_graph_search(br)[1])
print("Búsqueda por ramificación y acotación con subestimación:", search.branch_and_bround_with_underestimation_graph_search(br)[0].path())
print("-> Coste del camino:", search.branch_and_bround_with_underestimation_graph_search(br)[0].path_cost)
print("-> Nodos visitados:", search.branch_and_bround_with_underestimation_graph_search(br)[1])

print("\nCamino de C a F:")
print("Busqueda por ramificacion y acotacion:", search.branch_and_bround_graph_search(cf)[0].path())
print("-> Coste del camino:", search.branch_and_bround_graph_search(cf)[0].path_cost)
print("-> Nodos visitados:", search.branch_and_bround_graph_search(cf)[1])
print("Búsqueda por ramificación y acotación con subestimación:", search.branch_and_bround_with_underestimation_graph_search(cf)[0].path())
print("-> Coste del camino:", search.branch_and_bround_with_underestimation_graph_search(cf)[0].path_cost)
print("-> Nodos visitados:", search.branch_and_bround_with_underestimation_graph_search(cf)[1])

print("\nCamino de C a S:")
print("Busqueda por ramificacion y acotacion:", search.branch_and_bround_graph_search(cs)[0].path())
print("-> Coste del camino:", search.branch_and_bround_graph_search(cs)[0].path_cost)
print("-> Nodos visitados:", search.branch_and_bround_graph_search(cs)[1])
print("Búsqueda por ramificación y acotación con subestimación:", search.branch_and_bround_with_underestimation_graph_search(cs)[0].path())
print("-> Coste del camino:", search.branch_and_bround_with_underestimation_graph_search(cs)[0].path_cost)
print("-> Nodos visitados:", search.branch_and_bround_with_underestimation_graph_search(cs)[1])

#Conclusión en base a los resultados obtenidos:
#En base a los resultados obtenidos impresos, apreciamos que siempre existen dos posibilidades diferentes entre estos
#dos algoritmos:
#El primero es que el camino resultante con ambos algoritmos coincida, y por tanto, el coste del camino. Esto se puede
#apreciar en los ejemplos de los caminos de A a B, B a C y B a R.
#Por otro lado, la otra posibilidad esque el algoritmo de búsqueda por ramificación y acotación con subestimación de un
#resultado más eficiente que con el algoritmo de búsqueda por ramificación y acotación, dando un coste del camino
#más bajo. Esto es gracias a la implementación del algoritmo usando una heurística admisible (subestimación de lo que
# sería la solución real). Estos ejemplos corresponden a los caminos de: A a D, C a F y C a S.

#Finalmente, podemos concluir que el algoritmo de búsqueda por ramificación y acotación con subestimación resulta más
#ventajoso que el algoritmo de búsqueda por ramificación y acotación debido a que en ciertas situaciones, para el mismo
#camino, se usan menos nodos que en el otro algoritmo.
