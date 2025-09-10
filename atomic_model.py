import streamlit as st

# --- Element data ---
elements = {
    "Lithium (Li)": {
        "image": "https://media.istockphoto.com/id/1408665962/vector/li-lithium-element-information-facts-properties-trends-uses-and-comparison-periodic-table-of.jpg?s=612x612&w=0&k=20&c=t00YetZ1kzBd3urTszAhZEG55GWWsZU77qbzH0J6i4I=",
        "formula": "LiC6 + CoO2 → C6 + LiCoO2"
    },
    "Lead (Pb)": {
        "image": "https://previews.123rf.com/images/samjore/samjore2207/samjore220700179/188841650-pb-lead-element-information-facts-properties-trends-uses-and-comparison-periodic-table-of-the.jpg",
        "formula": "Pb + PbO₂ + 2H₂SO₄ → 2PbSO₄ + 2H₂O"
    }
}

# --- Streamlit UI ---
st.title("Battery Project: Atomic Models of Lithium and Lead")
st.write("Created by: Your Group Name")

element_name = st.selectbox("Select Element:", list(elements.keys()))
element = elements[element_name]

# --- Show chemical formula ---
st.subheader("Chemical Formula (During Discharge)")
st.write(element["formula"])

# --- Show image ---
st.image(element["image"], caption=element_name, use_column_width=True)

# --- Chemical reaction explanation ---
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

st.write("Both Lithium and Lead are important in battery technology, though in different types of batteries (Lithium-ion vs Lead-acid).")
