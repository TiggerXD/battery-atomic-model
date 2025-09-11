import streamlit as st
import pandas as pd

# --- Page Config ---
st.set_page_config(page_title="Battery Elements Explorer", layout="wide")
st.markdown("<h1 style='text-align:center;color:#00ffff'>🔬 Battery Elements Explorer</h1>", unsafe_allow_html=True)

# --- Sidebar ---
st.markdown("""
    <style>
    .sidebar .sidebar-content {
        background: linear-gradient(#111111,#333333);
        border-radius: 15px;
        padding: 15px;
    }
    .sidebar .sidebar-content h2 {
        color: #00ffff;
    }
    .stRadio>div>div, .stSelectbox>div>div {
        border-radius: 10px;
        background-color: #222222;
        color: #00ffff;
        padding: 5px;
    }
    </style>
""", unsafe_allow_html=True)

st.sidebar.title("⚡ Explore Elements")
element = st.sidebar.selectbox("Select Element", ["Lithium (Li)", "Lead (Pb)"])
page = st.sidebar.radio("Navigate", ["⚛️ Atomic Model", "📊 Physical Properties", "☢️ Nuclear & E-Waste"])

# --- Element Data ---
element_data = {
    "Lithium (Li)": {
        "formula": "LiC6 + CoO2 → C6 + LiCoO2",
        "boiling": "1342°C",
        "melting": "180.5°C",
        "heat_capacity": "3.58 J/g·K",
        "conductivity": "✅ Good conductor",
        "group": "Alkali Metal (Group 1)",
        "protons": 3,
        "neutrons": 4,
        "electrons": 3,
        "nuclear_symbol": "Li",
        "atomic_number": 3,
        "e_waste": "⚠️ Can leak toxic electrolytes, high water usage in mining.",
        "sketchfab_embed": "https://sketchfab.com/models/163af8fd340c4b68b50f0bbe5317af97/embed"
    },
    "Lead (Pb)": {
        "formula": "Pb + PbO2 + 2H2SO4 → 2PbSO4 + 2H2O",
        "boiling": "1749°C",
        "melting": "327.5°C",
        "heat_capacity": "0.13 J/g·K",
        "conductivity": "⚠️ Poor conductor",
        "group": "Post-Transition Metal (Group 14)",
        "protons": 82,
        "neutrons": 125,
        "electrons": 82,
        "nuclear_symbol": "Pb",
        "atomic_number": 82,
        "e_waste": "☣️ Highly toxic, unsafe recycling pollutes soil & water.",
        "sketchfab_embed": "https://sketchfab.com/models/9e44979216c748beb9abe9536f7fdbbd/embed"
    }
}
data = element_data[element]

# --- Page 1: Atomic Model (Embedded) ---
if page == "⚛️ Atomic Model":
    st.markdown(f"<h2 style='color:#00ff00'>⚛️ 3D Model of {element}</h2>", unsafe_allow_html=True)
    st.markdown(f"<b style='color:#ffff00'>Discharge Formula:</b> <span style='color:#ffffff'>{data['formula']}</span>", unsafe_allow_html=True)
    
    # Embed Sketchfab model
    embed_code = f"""
    <iframe title="{element} 3D Model" width="100%" height="500" src="{data['sketchfab_embed']}" frameborder="0" allowfullscreen allow="autoplay; fullscreen; xr-spatial-tracking"></iframe>
    """
    st.components.v1.html(embed_code, height=550)

# --- Page 2: Physical Properties ---
elif page == "📊 Physical Properties":
    st.markdown(f"<h2 style='color:#00ff00'>📊 Physical Properties of {element}</h2>", unsafe_allow_html=True)
    properties = {
        "Property": ["Boiling Point", "Melting Point", "Heat Capacity", "Electrical Conductivity",
                     "Periodic Table Group", "Protons", "Neutrons", "Electrons"],
        element: [data['boiling'], data['melting'], data['heat_capacity'], data['conductivity'],
                  data['group'], data['protons'], data['neutrons'], data['electrons']]
    }
    df = pd.DataFrame(properties)
    # Highlight important properties
    def highlight_props(x):
        important = ['Boiling Point','Melting Point','Electrical Conductivity','Protons','Neutrons','Electrons']
        return ['background-color:#444444; color:#ffff00' if v in important else 'background-color:#222222; color:#00ffff' for v in x]
    st.dataframe(df.style.apply(highlight_props, axis=0))

# --- Page 3: Nuclear & E-Waste ---
elif page == "☢️ Nuclear & E-Waste":
    st.markdown(f"<h2 style='color:#00ff00'>☢️ Nuclear Info & Environmental Impact of {element}</h2>", unsafe_allow_html=True)
    st.markdown(f"<b style='color:#ffff00'>Symbol:</b> <span style='color:#ffffff'>{data['nuclear_symbol']}</span>", unsafe_allow_html=True)
    st.markdown(f"<b style='color:#ffff00'>Atomic Number:</b> <span style='color:#ffffff'>{data['atomic_number']}</span>", unsafe_allow_html=True)
    st.markdown(f"<b style='color:#ff3333'>E-Waste Effect:</b> <span style='color:#ffffff'>{data['e_waste']}</span>", unsafe_allow_html=True)
    st.success("✅ Always recycle batteries responsibly!")
