import streamlit as st
import pandas as pd
import json
import os

# --- 1. CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(
    page_title="Pulse of the Program | Irish Breakdown",
    page_icon="☘️",
    layout="centered"
)

# Estilo profesional (Azul Navy y Dorado para ND)
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #002b5b;
        color: white;
    }
    .stInfo {
        background-color: #e8f4f8;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. MOTOR DE INTELIGENCIA (El "Modelo") ---
def get_nd_angle(trend):
    """
    Transforma noticias generales en estrategia local para Notre Dame.
    """
    t = trend.lower()
    
    if "transfer portal" in t:
        return "⚠️ **STRATEGY:** High impact on safety depth. Admissions must expedite graduate clearance."
    elif "visit" in t or "commit" in t or "isaiah rogers" in t:
        return "👀 **RECRUIT ALERT:** Follow-up to Isaiah Rogers momentum. Secondary is becoming a 'lock'."
    elif "offensive line" in t or "lt" in t:
        return "🔥 **BOARD HEAT:** Fans fixated on LT battle. Address this in today's 'Morning Notes'."
    elif "playoff" in t:
        return "🏆 **POST-SEASON:** 12-team format favors ND's independence. No conference title game needed."
    
    return "Analyzing sources for a specific local strategy..."

# --- 3. CARGA DE DATOS AUTOMATIZADA ---
def load_data():
    """
    Lee el archivo generado por GitHub Actions. 
    Si el archivo no existe (primera vez), usa datos de respaldo.
    """
    file_path = 'news_data.json'
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        # Datos de respaldo por si el scraper aún no ha corrido
        return [
            {"source": "System", "trend": "Esperando actualización de las 8:00 AM..."},
            {"source": "Manual", "trend": "No se encontró el archivo news_data.json"}
        ]

# --- 4. INTERFAZ DE USUARIO ---
st.title("☘️ Pulse of the Program")
st.subheader("Morning Intelligence Report (8:00 AM)")
st.markdown("---")

# Cargar las noticias del archivo JSON
data = load_data()

# Botón para generar el reporte basado en los datos actuales
if st.button("🚀 Generate Today's Intelligence"):
    st.write(f"**Report Date:** {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M')}")
    
    for item in data:
        with st.container():
            col1, col2 = st.columns([1, 4])
            with col1:
                st.caption(f"**[{item['source']}]**")
            with col2:
                st.write(f"**Trend:** {item['trend']}")
                
                # Ejecutar la lógica del modelo sobre la noticia real
                nd_angle = get_nd_angle(item['trend'])
                st.info(f"**ND Angle:** {nd_angle}")
            st.divider()
    
    st.success("Report Grounded in 'Irish Breakdown' context.")

# --- 5. SIDEBAR ---
with st.sidebar:
    st.header("Project Insights")
    st.write("**Student:** Gisela Sanchez Iznajar")
    st.write("**Data Pipeline:** Automated via GitHub Actions")
    st.markdown("---")
    st.write("### Tech Stack")
    st.info("Python + Streamlit + JSON + GitHub")
