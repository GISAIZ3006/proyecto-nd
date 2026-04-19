import streamlit as st

# Diccionario simulado de tendencias nacionales
national_trends = [
    {"topic": "Cambios en las reglas de NIL", "source": "ESPN"},
    {"topic": "Nuevas formaciones ofensivas en la SEC", "source": "CBS Sports"}
]

def generate_nd_angle(topic):
    # Aquí es donde NotebookLM y tus Gems harían la magia
    if "NIL" in topic:
        return "Impacto en ND: Podría acelerar las negociaciones con los reclutas de la clase 2026."
    elif "ofensiva" in topic:
        return "Impacto en ND: Mike Denbrock podría adaptar esto para aprovechar la movilidad de los QBs."
    return "Tendencia bajo observación para el programa."

st.header("☘️ Pulse of the Program: Morning Report")

if st.button("Generar Reporte de las 8:00 AM"):
    for trend in national_trends:
        with st.expander(f"Noticia: {trend['topic']}"):
            st.write(f"**Fuente:** {trend['source']}")
            st.info(generate_nd_angle(trend['topic']))
