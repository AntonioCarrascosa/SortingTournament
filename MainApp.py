import random
from Algoritmo import Algoritmo
import matplotlib.pyplot as plt

class MainApp:
    def __init__(self):
        self.algoritmos = [
            Algoritmo("burbuja"), 
            Algoritmo("seleccion"), 
            Algoritmo("insercion"), 
            Algoritmo("quick_sort"), 
            Algoritmo("merge_sort"), 
            Algoritmo("shell_sort"), 
            Algoritmo("radix_sort"), 
            Algoritmo("heap_sort")
        ]
        self.data = [random.randint(1, 100) for _ in range(10)]  # Lista de ejemplo

    def run(self):
        plt.ion()  # Activar modo interactivo en matplotlib
        for algoritmo in self.algoritmos:
            print(f"Ejecutando {algoritmo.algoritmo}...")
            algoritmo.ejecutar(self.data.copy())
            plt.show()
            plt.pause(0.5)  # Pausa para observar el resultado final de cada algoritmo

if __name__ == "__main__":
    app = MainApp()
    app.run()
