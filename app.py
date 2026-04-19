import streamlit as st
import pandas as pd

# --- TITLES & UI ---
st.title("☘️ Pulse of the Program")
st.subheader("Morning Intelligence Report (8:00 AM)")

# --- LOGIC: The 3 Pillars of your Objective ---

def process_intelligence(source, trend):
    """
    This function replaces the 'Monitor status' with actual 
    National-to-Local Bridge logic.
    """
    t = trend.lower()
    
    # 1. National-to-Local Bridge Logic
    if "transfer portal" in t:
        return "⚠️ **STRATEGY:** ND needs to evaluate depth at Safety immediately. With the new window, graduate transfers must be cleared by Admissions before May 1st."
    
    # 2. X Intelligence (Recruit Tracking)
    elif "cb prospect" in t or "visit" in t:
        return "👀 **RECRUIT ALERT:** This visit aligns with Isaiah Rogers' recent commitment. Strong momentum for the secondary; expect a 'Hot Topic' on the boards by noon."
    
    # 3. Message Board Sentiment (General)
    elif "offensive line" in t:
        return "🔥 **SENTIMENT:** Fans are highly critical of the LT position. Bryan, you should address the 'Left Tackle battle' in today's Morning Notes."
    
    else:
        return "Analyzing NotebookLM sources for a specific Irish Breakdown angle..."

# --- DATA: Actual Content ---
# In your final version, this would come from an API or Scraper.
raw_news = [
    {
        "source": "ESPN", 
        "trend": "New NCAA Transfer Portal Windows Announced"
    },
    {
        "source": "X (Twitter)", 
        "trend": "Top-tier CB prospect posts ND visit photos (Isaiah Rogers effect)"
    },
    {
        "source": "Message Boards",
        "trend": "High volume of posts regarding Offensive Line depth"
    }
]

# --- EXECUTION ---
if st.button("🚀 Generate 8:00 AM Report"):
    for item in raw_news:
        with st.container():
            col1, col2 = st.columns([1, 4])
            with col1:
                st.write(f"**[{item['source']}]**")
            with col2:
                st.write(f"**Trend:** {item['trend']}")
                
                # Here we call the logic instead of the static status
                nd_angle = process_intelligence(item['source'], item['trend'])
                st.info(f"**ND Angle:** {nd_angle}")
            st.divider()
