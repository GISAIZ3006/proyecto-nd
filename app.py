import streamlit as st
import time

# Título con estilo
st.title("✨ AI Sales & Marketing Agent")
st.caption("Especializado en Estrategia Deportiva y Retail")

if prompt := st.chat_input("Pregúntame sobre el mejor jugador o estrategia..."):
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        # 1. Indicador visual de que la IA está "pensando" o "leyendo"
        with st.spinner("Consultando fuentes en NotebookLM..."):
            # Simulamos el tiempo de proceso del RAG
            time.sleep(2) 
            
            # Lógica de respuesta
            if "jugador" in prompt.lower():
                response = "Basado en los datos de rendimiento de la temporada, el 'mejor jugador' se define por su eficiencia en momentos críticos. Según tus fuentes, este perfil encaja con..."
            else:
                response = "Estoy procesando la información de tus documentos para darte una respuesta exacta."
            
            st.markdown(response)
