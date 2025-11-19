import pandas as pd

class ProcesadorEDA:

    def __init__(self, df):
        self._df = df

    @property
    def dataframe(self):
        return self._df

    @dataframe.setter
    def dataframe(self, nuevo_df):
        self._df = nuevo_df

    def limpieza_datos(self):

        df = self.dataframe.copy()
        columnas_numericas = df.select_dtypes(include=["int64", "float64"]).columns
        df[columnas_numericas] = df[columnas_numericas].fillna(df[columnas_numericas].median())
        self.dataframe = df
        return df

    def resumen_descriptivo(self):

        columnas_numericas = self.dataframe.select_dtypes(include=["int64", "float64"])
        resumen = columnas_numericas.describe().T
        resumen["median"] = columnas_numericas.median()
        resumen["q1"] = columnas_numericas.quantile(0.25)
        resumen["q3"] = columnas_numericas.quantile(0.75)
        return resumen[["count", "mean", "std", "min", "q1", "median", "q3", "max"]]

    def correlaciones_especificas(self):

        correlaciones = {
            "Goals_vs_xG": self.dataframe["Goals"].corr(self.dataframe["Expected Goals (xG)"]),
            "Assists_vs_ProgressivePasses": self.dataframe["Assists"].corr(self.dataframe["Progressive Passes"]),
            "DribblesSuccess_vs_ProgressiveCarries": self.dataframe["Successful Dribbles"].corr(self.dataframe["Progressive Carries"])
        }

        return pd.Series(correlaciones, name="Correlaciones relevantes")

    def detectar_outliers(self, columna):

        q1 = self.dataframe[columna].quantile(0.25)
        q3 = self.dataframe[columna].quantile(0.75)
        iqr = q3 - q1

        limite_inferior = q1 - 1.5 * iqr
        limite_superior = q3 + 1.5 * iqr

        outliers = self.dataframe[
            (self.dataframe[columna] < limite_inferior) |
            (self.dataframe[columna] > limite_superior)
        ]
        return outliers
