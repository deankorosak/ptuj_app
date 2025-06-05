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


# Read HTML file
with open("ptuj_climate_map.html", "rb") as f:
    html_bytes = f.read()

# Method 1: Base64 iframe (often works better)
html_b64 = base64.b64encode(html_bytes).decode()
iframe_src = f"data:text/html;base64,{html_b64}"

st.markdown(f"""
<iframe src="{iframe_src}" 
        width="100%" 
        height="700" 
        frameborder="0" 
        sandbox="allow-scripts allow-same-origin allow-forms">
</iframe>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
---
*Climate analysis powered by Google Earth Engine • Visualization by geemap*
""")
