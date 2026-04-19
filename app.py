import streamlit as st
import google.generativeai as genai

# ESTA DEBE SER LA PRIMERA LÍNEA DE STREAMLIT DESPUÉS DE LOS IMPORTS
st.set_page_config(page_title="IA Análisis Deportivo", page_icon="⚽")

st.title("⚽ Dashboard de Estadísticas + IA")
st.markdown("### Proyecto de Semestre: Data & Modeling")

# Conectamos con tu API Key de los Secrets
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    pregunta = st.text_input("¿Qué quieres analizar hoy?")

    if pregunta:
        with st.spinner('Analizando...'):
            try:
                response = model.generate_content(pregunta)
                st.info(response.text)
            except Exception as e:
                st.error(f"Error: {e}")
else:
    st.error("Configura la GEMINI_API_KEY en Advanced Settings de Streamlit.")
