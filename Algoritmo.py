import time
import matplotlib.pyplot as plt

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
        elif self.algoritmo == 'quick_sort':
            return self._ordenar_quick_sort(lista)
        elif self.algoritmo == 'merge_sort':
            return self._ordenar_merge_sort(lista)
        elif self.algoritmo == 'shell_sort':
            return self._ordenar_shell_sort(lista)
        elif self.algoritmo == 'radix_sort':
            return self._ordenar_radix_sort(lista)
        elif self.algoritmo == 'heap_sort':
            return self._ordenar_heap_sort(lista)
        else:
            raise ValueError(f"Algoritmo '{self.algoritmo}' no soportado")

    def _plot_data(self, lista):
        plt.clf()
        plt.bar(range(len(lista)), lista)
        plt.pause(0.01)

    def _ordenar_burbuja(self, lista):
        n = len(lista)
        for i in range(n):
            for j in range(0, n-i-1):
                if lista[j] > lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]
                self._plot_data(lista)
        print(f"{self.algoritmo} ha terminado.")
        return lista

    def _ordenar_seleccion(self, lista):
        n = len(lista)
        for i in range(n):
            min_idx = i
            for j in range(i+1, n):
                if lista[j] < lista[min_idx]:
                    min_idx = j
            lista[i], lista[min_idx] = lista[min_idx], lista[i]
            self._plot_data(lista)
        print(f"{self.algoritmo} ha terminado.")
        return lista

    def _ordenar_insercion(self, lista):
        for i in range(1, len(lista)):
            key = lista[i]
            j = i-1
            while j >= 0 and key < lista[j]:
                lista[j + 1] = lista[j]
                j -= 1
                self._plot_data(lista)
            lista[j + 1] = key
            self._plot_data(lista)
        print(f"{self.algoritmo} ha terminado.")
        return lista

    def _ordenar_quick_sort(self, lista):
        if len(lista) <= 1:
            return lista
        else:
            pivot = lista[len(lista) // 2]
            left = [x for x in lista if x < pivot]
            middle = [x for x in lista if x == pivot]
            right = [x for x in lista if x > pivot]
            result = self._ordenar_quick_sort(left) + middle + self._ordenar_quick_sort(right)
            self._plot_data(result)
            print(f"{self.algoritmo} ha terminado.")
            return result

    def _ordenar_merge_sort(self, lista):
        if len(lista) <= 1:
            return lista
        mid = len(lista) // 2
        left = self._ordenar_merge_sort(lista[:mid])
        right = self._ordenar_merge_sort(lista[mid:])
        result = self._merge(left, right)
        print(f"{self.algoritmo} ha terminado.")
        return result

    def _merge(self, left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
            self._plot_data(result)
        result.extend(left[i:])
        result.extend(right[j:])
        self._plot_data(result)
        return result

    def _ordenar_shell_sort(self, lista):
        n = len(lista)
        gap = n // 2
        while gap > 0:
            for i in range(gap, n):
                temp = lista[i]
                j = i
                while j >= gap and lista[j - gap] > temp:
                    lista[j] = lista[j - gap]
                    j -= gap
                    self._plot_data(lista)
                lista[j] = temp
                self._plot_data(lista)
            gap //= 2
        print(f"{self.algoritmo} ha terminado.")
        return lista

    def _ordenar_radix_sort(self, lista):
        RADIX = 10
        maxLength = False
        tmp, placement = -1, 1
        while not maxLength:
            maxLength = True
            buckets = [[] for _ in range(RADIX)]
            for i in lista:
                tmp = i // placement
                buckets[tmp % RADIX].append(i)
                if maxLength and tmp > 0:
                    maxLength = False
            a = 0
            for b in range(RADIX):
                buck = buckets[b]
                for i in buck:
                    lista[a] = i
                    a += 1
                    self._plot_data(lista)
            placement *= RADIX
        print(f"{self.algoritmo} ha terminado.")
        return lista

    def _ordenar_heap_sort(self, lista):
        def heapify(arr, n, i):
            largest = i
            l = 2 * i + 1
            r = 2 * i + 2
            if l < n and arr[i] < arr[l]:
                largest = l
            if r < n and arr[largest] < arr[r]:
                largest = r
            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                heapify(arr, n, largest)
        
        n = len(lista)
        for i in range(n // 2 - 1, -1, -1):
            heapify(lista, n, i)
        
        for i in range(n-1, 0, -1):
            lista[i], lista[0] = lista[0], lista[i]
            heapify(lista, i, 0)
            self._plot_data(lista)
        
        print(f"{self.algoritmo} ha terminado.")
        return lista
