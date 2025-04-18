
import streamlit as st
from model_utils import get_hr_score

st.set_page_config(page_title="HR Prediction Model", layout="centered")

st.title("HR Prediction Model v3.0")

with st.form("hr_form"):
    batter_name = st.text_input("Batter Name")
    barrel_rate = st.slider("Barrel Rate (%)", 0.0, 30.0, 8.0)
    exit_velocity = st.slider("Exit Velocity (mph)", 70.0, 120.0, 89.0)
    xSLG = st.slider("Expected Slugging (xSLG)", 0.200, 1.000, 0.450)
    sweet_spot = st.slider("Sweet Spot %", 0.0, 100.0, 35.0)
    rpi = st.slider("Recent Performance Index", 0.0, 1.0, 0.5)
    
    hr9 = st.slider("Pitcher HR/9", 0.0, 3.0, 1.2)
    hard_hit_pct = st.slider("Hard-Hit % Allowed", 0.0, 60.0, 35.0)
    fatigue = st.slider("Fatigue Factor (0–10)", 0, 10, 5)
    
    park_factor = st.slider("Ballpark HR Factor", -15, 15, 0)
    wind_boost = st.slider("Wind Boost (mph)", -10, 10, 0)
    temp_boost = st.slider("Temp Boost (°F above 70)", 0, 30, 0)
    
    submitted = st.form_submit_button("Calculate HR Probability")
    if submitted:
        score, sleeper = get_hr_score(barrel_rate, exit_velocity, xSLG, sweet_spot, rpi,
                                      hr9, hard_hit_pct, fatigue,
                                      park_factor, wind_boost, temp_boost)
        st.subheader(f"HR Score: {score:.1f}/100")
        if sleeper:
            st.markdown("**Sleeper Tag: This batter has sneaky upside.**")
