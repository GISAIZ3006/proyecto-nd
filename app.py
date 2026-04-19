import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="IA Análisis Deportivo", page_icon="⚽")

st.title("⚽ Dashboard de Estadísticas + IA")
st.markdown("### Proyecto de Semestre: Data & Modeling")

if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    
    # Intentamos listar los modelos para ver cuál está disponible
    try:
        # Intentamos primero con el nombre más común
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # Si falla en el siguiente paso, el 'except' lo capturará
    except Exception:
        # Si falla el anterior, usamos el modelo Pro por defecto
        model = genai.GenerativeModel('gemini-pro')

    pregunta = st.text_input("¿Qué quieres analizar hoy?")

    if pregunta:
        with st.spinner('El Gem está pensando...'):
            try:
                # Intentamos generar el contenido
                response = model.generate_content(pregunta)
                st.info(response.text)
            except Exception as e:
                # Si sigue fallando, mostramos un mensaje de diagnóstico
                st.error("Error de conexión con el modelo.")
                st.write("Copia este error para tu reporte de clase:")
                st.code(f"Diagnóstico: {str(e)}")
else:
    st.error("Configura la GEMINI_API_KEY en Advanced Settings de Streamlit.")
