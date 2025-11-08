import  pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px



class Visualizador:
    def __init__(self, datos):
        self.__datos = datos


    @property
    def datos(self):
        return self.__datos

    @datos.setter
    def datos(self, nuevos_datos):
        self.__datos = nuevos_datos


    def histograma(self, columna):
        plt.hist(self.__datos[columna].dropna(), bins=15, color='skyblue', edgecolor='black')
        plt.title(f"Histograma de {columna}")
        plt.xlabel(columna)
        plt.ylabel("Frecuencia")
        plt.show()

        media = self.__datos[columna].mean()
        mediana = self.__datos[columna].median()
        print(f"Mini-historia: La media de {columna} es {media:.2f} y la mediana {mediana:.2f}. "
              f"Esto muestra cómo se distribuyen los valores de {columna}.")

    # --- Scatter (dispersión) ---
    def scatter(self, x, y):
        plt.scatter(self.__datos[x], self.__datos[y], color='orange', alpha=0.7)
        plt.title(f"Relación entre {x} y {y}")
        plt.xlabel(x)
        plt.ylabel(y)
        plt.show()

        if self.__datos[x].dtype != 'O' and self.__datos[y].dtype != 'O':
            corr = self.__datos[[x, y]].corr().iloc[0, 1]
            print(f"Mini-historia: La correlación entre {x} y {y} es {corr:.3f}. "
                  f"Indica {'una relación fuerte' if abs(corr) > 0.7 else 'una relación débil o moderada'}.")
        else:
            print("Mini-historia: Uno de los ejes no es numérico, no se puede calcular la correlación.")


    def heatmap(self):
        num = self.__datos.select_dtypes(include=['int64', 'float64'])
        corr = num.corr()

        plt.imshow(corr, cmap='coolwarm', interpolation='nearest')
        plt.colorbar()
        plt.xticks(range(len(corr.columns)), corr.columns, rotation=45, ha='right')
        plt.yticks(range(len(corr.columns)), corr.columns)
        plt.title("Mapa de calor de correlaciones")
        plt.show()

        top = corr.unstack().sort_values(ascending=False).drop_duplicates()
        top = top[(top < 1) & (top > 0.5)].head(3)
        print("Mini-historia: Las correlaciones más altas entre variables numéricas son:")
        for (a, b), v in top.items():
            print(f"   {a} y {b}: {v:.3f}")



# Cargar el dataset
ruta = "premier_limpio.csv"
df = pd.read_csv(ruta)

# Crear el objeto visualizador
viz = Visualizador(df)

#Visualización 1: Histograma de goles ---
viz.histograma("Goals")

#  Dispersión entre Goles esperados (xG) y Goles reales ---
viz.scatter("Expected Goals (xG)", "Goals")

#  Mapa de calor de correlaciones ---
viz.heatmap()
