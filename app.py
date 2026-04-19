

# Configuración de la página
st.set_page_config(page_title="IA Análisis Deportivo", page_icon="⚽")

# Título de tu proyecto
st.title("⚽ Dashboard de Estadísticas + IA")
st.markdown("### Proyecto de Semestre: Data & Modeling")

# Conectamos con tu API Key (la configuraremos luego en la web de Streamlit)
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    # Interfaz de usuario
    st.write("Bienvenido al sistema de análisis. Este prototipo usa IA para interpretar noticias y datos.")
    
    pregunta = st.text_input("¿Qué equipo o estadística quieres analizar hoy?", placeholder="Ej: Noticias recientes de Notre Dame")

    if pregunta:
        with st.spinner('El Gem está analizando la información...'):
            try:
                # Instrucción para que actúe como tu Gem experto
                prompt_full = f"Actúa como un experto analista deportivo. Responde de forma clara y directa a: {pregunta}"
                response = model.generate_content(prompt_full)
                
                st.subheader("Análisis del Gem:")
                st.info(response.text)
            except Exception as e:
                st.error("Hubo un error con la conexión a la IA.")
else:
    st.warning("⚠️ Configuración pendiente: Por favor, añade la GEMINI_API_KEY en los Secrets de Streamlit.")

# Sección de estadísticas (Ejemplo visual para tu reporte)
st.divider()
st.write("Ejemplo de visualización de datos:")
st.line_chart({"Puntos por partido": [14, 21, 10, 35, 28]})
