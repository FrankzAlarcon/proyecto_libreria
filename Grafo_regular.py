# Programa escrito en Python que genera un grafo d-regular random de n vértices con el paquete NetworkX y
# luego lo muestra por pantalla con el paquete Matplotlib.


import networkx as nx  # Importación del paquete NetworkX
#pip install matplotlib en el cmd con Permiso de Administrador
#pip install scipy
import matplotlib.pyplot as plt  # Importación paquete Matplotlib con el módulo pyplot

# G = nx.random_regular_graph(4,5)  # Función generadora de un grafo d-regular random de n vértices
# nx.draw_kamada_kawai(G, node_size=4, width=2, with_labels=True)  # Dibujar el grafo G con una interfaz particular
# plt.axis("equal")  # Redimensionar los ejes a longitudes iguales
# plt.show()  # Mostrar el grado d-regular por pantalla

G = nx.Graph() #Crear un grafo
#Anadir nordos
G.add_node('Quito')
G.add_node('Guayaquil')
G.add_nodes_from(['Cuenca','Manabí','Joya de los Sachas'])
#andir Aristas
G.add_edge('Quito','Guayaquil', weight= 500)
G.add_edge('Quito', 'Joya de los Sachas', weight=200)
G.add_edges_from([('Cuenca','Manabí'), ('Quito','Manabí')],weight = 300)
print(len(G.nodes))
print(len(G.edges))
print(G.nodes)
print(G.edges)
nx.draw_kamada_kawai(G, node_size=4, width=2, with_labels=True)
plt.axis("equal")  
plt.show()  
