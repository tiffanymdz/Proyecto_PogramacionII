from CargaDatos import CargadorDatos
from Procesador_EDA import ProcesadorEDA
from Modelado_POO import Jugador, Equipo

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

 Visualizaciones
print(" Detectando outliers en Goals:")
outliers_goals = procesador.detectar_outliers("Goals")
print(f"Se encontraron {len(outliers_goals)} outliers en Goals")
print(outliers_goals[["Player", "Team", "Goals"]].head())
print("-" * 60)

main
df_limpio.to_csv(r"C:\Users\tiffa\OneDrive\Desktop\Big Data\Programación II\premier_limpio.csv", index=False)
print(" Dataset limpio guardado como 'premier_limpio.csv'")

# 3️⃣Modelado POO de los jugadores y equipos

jugadores = []
for _, row in df_limpio.iterrows():
    jugador = Jugador(
        name=row["Player"],
        team=row["Team"],
        position=row["Position"],
        minutes=row["Minutes"],
        goals=row["Goals"],
        assists=row["Assists"]
    )
    jugadores.append(jugador)

equipo_mu = Equipo("Manchester United")
for j in jugadores:
    if j.team == "Manchester United":
        equipo_mu.agregar_jugador(j)

print(" Total goles MU:", equipo_mu.total_goles())
print(" Total asistencias MU:", equipo_mu.total_assists())

equipo_ful = Equipo("Fulham")
for j in jugadores:
    if j.team == "Fulham":
        equipo_ful.agregar_jugador(j)

print(" Total goles FUL :", equipo_ful.total_goles())
print(" Total asistencias FUL:", equipo_ful.total_assists())

equipo_liv = Equipo("Liverpool")
for j in jugadores:
    if j.team == "Liverpool":
        equipo_liv.agregar_jugador(j)

print(" Total goles LIV:", equipo_liv.total_goles())
print(" Total asistencias LIV:", equipo_liv.total_assists())