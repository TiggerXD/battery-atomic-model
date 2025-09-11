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
element = st.sidebar.selectbox("Select Element", ["Lithium (Li)", "Lead (Pb)"])
page = st.sidebar.radio("Navigate", 
                        ["⚛️ Atomic Model", "📊 Physical Properties", "☢️ Nuclear Info & E-Waste"])

# --- Element Data ---
element_data = {
    "Lithium (Li)": {
        "formula": "LiC6 + CoO2 → C6 + LiCoO2",
        "model": "https://sketchfab.com/models/163af8fd340c4b68b50f0bbe5317af97/embed",
        "boiling": "1342",
        "melting": "180.5",
        "heat_capacity": "3.58",
        "conductivity": "<span class='good'>✅ Good conductor</span>",
        "group": "Alkali Metal (Group 1)",
        "protons": "3",
        "neutrons": "4",
        "electrons": "3",
        "nuclear_symbol": "Li",
        "atomic_number": "3",
        "e_waste": "⚠️ Can leak toxic electrolytes, high water usage in mining."
    },
    "Lead (Pb)": {
        "formula": "Pb + PbO2 + 2H2SO4 → 2PbSO4 + 2H2O",
        "model": "https://sketchfab.com/models/9e44979216c748beb9abe9536f7fdbbd/embed",
        "boiling": "1749",
        "melting": "327.5",
        "heat_capacity": "0.13",
        "conductivity": "<span class='bad'>⚠️ Poor conductor</span>",
        "group": "Post-Transition Metal (Group 14)",
        "protons": "82",
        "neutrons": "125",
        "electrons": "82",
        "nuclear_symbol": "Pb",
        "atomic_number": "82",
        "e_waste": "☣️ Highly toxic, unsafe recycling pollutes soil & water."
    }
}

# --- Page 1: Atomic Model ---
if page == "⚛️ Atomic Model":
    st.title(f"⚛️ Atomic Model of {element}")
    st.markdown(f"Discharge formula: `{element_data[element]['formula']}`")
    st.components.v1.iframe(element_data[element]["model"], height=500)

# --- Page 2: Physical Properties ---
elif page == "📊 Physical Properties":
    st.title(f"📊 Physical Properties of {element}")

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
        element: [
            element_data[element]["boiling"],
            element_data[element]["melting"],
            element_data[element]["heat_capacity"],
            element_data[element]["conductivity"],
            element_data[element]["group"],
            element_data[element]["protons"],
            element_data[element]["neutrons"],
            element_data[element]["electrons"]
        ]
    }

    df = pd.DataFrame(data)
    st.markdown(df.to_html(index=False, escape=False, classes="styled-table"), unsafe_allow_html=True)

# --- Page 3: Nuclear & E-Waste ---
elif page == "☢️ Nuclear Info & E-Waste":
    st.title(f"☢️ Nuclear Info & E-Waste Effects of {element}")

    st.subheader("🧪 Nuclear Information")
    st.markdown(f"- Symbol: **{element_data[element]['nuclear_symbol']}**\n"
                f"- Atomic Number: **{element_data[element]['atomic_number']}**")

    st.subheader("♻️ Effects of Electronic Waste")
    st.markdown(f"- {element_data[element]['e_waste']}")
    st.success("✅ Always recycle batteries responsibly!")
