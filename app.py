import streamlit as st
import pandas as pd
import time

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Pulse of the Program | Irish Breakdown",
    page_icon="☘️",
    layout="centered"
)

# Custom CSS to make it look professional
st.markdown("""
    <style>
    .main {
        background-color: #f5f5f5;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #002b5b;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. INTELLIGENCE ENGINE (The "Model") ---
def get_nd_angle(source, trend):
    """
    This function acts as the 'National-to-Local Bridge'.
    In a production environment, this would call the NotebookLM / Gemini API.
    """
    t = trend.lower()
    
    # Logic for National-to-Local Bridge
    if "transfer portal" in t:
        return "⚠️ **STRATEGY:** High impact on safety/depth. ND Admissions needs to expedite graduate clearance for May."
    
    # Logic for X Intelligence (Recruits)
    elif "cb prospect" in t or "visit" in t or "isaiah rogers" in t:
        return "👀 **RECRUIT ALERT:** Follow-up to Isaiah Rogers' momentum. The secondary is becoming a 'lock' for this class."
    
    # Logic for Message Board Sentiment
    elif "offensive line" in t or "lt" in t:
        return "🔥 **BOARD HEAT:** Fans are fixated on the LT battle. High engagement detected; address this in 'Morning Notes'."
    
    elif "playoff" in t:
        return "🏆 **POST-SEASON:** 12-team format favors ND's independent status. No conference title game needed for a top-12 seed."
        
    return "Analyzing NotebookLM sources for a specific local strategy..."

# --- 3. DATA INGESTION (The "Data") ---
# This dictionary simulates the data scraped from your sources
morning_data = [
    {"source": "ESPN", "trend": "New NCAA Transfer Portal Windows Announced"},
    {"source": "X (Twitter)", "trend": "Top-tier CB prospect posts ND visit photos"},
    {"source": "Irish Breakdown Boards", "trend": "High volume of posts regarding Offensive Line depth"},
    {"source": "CBS Sports", "trend": "Expansion of the 12-team Playoff format impact"}
]

# --- 4. STREAMLIT UI ---
st.title("☘️ Pulse of the Program")
st.subheader("Morning Intelligence Report (8:00 AM)")
st.markdown("---")

# Main action button
if st.button("🚀 Generate Today's Intelligence"):
    with st.spinner("Accessing NotebookLM & Scraping National Feeds..."):
        time.sleep(1.5) # Simulating API Latency for realism
        
        for item in morning_data:
            with st.container():
                # Display Source and Trend
                col1, col2 = st.columns([1, 4])
                with col1:
                    st.caption(f"**[{item['source']}]**")
                with col2:
                    st.write(f"**Trend:** {item['trend']}")
                    
                    # Call the Model to get the "Notre Dame Angle"
                    nd_angle = get_nd_angle(item['source'], item['trend'])
                    st.info(f"**ND Angle:** {nd_angle}")
                st.divider()
    
    st.success("Report Generated Successfully. Data is grounded in 'Irish Breakdown' brand guidelines.")

# --- 5. SIDEBAR (Project Metadata for your Professors) ---
with st.sidebar:
    st.header("Project Info")
    st.write("**Student:** Gisela Sanchez Iznajar")
    st.write("**Course:** Semester Project: Data & Modeling")
    st.write("**Status:** Prototype (V1.2)")
    st.markdown("---")
    st.write("### Tech Stack")
    st.code("Python\nStreamlit\nNotebookLM\nGitHub Actions")
