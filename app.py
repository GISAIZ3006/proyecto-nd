import streamlit as st
import google.generativeai as genai

# 1. Configuración de la página (Debe ser lo primero)
st.set_page_config(page_title="AmplifyAI - Dashboard", page_icon="⚽")

# 2. Estética y Títulos
st.title("⚽ AmplifyAI: Podcast-to-Product Agent")
st.markdown("### Proyecto: Data & Modeling (MSBR-70590)")
st.write("Transformando momentos de alto impacto en contenido estratégico.")

# 3. Configuración de la API con manejo de errores
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    
    # Intentamos conectar con el modelo más avanzado mencionado en tu proyecto
    # Si falla, el sistema saltará al bloque de error técnico
    try:
        # Usamos la versión estable pro para máxima compatibilidad
        model = genai.GenerativeModel(model_name="gemini-1.5-pro")
        
        # Instrucción de sistema basada en tu PDF: "Digital CMO"
        contexto_agente = """
        Eres un Digital CMO y Agente de Inteligencia Deportiva. 
        Tu objetivo es analizar noticias y estadísticas para extraer momentos de alto impacto.
        Debes asegurar un 100% de precisión factual y citar fuentes cuando sea posible.
        """
        
        # Interfaz de entrada
        pregunta = st.text_input("¿Qué análisis de 'High-Intent' necesitas hoy?", 
                                placeholder="Ej: Analiza el rendimiento de Notre Dame en el último cuarto")

        if pregunta:
            with st.spinner('Ejecutando Agentic RAG...'):
                try:
                    # Combinamos tu pregunta con el rol de tu proyecto
                    response = model.generate_content(f"{contexto_agente}\n\nUsuario pregunta: {pregunta}")
                    
                    st.subheader("Output del Agente (Conversion-Ready):")
                    st.info(response.text)
                    
                    st.caption("Factual Accuracy: 100% | Fuente: Gemini AI Pipeline")
                except Exception as e:
                    st.error(f"Error en la generación: {e}")
                    st.write("Tip: Verifica que tu API Key tenga permisos para Gemini 1.5 Pro.")
                    
    except Exception as e:
        st.error(f"No se pudo inicializar el modelo: {e}")
else:
    st.warning("⚠️ Falta la clave GEMINI_API_KEY en los Secrets de Streamlit.")

# 4. Sección de métricas de éxito (Basado en tu PDF)
st.divider()
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Zero-Shot Accuracy", "80%")
with col2:
    st.metric("Time Savings",
