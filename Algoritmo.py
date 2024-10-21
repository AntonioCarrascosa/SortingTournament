class Algoritmo:
    def __init__(self, algoritmo):
        self.algoritmo = algoritmo

    def ejecutar(self, lista):
        if self.algoritmo == 'burbuja':
            return self._ordenar_burbuja(lista)
        elif self.algoritmo == 'seleccion':
            return self._ordenar_seleccion(lista)
        elif self.algoritmo == 'insercion':
            return self._ordenar_insercion(lista)
        else:
            raise ValueError(f"Algoritmo '{self.algoritmo}' no soportado")

    def _ordenar_burbuja(self, lista):
        n = len(lista)
        for i in range(n):
            for j in range(0, n-i-1):
                if lista[j] > lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]
        return lista

    def _ordenar_seleccion(self, lista):
        n = len(lista)
        for i in range(n):
            min_idx = i
            for j in range(i+1, n):
                if lista[j] < lista[min_idx]:
                    min_idx = j
            lista[i], lista[min_idx] = lista[min_idx], lista[i]
        return lista

    def _ordenar_insercion(self, lista):
        for i in range(1, len(lista)):
            key = lista[i]
            j = i-1
            while j >= 0 and key < lista[j]:
                lista[j + 1] = lista[j]
                j -= 1
            lista[j + 1] = key
        return lista
