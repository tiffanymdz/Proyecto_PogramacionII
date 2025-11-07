from CargaDatos import CargadorDatos
from Procesador_EDA import ProcesadorEDA

# 1️⃣ Cargar dataset
cargador = CargadorDatos(r"C:\Users\tiffa\OneDrive\Desktop\Big Data\Programación II\premier.csv")
df = cargador.cargar()

print("✅ Archivo cargado correctamente")
print(f"➡️ Filas totales: {cargador.num_filas}")
print(f"➡️ Porcentaje de nulos: {cargador.porcentaje_nulos:.2f}%")
print("-" * 60)

# 2️⃣ Procesar con ProcesadorEDA
procesador = ProcesadorEDA(df)

df_limpio = procesador.limpieza_datos()
print("✅ Datos limpiados (imputación aplicada)\n")

print("📊 Resumen descriptivo de variables numéricas:")
print(procesador.resumen_descriptivo())
print("-" * 60)

print("🔗 Correlaciones relevantes:")
print(procesador.correlaciones_especificas())
print("-" * 60)

df_limpio.to_csv(r"C:\Users\tiffa\OneDrive\Desktop\Big Data\Programación II\premier_limpio.csv", index=False)
print("✅ Dataset limpio guardado como 'premier_limpio.csv'")
