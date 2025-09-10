import streamlit as st

# --- Element data ---
elements = {
    "Lithium (Li)": {
        "image": "https://media.istockphoto.com/id/1408665962/vector/li-lithium-element-information-facts-properties-trends-uses-and-comparison-periodic-table-of.jpg?s=612x612&w=0&k=20&c=t00YetZ1kzBd3urTszAhZEG55GWWsZU77qbzH0J6i4I=",
        "formula": "LiC6 + CoO2 → C6 + LiCoO2",
        "physical": {
            "Density": "0.534 g/cm³",
            "Melting Point": "180.5 °C",
            "Boiling Point": "1342 °C",
            "Conductivity": "High"
        },
        "nuclear": {
            "Symbol": "⁷Li",
            "Atomic Number": 3,
            "Mass Number": 7,
            "E-waste effects": "Lithium batteries can cause soil and water pollution if disposed improperly, releasing toxic chemicals and metals."
        }
    },
    "Lead (Pb)": {
        "image": "https://previews.123rf.com/images/samjore/samjore2207/samjore220700179/188841650-pb-lead-element-information-facts-properties-trends-uses-and-comparison-periodic-table-of-the.jpg",
        "formula": "Pb + PbO₂ + 2H₂SO₄ → 2PbSO₄ + 2H₂O",
        "physical": {
            "Density": "11.34 g/cm³",
            "Melting Point": "327.5 °C",
            "Boiling Point": "1749 °C",
            "Conductivity": "Moderate"
        },
        "nuclear": {
            "Symbol": "²⁰⁶Pb",
            "Atomic Number": 82,
            "Mass Number": 206,
            "E-waste effects": "Lead-acid batteries can release lead into soil and water, causing toxicity to humans, animals, and plants if not recycled properly."
        }
    }
}

# --- Page selector ---
st.title("Battery Project: Lithium and Lead")
page = st.sidebar.radio("Select Page:", ["Atomic Model & Reaction", "Physical Properties", "Nuclear Info & E-waste"])

# --- Dropdown to select element ---
element_name = st.selectbox("Select Element:", list(elements.keys()))
element = elements[element_name]

# --- Page 1: Atomic Model & Reaction ---
if page == "Atomic Model & Reaction":
    st.subheader("Atomic Model & Chemical Reaction")
    st.write("**Chemical Formula (During Discharge):**")
    st.write(element["formula"])
    st.image(element["image"], caption=element_name, use_container_width=True)
    
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
        
# --- Page 2: Physical Properties ---
elif page == "Physical Properties":
    st.subheader(f"Physical Properties of {element_name}")
    for prop, value in element["physical"].items():
        st.write(f"**{prop}:** {value}")

# --- Page 3: Nuclear Info & E-waste ---
elif page == "Nuclear Info & E-waste":
    st.subheader(f"Nuclear Information of {element_name}")
    for key, value in element["nuclear"].items():
        st.write(f"**{key}:** {value}")
