import streamlit as st
import streamlit.components.v1 as components
import pandas as pd

# ---------------- CONFIG ----------------
st.set_page_config(
    page_title="Battery Elements Explorer",
    page_icon="🔋",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- CUSTOM STYLING ----------------
st.markdown("""
    <style>
    /* Global background */
    .stApp {
        background: linear-gradient(135deg, #f0f9ff, #cbebff, #a6e3e9);
        font-family: 'Segoe UI', sans-serif;
    }
    /* Sidebar styling */
    section[data-testid="stSidebar"] {
        background: #1e3a8a;
        color: white;
    }
    section[data-testid="stSidebar"] .stRadio > label {
        color: white;
        font-weight: 600;
    }
    section[data-testid="stSidebar"] h1, h2, h3 {
        color: white;
    }
    /* Titles */
    h1 {
        color: #0f172a;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
    }
    h2, h3 {
        color: #1e293b;
    }
    /* Tables */
    .stTable {
        background: white;
        border-radius: 10px;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
    }
    /* Markdown text */
    p, li {
        font-size: 1.05rem;
        line-height: 1.6;
    }
    /* Buttons and selectbox */
    .stSelectbox div {
        background: white;
        border-radius: 8px;
        padding: 6px;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
st.sidebar.title("🔍 Navigation")
page = st.sidebar.radio(
    "Go to:",
    ["⚛️ Atomic Models", "📊 Physical Properties", "☢️ Nuclear & E-Waste Effects"]
)

# ---------------- PAGE 1: Atomic Models ----------------
if page == "⚛️ Atomic Models":
    st.title("⚛️ Atomic Models of Battery Elements")

    st.write("Explore the **3D atomic structures** of Lithium and Lead, "
             "two essential elements in electronic batteries. "
             "🔄 Rotate, zoom, and inspect the atoms interactively!")

    elements = {
        "Lithium": {
            "embed": "https://sketchfab.com/models/163af8fd340c4b68b50f0bbe5317af97/embed",
            "formula": "🔋 LiC₆ + CoO₂ → C₆ + LiCoO₂"
        },
        "Lead": {
            "embed": "https://sketchfab.com/models/9e44979216c748beb9abe9536f7fdbbd/embed",
            "formula": "🔋 Pb + PbO₂ + 2H₂SO₄ → 2PbSO₄ + 2H₂O"
        }
    }

    choice = st.selectbox("🔎 Choose an element:", list(elements.keys()))

    st.subheader(f"⚗️ Discharge Formula for {choice}")
    st.markdown(f"<div style='padding:10px; background:white; border-radius:10px; box-shadow:0px 3px 8px rgba(0,0,0,0.1); font-size:1.1rem;'><b>{elements[choice]['formula']}</b></div>", unsafe_allow_html=True)

    st.subheader(f"🧩 3D Atomic Model of {choice}")
    components.iframe(elements[choice]["embed"], height=600)

# ---------------- PAGE 2: Physical Properties ----------------
elif page == "📊 Physical Properties":
    st.title("📊 Physical Properties of Lithium & Lead")
    st.write("Here’s a comparison of important physical properties of **Lithium (Li)** and **Lead (Pb)**.")

    data = {
        "Property": [
            "🔥 Boiling Point (°C)",
            "❄️ Melting Point (°C)",
            "🌡️ Heat Capacity (J/g·K)",
            "⚡ Electrical Conductivity",
            "🔎 Periodic Table Group",
            "➕ Protons",
            "➖ Neutrons",
            "🟢 Electrons"
        ],
        "Lithium (Li)": [
            "1342", "180.5", "3.58", "Good conductor", "Alkali Metal (Group 1)", "3", "4", "3"
        ],
        "Lead (Pb)": [
            "1749", "327.5", "0.13", "Poor conductor", "Post-Transition Metal (Group 14)", "82", "125", "82"
        ]
    }

    df = pd.DataFrame(data)
    st.table(df)

# ---------------- PAGE 3: Nuclear & E-Waste ----------------
elif page == "☢️ Nuclear & E-Waste Effects":
    st.title("☢️ Nuclear Significance & E-Waste Effects")
    st.write("""
    ### ⚛️ Nuclear Significance
    - **Lithium (Li):** Used in fusion research and nuclear technology as a coolant and tritium source.  
    - **Lead (Pb):** Used as radiation shielding due to its high density.

    ### ♻️ Electronic Waste Concerns
    - **Lithium Batteries:**  
      🔋 Can leak toxic electrolytes and heavy metals if not disposed properly.  
      🌍 Mining lithium harms ecosystems and uses large amounts of water.  

    - **Lead Batteries:**  
      ☣️ Lead is highly toxic, damaging the brain, kidneys, and nervous system.  
      🚯 Lead-acid batteries are the **most recycled** consumer product, but unsafe recycling still causes pollution.  

    ### ✅ Safer Practices
    - Encourage recycling through official programs.  
    - Reduce use of toxic materials in future battery designs.  
    - Explore eco-friendly alternatives (e.g., sodium-ion batteries).
    """)

    st.success("⚡ Knowledge is power — let's use it to build safer and greener batteries!")
