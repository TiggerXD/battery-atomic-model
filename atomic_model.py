import streamlit as st
import pandas as pd

# --- Custom CSS for global styling ---
st.markdown("""
<style>
/* Sidebar styling */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #1e3a8a, #3b82f6);
    padding: 20px;
}
section[data-testid="stSidebar"] h1, 
section[data-testid="stSidebar"] h2, 
section[data-testid="stSidebar"] h3, 
section[data-testid="stSidebar"] p {
    color: white !important;
}
/* Sidebar buttons */
div[data-baseweb="radio"] label {
    background: white;
    color: #1e3a8a;
    border-radius: 10px;
    padding: 10px 15px;
    margin: 5px 0;
    font-weight: bold;
    transition: 0.3s;
    box-shadow: 0 2px 6px rgba(0,0,0,0.2);
}
div[data-baseweb="radio"] label:hover {
    background: #93c5fd;
    color: #111827;
    cursor: pointer;
}
/* Highlight styles */
.highlight-blue {
    background: #dbeafe;
    color: #1e3a8a;
    padding: 2px 6px;
    border-radius: 6px;
    font-weight: bold;
}
.good {
    background: #dcfce7;
    color: #166534;
    padding: 4px 8px;
    border-radius: 6px;
    font-weight: bold;
}
.bad {
    background: #fee2e2;
    color: #991b1b;
    padding: 4px 8px;
    border-radius: 6px;
    font-weight: bold;
}
/* Table styling */
.styled-table {
    border-collapse: collapse;
    margin: 20px 0;
    font-size: 1rem;
    width: 100%;
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 3px 10px rgba(0,0,0,0.15);
}
.styled-table th {
    background: #1e3a8a;
    color: white;
    text-align: center;
    padding: 12px;
}
.styled-table td {
    background: #f0f9ff;
    text-align: center;
    padding: 10px;
    color: #0f172a;
    font-weight: 500;
}
.styled-table tr:nth-child(even) td {
    background: #dbeafe;
}
</style>
""", unsafe_allow_html=True)

# --- Sidebar Navigation ---
st.sidebar.title("🔬 Battery Elements Explorer")
page = st.sidebar.radio("Navigate", 
                        ["⚛️ Atomic Models", 
                         "📊 Physical Properties", 
                         "☢️ Nuclear Info & E-Waste"])

# --- Page 1: Atomic Models ---
if page == "⚛️ Atomic Models":
    st.title("⚛️ Atomic Models of Lithium & Lead")
    st.markdown("Explore the **3D models** of "
                "<span class='highlight-blue'>Lithium</span> and "
                "<span class='highlight-blue'>Lead</span> atoms, "
                "and their role in **battery chemistry** 🔋.",
                unsafe_allow_html=True)

    st.subheader("Lithium (Li) – Discharging Formula")
    st.markdown("`LiC6 + CoO2 → C6 + LiCoO2`")
    st.components.v1.iframe("https://sketchfab.com/models/163af8fd340c4b68b50f0bbe5317af97/embed", 
                             height=400)

    st.subheader("Lead (Pb) – Discharging Formula")
    st.markdown("`Pb + PbO2 + 2H2SO4 → 2PbSO4 + 2H2O`")
    st.components.v1.iframe("https://sketchfab.com/models/9e44979216c748beb9abe9536f7fdbbd/embed", 
                             height=400)

# --- Page 2: Physical Properties ---
elif page == "📊 Physical Properties":
    st.title("📊 Physical Properties of Lithium & Lead")
    st.write("Here’s a comparison of important physical properties of "
             "<span class='highlight-blue'>Lithium (Li)</span> "
             "and <span class='highlight-blue'>Lead (Pb)</span>.",
             unsafe_allow_html=True)

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
            "1342", "180.5", "3.58", "<span class='good'>✅ Good conductor</span>", 
            "Alkali Metal (Group 1)", "3", "4", "3"
        ],
        "Lead (Pb)": [
            "1749", "327.5", "0.13", "<span class='bad'>⚠️ Poor conductor</span>", 
            "Post-Transition Metal (Group 14)", "82", "125", "82"
        ]
    }

    df = pd.DataFrame(data)
    st.markdown(df.to_html(index=False, escape=False, classes="styled-table"), unsafe_allow_html=True)

# --- Page 3: Nuclear Info & E-Waste ---
elif page == "☢️ Nuclear Info & E-Waste":
    st.title("☢️ Nuclear Info & Environmental Impact")
    st.markdown("Both Lithium and Lead have **nuclear symbols** and "
                "play critical roles in **battery technology**. "
                "But battery disposal creates **electronic waste (e-waste)** 🌍.", 
                unsafe_allow_html=True)

    st.subheader("🧪 Nuclear Information")
    st.markdown("""
    - Lithium: Symbol = **Li**, Atomic Number = **3**
    - Lead: Symbol = **Pb**, Atomic Number = **82**
    """)

    st.subheader("♻️ Effects of Electronic Waste")
    st.markdown("""
    - ⚠️ **Soil & Water Contamination** from heavy metals.  
    - 🧍 **Health Risks**: Lead exposure damages the nervous system.  
    - 🌍 **Environmental Damage**: Improper disposal harms ecosystems.  
    - 💡 **Solution**: Recycling batteries reduces pollution and saves resources.  
    """)

    st.success("✅ Always recycle batteries responsibly to protect the environment!")
