import streamlit as st

# --- Element data ---
elements = {
    "Lithium (Li)": {
        "image": "https://media.istockphoto.com/id/1408665962/vector/li-lithium-element-information-facts-properties-trends-uses-and-comparison-periodic-table-of.jpg?s=612x612&w=0&k=20&c=t00YetZ1kzBd3urTszAhZEG55GWWsZU77qbzH0J6i4I=",
        "formula": "Li → Li⁺ + e⁻"
    },
    "Lead (Pb)": {
        "image": "https://media.istockphoto.com/id/1408665962/vector/li-lithium-element-information-facts-properties-trends-uses-and-comparison-periodic-table-of.jpg?s=612x612&w=0&k=20&c=t00YetZ1kzBd3urTszAhZEG55GWWsZU77qbzH0J6i4I=",
        "formula": "PbO₂ + Pb + 2H₂SO₄ → 2PbSO₄ + 2H₂O"
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
    Lithium is highly reactive and loses **1 electron** easily, forming **Li⁺ ions**.  
    In lithium batteries, these ions move between electrodes during charge and discharge.
    """)
elif element_name == "Lead (Pb)":
    st.write("""
    Lead is used in **lead-acid batteries**.  
    The Pb and PbO₂ electrodes react with sulfuric acid to produce electricity.  
    Lead changes oxidation states between **Pb²⁺** and **Pb⁴⁺**.
    """)

st.write("Both Lithium and Lead are important in battery technology, though in different types of batteries (Lithium-ion vs Lead-acid).")
