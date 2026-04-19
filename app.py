import streamlit as st
import pandas as pd

# 1. UI Setup
st.title("☘️ Pulse of the Program")
st.subheader("Morning Intelligence Report (8:00 AM)")

# 2. Simulated Intelligence Logic
def get_nd_angle(national_headline):
    # This logic mimics the "Gem" specialized for Bryan Driskell
    if "Recruit" in national_headline:
        return "Action: Cross-reference with Isaiah Rogers' latest X activity."
    elif "NIL" in national_headline:
        return "Angle: How this impacts the current ND donor collective strategy."
    return "Status: Monitor for potential impact on Irish Breakdown topics."

# 3. Data Presentation
news_data = [
    {"source": "ESPN", "headline": "New NCAA Transfer Portal Windows Announced"},
    {"source": "X", "headline": "Top-tier CB prospect posts ND visit photos"}
]

if st.button("Generate Today's Report"):
    for item in news_data:
        with st.container():
            st.write(f"**Source:** {item['source']}")
            st.write(f"**Trend:** {item['headline']}")
            st.success(f"**ND Angle:** {get_nd_angle(item['headline'])}")
            st.divider()
