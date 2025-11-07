import pandas as pd

class CargadorDatos:
    def __init__(self, ruta_archivo):
        self.ruta_archivo = ruta_archivo
        self.dataframe = None
        self.num_filas = 0
        self.porcentaje_nulos = 0

    def cargar(self):
        self.dataframe = pd.read_csv(self.ruta_archivo)
        self.num_filas = len(self.dataframe)
        total_nulos = self.dataframe.isnull().sum().sum()
        total_celdas = self.dataframe.size
        self.porcentaje_nulos = (total_nulos / total_celdas) * 100

        print("✅ Archivo cargado.")
        print(f"➡️ Filas: {self.num_filas}")
        print(f"➡️ Total de valores nulos: {total_nulos}")
        print(f"➡️ Porcentaje de nulos: {self.porcentaje_nulos:.2f}%")