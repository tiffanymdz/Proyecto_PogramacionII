# Premier_League_Insights

Premier League Insights ⚽
 Proyecto universitario de análisis de datos de la Premier League 2024/2025 utilizando Programación Orientada a Objetos en Python.

 ⚽ Información del dataset
 
 nombre: Premier League - Player Stats Season - 24/25
 
 link: https://www.kaggle.com/datasets/eduardopalmieri/premier-league-player-stats-season-2425/data
 
 filas: 4271
 
 columnas: 33

📋Descripción
 
 Sistema desarrollado en Python con POO que ingiere datos de partidos desde archivos CSV, permite realizar
 análisis exploratorio de datos (EDA) y visualización de gráficos de manera estática e interactiva mediante un
 dashboard.

🎯Objetivos del Proyecto
 
 Ingesta: Cargar archivos CSV con partidos de la Premier League 2024/2025
 
 EDA: Proveer métodos orientados a objetos y notebooks con análisis descriptivo
 
 Visualización: Crear gráficas que cuenten una historia y un dashboard interactivo con Streamlit

🏗 Arquitectura del Proyecto
 El proyecto está estructurado con Programación Orientada a Objetos, separando responsabilidades en diferentes clases y módulos:
 
 Clases Principales
 
 CargadorDatos : Gestiona la carga del dataset premier.csv y registra métricas de calidad
 
 ProcesadorEDA : Realiza limpieza, análisis estadístico y detección de outliers
 
 Visualizador : Genera visualizaciones estáticas con narrativas analíticas
 
 Jugador : Modelo de datos para representar jugadores individuales
 
 Equipo : Modelo de datos para gestionar equipos y sus jugadores

 🛠 Tecnologías Utilizadas
 
 Python 3.x: Lenguaje principal
 
 Pandas: Manipulación y análisis de datos
 
 NumPy: Cálculos numéricos
 
 Matplotlib: Visualización estática
 
 Seaborn: Visualizaciones estadísticas avanzadas
 
 Plotly: Gráficos interactivos
 
 Streamlit: Dashboard interactivo
 
 Jupyter Notebook: Desarrollo y presentación

 ⚙ Funcionalidades Implementadas
 
 1. Carga de Datos (CargadorDatos )
  
 - Carga del dataset premier.csv
 
 - Corrección automática de formato en columnas (ej: Pass Completion%)
 
 - Registro automático del número de filas número de filas
 
 - Cálculo del porcentaje de valores nulos
 
 Atributos principales:
 
 ruta_archivo : Ruta del archivo CSV
 
 dataframe : DataFrame de Pandas con los datos
 
 num_filas : Total de filas cargadas
 
 porcentaje_nulos : Porcentaje de valores nulos
 
 2. Procesamiento EDA (ProcesadorEDA )
 
 Métodos implementados:
 
 limpieza_datos()
 
 Imputación de valores nulos con la mediana para columnas numéricas
 
 Preservación de tipos de datos correctos
 
 Retorna el dataframe limpio
 
 resumen_descriptivo()
 
 Estadísticas completas: count, mean, std, min, Q1, median, Q3, max
 
 Aplicado a todas las variables numéricas
 
 Formato tabular para fácil interpretación
 
 correlaciones_especificas()
 
 Calcula correlaciones clave:
 
 Goals vs Expected Goals (xG): Mide precisión predictiva
 
 Assists vs Progressive Passes: Relación entre pases progresivos y asistencias
 
 Successful Dribbles vs Progressive Carries: Efectividad en avance con balón
 
 detectar_outliers(columna)
 
 Detección basada en el método IQR (Rango Intercuartílico)
 
 Identifica valores atípicos por encima/debajo de 1.5 * IQR
 
 Retorna DataFrame con los outliers detectados
 
 3. Visualización (Visualizador )
 
 Cada visualización incluye datos estadísticos y una mini-historia que explica el insight:
 
 scatter()
 
 Tipo: Gráfico de dispersión
 
 Variables: Expected Goals (xG) vs Goals
 
 Historia: Identifica jugadores/equipos sobre-performing o bajo-performing
 
 Estadísticas mostradas: Correlación, máximo, mínimo y media de xG
 
 histograma()
 
 Tipo: Histograma con curva KDE
 
 Variable: Goals
 
 Historia: Muestra que la mayoría de observaciones tienen 0 goles (eventos poco frecuentes)
 
 Estadísticas mostradas: Máximo, mediana, mínimo
 
 correlaciones()
 
 Tipo: Gráfico de barras horizontal
 
 Variables: Tres pares de correlaciones clave
 
 Historia: xG es el mejor predictor de Goals, mientras que Assists aporta poco
 
 heatmap()
 
 Tipo: Mapa de calor
 
 Variables: Matriz de correlaciones entre métricas ofensivas
 
 Historia: Dribbles y Carries moderadamente relacionados; Assists-ProgPasses sorprendentemente débil
 
 4. Modelado POO del Dominio
 
 Clase Jugador
 
 Atributos:
 
 name: Nombre del jugador
 
 team: Equipo al que pertenece
 
 position: Posición en el campo
 
 minutes: Minutos jugados
 
 goals: Goles anotados
 
 assists: Asistencias realizadas
 
Clase Equipo

Atributos:

name: Nombre del equipo 

liga: Liga del equipo ("Premier League")

jugadores: Lista de objetos Jugador

Métodos: 

agregar_jugador(jugador): Añade un jugador al equipo

total_goles(): Calcula suma de goles del equipo

total_assits(): Calcula suma de asistencias del equipo

📊 Análisis Realizados
 
 Análisis Exploratorio (EDA)
 
✅ Imputación de valores nulos con mediana
 
✅ Estadísticas descriptivas completas (8 métricas)

✅ Correlaciones entre variables ofensivas clave

✅ Detección de outliers con método IQR

✅ Generación de dataset limpio (premier_clean.csv)
 
Visualizaciones con Historia
 
 Cada gráfico cuenta una historia específica:
 
 1. Scatter xG vs Goals: Identifica sobre/bajo-rendimiento respecto a expectativas
 
 2. Histograma de Goals: Muestra distribución sesgada (mayoría con 0 goles)
 
 3. Correlaciones: xG es el mejor predictor de rendimiento ofensivo
 
 4. Heatmap: Revela relaciones sorprendentes (ej: Assists-ProgPasses débil)
 
 📈 Resultados y Hallazgos Clave
 
 Correlaciones principales:
 
 Goals vs xG: 0.61 (moderada-alta) → xG es buen predictor
 
 Assists vs Progressive Passes: 0.13 (débil) → Relación sorprendentemente baja
 
 Dribbles vs Carries: 0.46 (moderada) → Habilidades relacionadas
 
 Insights del Histograma:
 
 Media de Goals: 0.09 → Eventos de gol poco frecuentes
 
 Mayoría de observaciones en 0 goles
 
 Distribución altamente sesgada

👥 Autores
 
 María Paubla Delgado Loaiza y Tiffany Méndez Quirós
 
 Colegio Universitario de Cartago
 
 BD-143 Programación II
 
 III Cuatrimestre 2025
 
 Profesor: Osvaldo González Chaves

🔧Notas Técnicas
 
 El dataset se carga desde la ruta especificada en 
 
 CargadorDatos
 
 La limpieza genera automáticamente premier_limpio.csv
 
 Todas las visualizaciones incluyen estadísticas y narrativas
 
 El código está completamente orientado a objetos

📄LicenciaProyecto desarrollado con fines académicos para el curso BD-143 Programación II.
