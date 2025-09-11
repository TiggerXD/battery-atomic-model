import streamlit as st

# ---------------- CONFIG ----------------
st.set_page_config(page_title="Battery Elements Explorer", layout="wide")

# ---------------- CSS ----------------
st.markdown("""
<style>
body {
    background-color: #f5f7fa;
    color: #222;
    font-family: 'Segoe UI', sans-serif;
}
.main-title {
    font-size: 40px;
    font-weight: bold;
    color: #0d6efd;
    text-align: center;
    padding: 20px;
}
.section-title {
    font-size: 28px;
    color: #198754;
    margin-top: 30px;
}
.highlight-li {
    background-color: #d1e7dd;
    padding: 5px 10px;
    border-radius: 8px;
    font-weight: bold;
    color: #0f5132;
}
.highlight-pb {
    background-color: #cfe2ff;
    padding: 5px 10px;
    border-radius: 8px;
    font-weight: bold;
    color: #084298;
}
/* Sidebar fix */
section[data-testid="stSidebar"] {
    background-color: #e9ecef !important;
    color: #212529 !important;
}
section[data-testid="stSidebar"] * {
    color: #212529 !important;
    font-weight: 500;
}
</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
st.sidebar.title("🔬 Navigation")
page = st.sidebar.radio("Go to:", ["🏠 Home", "📊 Physical Properties", "☢️ Nuclear & E-Waste Effects"])
atom_choice = st.sidebar.selectbox("⚛️ Select an element:", ["Lithium (Li)", "Lead (Pb)"])

# ---------------- ELEMENT DATA ----------------
element_data = {
    "Lithium (Li)": {
        "atomic_number": 3,
        "category": "Alkali Metal",
        "formula": "LiC₆ + CoO₂ → C₆ + LiCoO₂",
        "boiling_point": 1342,
        "melting_point": 180.5,
        "thermal_conductivity": 84.8,
        "electrical_conductivity": 10.6,
        "periodic_position": "Group 1 (Alkali Metal)",
        "protons": 3,
        "neutrons": 4,
        "electrons": 3,
        "gif": "lithium.gif"
    },
    "Lead (Pb)": {
        "atomic_number": 82,
        "category": "Post-Transition Metal",
        "formula": "Pb + PbO₂ + 2H₂SO₄ → 2PbSO₄ + 2H₂O",
        "boiling_point": 1749,
        "melting_point": 327.5,
        "thermal_conductivity": 35.3,
        "electrical_conductivity": 4.8,
        "periodic_position": "Group 14 (Post-Transition Metal)",
        "protons": 82,
        "neutrons": 125,
        "electrons": 82,
        "gif": "lead.gif"
    }
}

# ---------------- PAGE 1: HOME ----------------
if page == "🏠 Home":
    st.markdown('<div class="main-title">⚡ Atomic Models of Battery Elements ⚡</div>', unsafe_allow_html=True)

    st.write(
        """
        Welcome to the **Battery Elements Explorer**! 🚀  
        Learn about the atomic structures of Lithium and Lead, key players in modern battery technology.  
        """
    )

    st.markdown(f"### 🔹 {atom_choice}")

    # Show GIF
    st.image(element_data[atom_choice]["gif"], use_container_width=True)
    
    formula_class = "highlight-li" if atom_choice == "Lithium (Li)" else "highlight-pb"
    st.markdown(f"**Chemical Formula:** <span class='{formula_class}'>{element_data[atom_choice]['formula']}</span>", unsafe_allow_html=True)

    st.write(
        f"""
        - **Atomic Number:** {element_data[atom_choice]['atomic_number']}  
        - **Category:** {element_data[atom_choice]['category']}  
        - This atomic model helps you visualize the **protons**, **neutrons**, and **electrons** in the nucleus and shells.
        """
    )

# ---------------- PAGE 2: PHYSICAL PROPERTIES ----------------
elif page == "📊 Physical Properties":
    st.markdown('<div class="main-title">📊 Physical Properties Comparison</div>', unsafe_allow_html=True)

    st.write(
        """
        Physical properties of battery elements dictate their behavior in chemical reactions and battery performance.  
        """
    )

    st.table({
        "Property": [
            "🌡️ Boiling Point (°C)", 
            "🔥 Melting Point (°C)", 
            "♨️ Thermal Conductivity (W/m·K)", 
            "⚡ Electrical Conductivity (10^6 S/m)", 
            "📍 Periodic Table Position", 
            "🔵 Protons", 
            "🔴 Neutrons", 
            "🟡 Electrons",
            "💡 Battery Formula"
        ],
        "Lithium (Li)": [
            element_data["Lithium (Li)"]["boiling_point"],
            element_data["Lithium (Li)"]["melting_point"],
            element_data["Lithium (Li)"]["thermal_conductivity"],
            element_data["Lithium (Li)"]["electrical_conductivity"],
            element_data["Lithium (Li)"]["periodic_position"],
            element_data["Lithium (Li)"]["protons"],
            element_data["Lithium (Li)"]["neutrons"],
            element_data["Lithium (Li)"]["electrons"],
            element_data["Lithium (Li)"]["formula"]
        ],
        "Lead (Pb)": [
            element_data["Lead (Pb)"]["boiling_point"],
            element_data["Lead (Pb)"]["melting_point"],
            element_data["Lead (Pb)"]["thermal_conductivity"],
            element_data["Lead (Pb)"]["electrical_conductivity"],
            element_data["Lead (Pb)"]["periodic_position"],
            element_data["Lead (Pb)"]["protons"],
            element_data["Lead (Pb)"]["neutrons"],
            element_data["Lead (Pb)"]["electrons"],
            element_data["Lead (Pb)"]["formula"]
        ]
    })

# ---------------- PAGE 3: NUCLEAR & E-WASTE ----------------
elif page == "☢️ Nuclear & E-Waste Effects":
    st.markdown('<div class="main-title">☢️ Nuclear & Environmental Impact</div>', unsafe_allow_html=True)

    st.subheader("⚛️ Nuclear Symbols")
    lithium_formula = f"<span class='highlight-li'>⁷₃Li</span>"
    lead_formula = f"<span class='highlight-pb'>²⁰⁷₈₂Pb</span>"
    st.markdown(
        f"""
        Elements have **nuclear symbols** indicating the number of **protons** and **nucleons**:  
        - Lithium → {lithium_formula}  
        - Lead → {lead_formula}  
        """, unsafe_allow_html=True
    )

    st.subheader("🗑️ Effects of Electronic Waste")
    st.write(
        f"""
        Improper disposal of batteries has serious consequences:  

        - 🔹 **Lithium-ion batteries**: Can overheat or explode 🔥. Formula: **{element_data['Lithium (Li)']['formula']}**  
        - 🔸 **Lead-acid batteries**: Toxic lead and sulfuric acid leak ☣️. Formula: **{element_data['Lead (Pb)']['formula']}**  

        **Recycling Benefits:**  
        - Recovers valuable metals ♻️  
        - Prevents environmental contamination 🌍  
        - Reduces mining impact ⛏️  
        """
    )
