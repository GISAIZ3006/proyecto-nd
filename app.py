import streamlit as st

# Configuración de la página con estilo profesional
st.set_page_config(page_title="AI Sales Agent", page_icon="🤖")

# Título con el enfoque de tu proyecto
st.title("✨ AI Sales & Marketing Agent")
st.markdown("### Powered by NotebookLM & Gemini")

# Simulación de la lógica de "Source Grounding" que aprendiste en NotebookLM
def get_ai_response(user_input):
    # Aquí es donde el chatbot "vibraría" con la lógica de tu Gem
    if "atleta" in user_input.lower():
        return "Según los lineamientos de ND Athletics, el mensaje debe enfocarse en la superación."
    elif "producto" in user_input.lower():
        return "Para maximizar ventas, el agente sugiere un Carousel de Instagram con brillos/rhinestones."
    else:
        return "Estoy analizando tus fuentes de NotebookLM para darte la mejor estrategia..."

# Interfaz de Chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostrar historial de chat
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input del usuario
if prompt := st.chat_input("¿Cómo puedo ayudarte con tu estrategia de ventas hoy?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Respuesta del modelo
    response = get_ai_response(prompt)
    
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
