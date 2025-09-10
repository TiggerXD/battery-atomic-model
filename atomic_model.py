import streamlit as st
import pandas as pd

st.set_page_config(page_title="Battery Elements App", page_icon="🔋", layout="wide")

# --- Element data ---
elements = {
    "Lithium (Li)": {
        "image": "https://media.istockphoto.com/id/1408665962/vector/li-lithium-element-information-facts-properties-trends-uses-and-comparison-periodic-table-of.jpg?s=612x612&w=0&k=20&c=t00YetZ1kzBd3urTszAhZEG55GWWsZU77qbzH0J6i4I=",
        "formula": "LiC6 + CoO2 → C6 + LiCoO2",
        "physical": {
            "🌡️ Boiling Point": ("1342 °C", "Temperature at which lithium changes from liquid to gas."),
            "🌡️ Melting Point": ("180.5 °C", "Temperature at which lithium changes from solid to liquid."),
            "🔥 Heat Capacity": ("3.58 J/g·K", "Amount of heat required to raise 1 gram of lithium by 1°C."),
            "⚡ Electrical Conductivity": ("High", "Ability to conduct electric current."),
            "🧪 Periodic Table Type": ("Alkali Metal", "Lithium is a soft, highly reactive metal in group 1."),
            "🧬 Protons": (3, "Number of positively charged particles in the nucleus."),
            "🧬 Neutrons": (4, "Number of neutral particles in the nucleus."),
            "🧬 Electrons": (3, "Number of negatively charged particles surrounding the nucleus.")
        },
        "nuclear": {
            "🧪 Symbol": ("⁷Li", "The nuclear symbol shows the element and its mass number."),
            "🔢 Atomic Number": (3, "Number of protons in the nucleus, defines the element."),
            "⚖️ Mass Number": (7, "Total number of protons and neutrons."),
            "🗑️ E-waste Effects": ("Lithium batteries can release toxic chemicals if disposed improperly, polluting soil and water.", "Environmental and health impact of discarded lithium batteries.")
        }
    },
    "Lead (Pb)": {
        "image": "https://previews.123rf.com/images/samjore/samjore2207/samjore220700179/188841650-pb-lead-element-information-facts-properties-trends-uses-and-comparison-periodic-table-of-the.jpg",
        "formula": "Pb + PbO₂ + 2H₂SO₄ → 2PbSO₄ + 2H₂O",
        "physical": {
            "🌡️ Boiling Point": ("1749 °C", "Temperature at which lead changes from liquid to gas."),
            "🌡️ Melting Point": ("327.5 °C", "Temperature at which lead changes from solid to liquid."),
            "🔥 Heat Capacity": ("0.128 J/g·K", "Amount of heat required to raise 1 gram of lead by 1°C."),
            "⚡ Electrical Conductivity": ("Moderate", "Ability to conduct electric current."),
            "🧪 Periodic Table Type": ("Post-transition Metal", "Lead is a heavy metal found in group 14."),
            "🧬 Protons": (82, "Number of positively charged particles in the nucleus."),
            "🧬 Neutrons": (125, "Number of neutral particles in the nucleus."),
            "🧬 Electrons": (82, "Number of negatively charged particles surrounding the nucleus.")
        },
        "nuclear": {
            "🧪 Symbol": ("²⁰⁶Pb", "The nuclear symbol shows the element and its mass number."),
            "🔢 Atomic Number": (82, "Number of protons in the nucleus, defines the element."),
            "⚖️ Mass Number": (206, "Total number of protons and neutrons."),
            "🗑️ E-waste Effects": ("Lead-acid batteries can release lead into soil and water, causing toxicity to humans and animals.", "Environmental and health impact of discarded lead batteries.")
        }
    }
}

# --- Sidebar ---
st.sidebar.title("📚 Pages")
page = st.sidebar.selectbox("Select a Page:", ["🧪 Atomic Model & Reaction", "📊 Physical Properties", "⚛️ Nuclear Info & E-waste"])
element_name = st.sidebar.selectbox("Select Element:", list(elements.keys()))
element = elements[element_name]

# --- Page 1: Atomic Model & Reaction ---
if page.startswith("🧪"):
    st.subheader("Atomic Model & Chemical Reaction")
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image(element["image"], caption=element_name, use_container_width=True)
    with col2:
        st.markdown(f"**Chemical Formula (During Discharge):** {element['formula']}")
        st.subheader("Battery Chemistry Explanation")
        if element_name == "Lithium (Li)":
            st.write("""
            Lithium-ion batteries work by moving **Li⁺ ions** between the anode and cathode.
            During discharge, lithium ions leave the anode (graphite, C6) and intercalate into the cathode (CoO2),
            releasing energy according to the formula above.
            """)
        elif element_name == "Lead (Pb)":
            st.write("""
            Lead-acid batteries use Pb and PbO₂ electrodes with sulfuric acid.
            During discharge, lead and lead dioxide react with H₂SO₄ to produce PbSO₄ and water,
            releasing electrical energy.
            """)

# --- Page 2: Physical Properties as a Table ---
elif page.startswith("📊"):
    st.subheader(f"Physical Properties of {element_name}")
    table_data = []
    for prop, (value, description) in element["physical"].items():
        table_data.append({"Property": prop, "Value": value, "Description": description})
    df = pd.DataFrame(table_data)
    st.table(df)

# --- Page 3: Nuclear Info & E-waste as Table ---
elif page.startswith("⚛️"):
    st.subheader(f"Nuclear Information & E-waste Effects of {element_name}")
    table_data = []
    for key, (value, description) in element["nuclear"].items():
        table_data.append({"Property": key, "Value": value, "Description": description})
    df = pd.DataFrame(table_data)
    st.table(df)
