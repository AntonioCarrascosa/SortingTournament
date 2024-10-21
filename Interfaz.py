import tkinter as tk
import random
from threading import Thread
from Algoritmo import Algoritmo

class Interfaz:
    def __init__(self, root):
        self.root = root
        self.root.title("Competencia de Algoritmos de Ordenamiento")

        self.canvas = tk.Canvas(root, width=800, height=400, bg="white")
        self.canvas.pack()

        self.data = [random.randint(1, 400) for _ in range(10)]  # Reducción a 10 elementos
        self.draw_data(self.data)

        self.button = tk.Button(root, text="Iniciar Competencia", command=self.iniciar_competencia)
        self.button.pack()

        self.algoritmos = [Algoritmo("bubble_sort"), Algoritmo("selection_sort"), Algoritmo("insertion_sort"), 
                           Algoritmo("quick_sort"), Algoritmo("merge_sort"), Algoritmo("shell_sort"), 
                           Algoritmo("radix_sort"), Algoritmo("heap_sort")]
        
        self.algoritmos = [Algoritmo("bubble_sort")]
        
    def draw_data(self, data):
        self.canvas.delete("all")
        bar_width = 800 / len(data)
        for i, height in enumerate(data):
            x0 = i * bar_width
            y0 = 400 - height
            x1 = (i + 1) * bar_width
            y1 = 400
            self.canvas.create_rectangle(x0, y0, x1, y1, fill="blue")
        self.canvas.update_idletasks()

    def iniciar_competencia(self):
        self.button.config(state=tk.DISABLED)  # Deshabilitar botón

        def run_algoritmo(algo):
            try:
                algo.ejecutar(self.data.copy(), self.draw_data, 0.001)
            except Exception as e:
                print(f"Error en {algo.algoritmo}: {e}")

        threads = []
        for algo in self.algoritmos:
            thread = Thread(target=run_algoritmo, args=(algo,))
            threads.append(thread)
            thread.start()
        for thread in threads:
            thread.join()

        self.button.config(state=tk.NORMAL)  # Habilitar botón de nuevo
