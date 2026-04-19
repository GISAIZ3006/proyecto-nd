import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="IA Análisis Deportivo", page_icon="⚽")

st.title("⚽ Dashboard de Estadísticas + IA")
st.markdown("### Proyecto de Semestre: Data & Modeling")

if "GEMINI_API_KEY" in st.secrets:
    # Conexión con la clave
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    
    # Nombre de modelo completo para evitar el Error 404
    model = genai.GenerativeModel(model_name="models/gemini-1.5-flash-latest")
    
    pregunta = st.text_input("¿Qué quieres analizar hoy?")

    if pregunta:
        with st.spinner('Analizando con Gemini...'):
            try:
                # Generamos el contenido
                response = model.generate_content(pregunta)
                st.info(response.text)
            except Exception as e:
                st.error(f"Error en la API: {e}")
                st.write("Prueba a escribir algo más específico como: 'Resumen de Notre Dame'")
else:
    st.error("Por favor, configura la GEMINI_API_KEY en los Secrets de Streamlit.")
