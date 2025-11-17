

import streamlit as st
import pandas as pd
import plotly.express as px


# CONFIGURACIÓN 

st.set_page_config(
    page_title="Premier League Dashboard",
    layout="wide",
)

COLOR_SCATTER = px.colors.sequential.Viridis
COLOR_HIST = px.colors.sequential.Plasma
COLOR_BARS = px.colors.sequential.Blues

# CARGA DE DATOS

st.title("Visualizador de Datos de la Premier League")
st.write("Explora las relaciones entre variables futbolísticas usando visualizaciones interactivas.")

datos = pd.read_csv("premier_limpio.csv")


# SCATTER 

st.header("Scatter: Expected Goals vs Goals")

fig_scatter = px.scatter(
    datos,
    x="Expected Goals (xG)",
    y="Goals",
    title="Relación entre xG y Goals",
    opacity=0.8,
    color="Expected Goals (xG)",
    color_continuous_scale=COLOR_SCATTER,
)

fig_scatter.update_layout(
    template="plotly_white",
    title_font=dict(size=22),
    margin=dict(l=20, r=20, t=60, b=20)
)

st.plotly_chart(fig_scatter, use_container_width=True)

corr_xg_goals = datos["Expected Goals (xG)"].corr(datos["Goals"])
st.info(f"📈 **Correlación xG - Goals:** {corr_xg_goals:.3f}")



# HISTOGRAMA

st.header("Histograma de Goals")

# Asegurar que Goals es numérico
datos["Goals"] = pd.to_numeric(datos["Goals"], errors="coerce")

fig_hist = px.histogram(
    datos,
    x="Goals",
    nbins=20,
    title="Distribución de goles en la temporada",
    color_discrete_sequence=['#1f77b4']
)

st.plotly_chart(fig_hist, use_container_width=True)


# CORRELACIONES

st.header(" Correlaciones ")

corr_goals_xg = datos["Goals"].corr(datos["Expected Goals (xG)"])
corr_assists_passes = datos["Assists"].corr(datos["Progressive Passes"])
corr_dribbles_carries = datos["Successful Dribbles"].corr(datos["Progressive Carries"])

corr_df = pd.DataFrame({
    "Relación": ["Goals vs xG", "Assists vs ProgPasses", "Dribbles vs Carries"],
    "Correlación": [corr_goals_xg, corr_assists_passes, corr_dribbles_carries]
})

fig_corr = px.bar(
    corr_df,
    x="Correlación",
    y="Relación",
    title="Correlaciones",
    color="Correlación",
    color_continuous_scale=COLOR_BARS,
)

fig_corr.update_layout(template="plotly_white")

st.plotly_chart(fig_corr, use_container_width=True)



# HEATMAP 

st.header(" Heatmap  de correlaciones")

heatmap_df = pd.DataFrame({
    "Goals_vs_xG": [corr_goals_xg],
    "Assists_vs_ProgPasses": [corr_assists_passes],
    "Dribbles_vs_Carries": [corr_dribbles_carries]
})

st.dataframe(
    heatmap_df.style.background_gradient(cmap="coolwarm"),
    use_container_width=True
)

st.success("App ejecutada correctamente. ¡Buen trabajo ")
