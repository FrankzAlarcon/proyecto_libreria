from queue import PriorityQueue #importar cola de prioridad

class Grafo:
  def __init__(self, num_nodos):
      self.numNodos = num_nodos #numero de nodos
      self.aristas = [[-1 for i in range(num_nodos)] for j in range(num_nodos)]#aristas y pesos
      self.visitado = [] #lista de vertices visitados

  def agregarArista(self, origen, destino, peso):
      self.aristas[origen][destino] = peso
      self.aristas[destino][origen] = peso

  def dijkstra(self, nodoInicial):
      D={nodo:float('inf') for nodo in range(self.numNodos)}
      D[nodoInicial] = 0
      #cola de prioridad
      colaPrioridad = PriorityQueue()
      colaPrioridad.put((0, nodoInicial))
      #recorrer
      while not colaPrioridad.empty():
        (dist, nodoActual) = colaPrioridad.get()
        self.visitado.append(nodoActual)
        #Visitar los nodos adyacentes
        for vecino in range(self.numNodos):
          if self.aristas[nodoActual][vecino] != -1:
            distancia = self.aristas[nodoActual][vecino]
            if vecino not in self.visitado:
              constoAnterior = D[vecino]
              costoNuevo = D[nodoActual] + distancia
              if costoNuevo < constoAnterior:
                colaPrioridad.put((costoNuevo,vecino))
                D[vecino] = costoNuevo
      return D

