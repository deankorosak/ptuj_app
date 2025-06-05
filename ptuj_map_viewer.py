# ptuj_map_viewer.py
import streamlit as st

st.set_page_config(
    page_title="Ptuj Climate Analysis", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# Header
st.markdown("""
# 🌡️ Ptuj Urban Climate Analysis
**Interactive microscale climate mapping** • *2019-2024 Analysis*

---
""")

# Info in sidebar
st.sidebar.markdown("""
### 🗺️ **Map Controls**
Use the layer panel in the map to:
- Toggle different climate layers
- Adjust layer opacity
- Zoom and pan around Ptuj

### 📊 **Available Layers**
- **🌡️ Mean Temperature** - Multi-year average
- **📈 Temperature Variability** - Standard deviation
- **🏙️ Urban Heat Islands** - Heat intensity mapping  
- **📉 Temperature Trends** - Warming/cooling patterns
- **🔥 Heat Stress Days** - Days above 35°C

### 📍 **Study Area**
- **Location**: Ptuj, Slovenia
- **Radius**: 5 km from city center
- **Data Source**: Landsat 8 thermal imagery
- **Resolution**: 30m pixels
""")

# Load and display the HTML map
try:
    with open("ptuj_climate_map.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    
    # Display the map
    st.components.v1.html(html_content, height=650, scrolling=False)
    
    # Success message
    st.success("✅ Interactive map loaded successfully!")
    
    # Additional info below map
    st.markdown("""
    ---
    ### 💡 **How to Use This Map**
    
    1. **Layer Control**: Click the layers icon (📋) in the top-right of the map
    2. **Zoom**: Use mouse wheel or +/- buttons
    3. **Pan**: Click and drag to move around
    4. **Measure**: Use the ruler tool for distance measurements
    5. **Fullscreen**: Click the expand button for full-screen view
    
    ### 📊 **Understanding the Data**
    - **Blue areas**: Cooler temperatures
    - **Red areas**: Warmer temperatures  
    - **Heat islands**: Urban areas warmer than surroundings
    - **Temporal trends**: Shows warming (red) or cooling (blue) over time
    """)

except FileNotFoundError:
    st.error("""
    ❌ **Map file not found!**
    
    Please make sure `ptuj_climate_map.html` is in the same folder as this app.
    
    To create the map file, run your analysis script and export with:
    ```python
    m.to_html("ptuj_climate_map.html")
    ```
    """)

except Exception as e:
    st.error(f"❌ **Error loading map**: {e}")
    
    st.info("""
    **Troubleshooting tips:**
    1. Check that the HTML file exists
    2. Ensure the file isn't corrupted
    3. Try re-exporting from your analysis script
    """)

# Footer
st.markdown("""
---
*Climate analysis powered by Google Earth Engine • Visualization by geemap*
""")