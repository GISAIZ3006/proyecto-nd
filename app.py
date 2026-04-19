import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="IA Análisis Deportivo", page_icon="⚽")

st.title("⚽ Dashboard de Estadísticas + IA")
st.markdown("### Proyecto de Semestre: Data & Modeling")

if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    
    # Usamos 'gemini-pro' que es el modelo estándar más estable para la API
    model = genai.GenerativeModel('gemini-pro')
    
    pregunta = st.text_input("¿Qué quieres analizar hoy?")

    if pregunta:
        with st.spinner('Analizando...'):
            try:
                response = model.generate_content(pregunta)
                st.info(response.text)
            except Exception as e:
                st.error(f"Error técnico: {e}")
else:
    st.error("Configura la GEMINI_API_KEY en Advanced Settings de Streamlit.")
