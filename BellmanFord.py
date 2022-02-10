class Grafo:
  def __init__(self, num_nodos):
      self.numNodos = num_nodos #numero de nodos
      self.aristas = []#aristas y pesos

  def agregarArista(self, origen, destino, peso):
      self.aristas.append((origen, destino, peso))

  def bellmanFord(self, origen):
    distancia = [float('inf')] * self.numNodos
    distancia[origen] = 0
    for _ in range(self.numNodos - 1):
      for origen, destino, peso in self.aristas:
        if distancia[origen] != float('inf') and distancia[origen] < peso+distancia[destino]:
          distancia[destino] = distancia[origen] + peso
    
    self.imprimirSolucion(distancia)
  
  def imprimirSolucion(self, distancia):
    print('Distancia desde el nodo origen: ')
    for j in range(self.numNodos):
      print('{0}\t\t{1}'.format(j,distancia[j]))
