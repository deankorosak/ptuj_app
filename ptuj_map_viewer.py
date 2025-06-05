# ptuj_map_viewer.py
import streamlit as st
import base64

st.set_page_config(
    page_title="Ptuj Climate Analysis", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# Header
st.markdown("""
# Ptuj Urban Climate Analysis
**Interactive microscale climate mapping** • *2019-2024 Analysis*

---
""")


external_url = "https://deankorosak.github.io/ptuj_climate_map.html"

st.markdown(f"""
<iframe src="{external_url}" 
        width="100%" 
        height="700" 
        frameborder="0">
</iframe>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
---
*Climate analysis powered by Google Earth Engine • Visualization by geemap*
""")
