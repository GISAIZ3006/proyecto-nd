import streamlit as st
import pandas as pd
import json
import os
from datetime import datetime

# --- CONFIGURACIÓN ---
st.set_page_config(page_title="Pulse of the Program", page_icon="☘️")

st.markdown("""
    <style>
    .report-box { border-left: 5px solid #002b5b; padding-left: 15px; margin-bottom: 20px; }
    .stButton>button { background-color: #002b5b; color: white; width: 100%; }
    </style>
    """, unsafe_allow_html=True)

# --- MODELO DE INTELIGENCIA ---
def get_nd_angle(trend):
    t = trend.lower()
    if "transfer portal" in t:
        return "⚠️ **STRATEGY:** Monitor safety depth. Graduate clearance is priority."
    elif "visit" in t or "commit" in t or "isaiah rogers" in t:
        return "👀 **RECRUIT ALERT:** Follow-up to Isaiah Rogers momentum. Secondary is solid."
    elif "offensive line" in t or "lt" in t:
        return "🔥 **BOARD HEAT:** Fan focus on LT battle. Address in Morning Notes."
    elif "playoff" in t:
        return "🏆 **POST-SEASON:** 12-team format favors ND's independent path."
    return "Analyzing sources for a specific local strategy..."

# --- CARGA DE DATOS ---
def load_data():
    file_path = 'news_data.json'
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f), os.path.getmtime(file_path)
    return None, None

# --- UI ---
st.title("☘️ Pulse of the Program")
st.subheader("Morning Intelligence Agent")

data, last_mod = load_data()

if last_mod:
    last_update = datetime.fromtimestamp(last_mod).strftime('%Y-%m-%d %H:%M')
    st.caption(f"Last automated sync: {last_update}")

if st.button("🚀 Generate Strategic Analysis"):
    if data:
        for item in data:
            with st.container():
                st.markdown(f"### {item['source']}")
                st.write(f"**Current Trend:** {item['trend']}")
                # Aplicamos el modelo
                angle = get_nd_angle(item['trend'])
                st.info(f"**ND Angle:** {angle}")
                st.divider()
        st.success("Analysis complete based on latest 8:00 AM data.")
    else:
        st.error("Data source not found. Please run the automated scraper.")
