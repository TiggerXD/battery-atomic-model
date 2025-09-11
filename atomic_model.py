import streamlit as st
import pandas as pd

# --- Page Setup ---
st.set_page_config(page_title="Battery Elements App", page_icon="🔋", layout="wide")

# --- Custom CSS for styling ---
st.markdown("""
    <style>
        /* Sidebar banner */
        [data-testid="stSidebar"] > div:first-child {
            background: linear-gradient(135deg, #1E3C72, #2A5298);
            padding: 20px;
            border-radius: 10px;
        }
        [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3 {
            color: white !important;
            text-align: center;
        }
        /* Table styling */
        table {
            border-collapse: collapse;
            width: 100%;
        }
        th, td {
            text-align: left;
            padding: 8px;
        }
        tr:nth-child(even) {background-color: #f2f2f2;}
        th {
            background-color: #2A5298;
            color: white;
        }
        /* Info box style */
        .infobox {
            padding: 15px;
            border-radius: 10px;
            margin: 10px 0;
            font-size: 16px;
        }
        .good {background-color: #d4edda; color: #155724;}
        .warn {background-color: #fff3cd; color: #856404;}
        .bad {background-color: #f8d7da; color: #721c24;}
    </style>
""", unsafe_allow_html=True)

# --- Element data ---
elements = {
    "Lithium (Li)": {
        "image": "https://media.istockphoto.com/id/1408665962/vector/li-lithium-element-information-facts-properties-trends-uses-and-comparison-periodic-table-of.jpg?s=612x612&w=0&k=20&c=t00YetZ1kzBd3urTszAhZEG55GWWsZU77qbzH0J6i4I=",
        "formula": "LiC6 + CoO2 → C6 + LiCoO2",
        "physical": {
            "🌡️ Boiling Point": ("1342 °C", "Temperature at which lithium changes from liquid to gas."),
            "🌡️ Melting Point": ("180.5 °C", "Temperature at which lithium changes from solid to liquid."),
            "🔥 Heat Capacity": ("3.58 J/g·K", "Heat required to raise 1g by 1°C."),
            "⚡ Electrical Conductivity": ("High", "Ability to conduct current."),
            "🧪 Periodic Table Type": ("Alkali Metal", "Soft, highly reactive Group 1 metal."),
            "🧬 Protons": (3, "Positive charges in nucleus."),
            "🧬 Neutrons": (4, "Neutral particles in nucleus."),
            "🧬 Electrons": (3, "Negative charges orbiting nucleus.")
        },
        "nuclear": {
            "🧪 Symbol": ("⁷Li", "Nuclear symbol with mass number."),
            "🔢 Atomic Number": (3, "Defines the element."),
            "⚖️ Mass Number": (7, "Protons + Neutrons."),
            "🗑️ E-waste Effects": ("Lithium batteries can release toxic chemicals if discarded poorly.", "Environmental hazard.")
        }
    },
    "Lead (Pb)": {
        "image": "https://previews.123rf.com/images/samjore/samjore2207/samjore220700179/188841650-pb-lead-element-information-facts-properties-trends-uses-and-comparison-periodic-table-of-the.jpg",
        "formula": "Pb + PbO₂ + 2H₂SO₄ → 2PbSO₄ + 2H₂O",
        "physical": {
            "🌡️ Boiling Point": ("1749 °C", "Temperature at which lead changes from liquid to gas."),
            "🌡️ Melting Point": ("327.5 °C", "Temperature at which lead changes from solid to liquid."),
            "🔥 Heat Capacity": ("0.128 J/g·K", "Heat required to raise 1g by 1°C."),
            "⚡ Electrical Conductivity": ("Moderate", "Ability to conduct current."),
            "🧪 Periodic Table Type": ("Post-transition Metal", "Heavy metal in Group 14."),
            "🧬 Protons": (82, "Positive charges in nucleus."),
            "🧬 Neutrons": (125, "Neutral particles in nucleus."),
            "🧬 Electrons": (82, "Negative charges orbiting nucleus.")
        },
        "nuclear": {
            "🧪 Symbol": ("²⁰⁶Pb", "Nuclear symbol with mass number."),
            "🔢 Atomic Number": (82, "Defines the element."),
            "⚖️ Mass Number": (206, "Protons + Neutrons."),
            "🗑️ E-waste Effects": ("Lead-acid batteries can leak lead, causing soil and water toxicity.", "Health & environment hazard.")
        }
    }
}

# --- Sidebar ---
st.sidebar.title("🔋 Battery Elements Explorer")
page = st.sidebar.selectbox("📚 Choose a Page:", ["🧪 Atomic Model & Reaction", "📊 Physical Properties", "⚛️ Nuclear Info & E-waste"])
element_name = st.sidebar.selectbox("🔎 Select Element:", list(elements.keys()))
element = elements[element_name]

# --- Page 1 ---
if page.startswith("🧪"):
    st.markdown("## 🧪 Atomic Model & Chemical Reaction")
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image(element["image"], caption=element_name, use_container_width=True)
    with col2:
        st.markdown(f"<div class='infobox good'><b>Chemical Formula (Discharge):</b> {element['formula']}</div>", unsafe_allow_html=True)
        if element_name.startswith("Lithium"):
            st.markdown("<div class='infobox warn'>Lithium-ion batteries move Li⁺ ions between anode and cathode. During discharge, ions shift from graphite (C6) to cobalt oxide (CoO₂).</div>", unsafe_allow_html=True)
        else:
            st.markdown("<div class='infobox warn'>Lead-acid batteries use Pb/PbO₂ electrodes with H₂SO₄. During discharge, they form PbSO₄ and water, releasing energy.</div>", unsafe_allow_html=True)

# --- Page 2 ---
elif page.startswith("📊"):
    st.markdown(f"## 📊 Physical Properties of {element_name}")
    table_data = []
    for prop, (value, description) in element["physical"].items():
        table_data.append({"Property": prop, "Value": value, "Description": description})
    df = pd.DataFrame(table_data)
    st.table(df)

# --- Page 3 ---
elif page.startswith("⚛️"):
    st.markdown(f"## ⚛️ Nuclear Info & E-waste for {element_name}")
    table_data = []
    for key, (value, description) in element["nuclear"].items():
        table_data.append({"Property": key, "Value": value, "Description": description})
    df = pd.DataFrame(table_data)
    st.table(df)
    st.markdown("<div class='infobox bad'>⚠️ Improper disposal of these batteries can cause serious environmental and health risks!</div>", unsafe_allow_html=True)
