
import streamlit as st
from model_utils import get_hr_score

st.set_page_config(page_title="HR Prediction Model", layout="centered")

st.title("💣 HR Prediction Model v3.0")

st.markdown("This tool estimates a hitter’s HR probability based on power, matchup, and conditions.")

with st.form("hr_form"):
    batter_name = st.text_input("🔤 Batter Name")

    st.markdown("### 🧨 Hitter Power (BPS)")
    barrel_rate = st.slider("Barrel Rate (%)", 0.0, 30.0, 10.0)
    exit_velocity = st.slider("Average Exit Velocity (mph)", 70.0, 120.0, 91.0)
    xSLG = st.select_slider("Expected Slugging (xSLG)", options=[0.350, 0.400, 0.450, 0.500, 0.550, 0.600, 0.650], value=0.500)
    sweet_spot = st.slider("Sweet Spot Contact (%)", 0.0, 60.0, 35.0)
    rpi = st.select_slider("🔥 Hot Streak Level (Recent Performance Index)", options=[0.2, 0.4, 0.6, 0.8, 1.0], value=0.6)

    st.markdown("### ⚠️ Pitcher Vulnerability (PVS)")
    hr9 = st.slider("HR Allowed per 9 IP", 0.0, 3.0, 1.2)
    hard_hit_pct = st.slider("Hard-Hit Rate Allowed (%)", 20.0, 60.0, 35.0)
    fatigue = st.slider("Pitcher Fatigue (0 = Fresh, 10 = Gassed)", 0, 10, 4)

    st.markdown("### 🌎 Game Context")
    park_factor = st.slider("Park HR Factor (–15 = Pitcher's Park, +15 = HR-friendly)", -15, 15, 0)
    wind_boost = st.slider("Wind Boost (mph out to OF)", -10, 10, 0)
    temp_boost = st.slider("Temp Boost (°F above 70)", 0, 30, 0)

    submitted = st.form_submit_button("📊 Calculate HR Probability")
    if submitted:
        score, sleeper = get_hr_score(barrel_rate, exit_velocity, xSLG, sweet_spot, rpi,
                                      hr9, hard_hit_pct, fatigue,
                                      park_factor, wind_boost, temp_boost)
        st.subheader(f"🔢 HR Score: {score:.1f} / 100")
        if sleeper:
            st.markdown("🧨 **Sleeper Tag: This batter has sneaky upside!**")
