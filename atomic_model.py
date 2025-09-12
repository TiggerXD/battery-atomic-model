import streamlit as st

# ---------------- CONFIG ----------------
st.set_page_config(page_title="Battery Elements Explorer", layout="wide")

# ---------------- CSS ----------------
# IMPORTANT: CSS only adjusts the selectbox text color (not the whole sidebar).
st.markdown(
    """
    <style>
    /* Make the element selectbox text dark and readable (only affects combobox/select) */
    div[role="combobox"] > div > div > span {
        color: #212529 !important;
        font-weight: 600;
    }

    /* Main page styling (safe changes) */
    body {
        background-color: #f7fbfc;
        color: #111827;
        font-family: 'Segoe UI', Arial, sans-serif;
    }
    .main-title {
        font-size: 40px;
        font-weight: 700;
        color: #0b5ed7;
        text-align: center;
        padding: 14px 0;
    }
    .section-title {
        font-size: 24px;
        color: #0f5132;
        margin-top: 18px;
        margin-bottom: 6px;
    }
    .muted {
        color: #495057;
        margin-bottom: 12px;
    }
    .highlight-li {
        background-color: #d1e7dd;
        padding: 6px 10px;
        border-radius: 8px;
        font-weight: 700;
        color: #0f5132;
    }
    .highlight-pb {
        background-color: #cfe2ff;
        padding: 6px 10px;
        border-radius: 8px;
        font-weight: 700;
        color: #084298;
    }
    .gif-wrap {
        display:flex;
        justify-content:center;
        align-items:center;
        margin-top: 12px;
        margin-bottom: 12px;
    }
    .note {
        background:#fff3cd;
        padding:10px;
        border-radius:8px;
        color:#664d03;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------- SIDEBAR ----------------
st.sidebar.title("🔬 Navigation")
page = st.sidebar.radio("Go to:", ["🏠 Home", "📊 Physical Properties", "☢️ Nuclear & E-Waste"])
# element selection combobox (text color fixed by CSS above)
element_choice = st.sidebar.selectbox("⚛️ Choose element", ["Lithium (Li)", "Lead (Pb)"])

# ---------------- ELEMENT DATA ----------------
# Make sure these GIF filenames exist in the same folder as this script in your repo.
ELEMENTS = {
    "Lithium (Li)": {
        "gif": "lithium.gif",
        "atomic_number": 3,
        "category": "Alkali Metal (Group 1)",
        "formula": "LiC₆ + CoO₂ → C₆ + LiCoO₂",
        "boiling_point": "1342 °C",
        "melting_point": "180.5 °C",
        "thermal_conductivity": "84.8 W/m·K",
        "electrical_conductivity": "10.6×10⁶ S/m",
        "protons": 3,
        "neutrons": 4,
        "electrons": 3,
        "description": (
            "Lithium is a soft, silvery metal and the lightest solid element. "
            "It has high electrochemical potential and is widely used in rechargeable lithium-ion batteries "
            "for phones, laptops and electric vehicles due to its high energy density and low weight."
        ),
    },
    "Lead (Pb)": {
        "gif": "lead.gif",
        "atomic_number": 82,
        "category": "Post-Transition Metal (Group 14)",
        "formula": "Pb + PbO₂ + 2H₂SO₄ → 2PbSO₄ + 2H₂O",
        "boiling_point": "1749 °C",
        "melting_point": "327.5 °C",
        "thermal_conductivity": "35.3 W/m·K",
        "electrical_conductivity": "4.8×10⁶ S/m",
        "protons": 82,
        "neutrons": 125,
        "electrons": 82,
        "description": (
            "Lead is a heavy, malleable metal used primarily in lead-acid batteries. "
            "Lead-acid batteries are reliable and inexpensive for applications like vehicle starting and backup power, "
            "but lead is toxic and requires responsible recycling."
        ),
    },
}

# small helper
def formula_html(element_key):
    cls = "highlight-li" if "Lithium" in element_key else "highlight-pb"
    formula = ELEMENTS[element_key]["formula"]
    return f"**Chemical Formula:** <span class='{cls}'>{formula}</span>"

# ---------------- PAGE: HOME ----------------
if page == "🏠 Home":
    st.markdown('<div class="main-title">⚡ Battery Elements Explorer</div>', unsafe_allow_html=True)
    st.markdown(
        "Welcome! This mini-app explores the atomic structure and battery-relevant chemistry of **Lithium** and **Lead**. "
        "Use the sidebar to choose an element and switch pages. Below you'll find an animated model, the key reaction, "
        "and a friendly explanation of why this element matters to batteries. 🔋⚡",
        unsafe_allow_html=True,
    )

    st.markdown(f"## {element_choice}")
    st.markdown(f"<div class='muted'>{ELEMENTS[element_choice]['description']}</div>", unsafe_allow_html=True)

    # GIF display (use_container_width=True to avoid the deprecated param; caption and centered)
    st.markdown('<div class="gif-wrap">', unsafe_allow_html=True)
    try:
        st.image(ELEMENTS[element_choice]["gif"], caption=f"{element_choice} — Atom model (animated)", use_container_width=True)
    except Exception as e:
        st.error("Could not load GIF. Make sure the GIF file is in the same repository folder as this script.")
        st.write(e)
    st.markdown('</div>', unsafe_allow_html=True)

    # Highlighted formula & short explanation
    st.markdown(formula_html(element_choice), unsafe_allow_html=True)
    st.markdown(
        """
        <div class='note'>
        🔎 <strong>Quick explainer:</strong> The chemical formula shown above is the simplified reaction (discharge)
        used in the battery type that involves this element — it summarizes how atoms move between electrodes during
        charge/discharge and how energy is stored/released.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("### What you're seeing in the animation")
    st.markdown(
        "- 🟡 **Yellow dots** = electrons moving in shells (visualized for learning; real quantum orbitals are not circular).  \n"
        "- 🔵 **Blue / red** (in GIFs) represent the nucleus (protons/neutrons) clustered together.  \n"
        "- The animation helps you visualize electron shells and how valence electrons are available for reactions."
    )

# ---------------- PAGE: PHYSICAL PROPERTIES ----------------
elif page == "📊 Physical Properties":
    st.markdown('<div class="main-title">📊 Physical Properties & Why They Matter</div>', unsafe_allow_html=True)
    st.markdown(
        "Physical properties (melting point, conductivity, density, etc.) strongly influence how an element behaves in "
        "a battery. Below is a quick comparison and short explanations tying each property to battery performance."
    )

    # Build table-like presentation with explanations
    left_col, right_col = st.columns([1,1])
    with left_col:
        st.markdown("#### 🔹 Lithium (Li)")
        st.write(f"- **Atomic number:** {ELEMENTS['Lithium (Li)']['atomic_number']}")
        st.write(f"- **Category:** {ELEMENTS['Lithium (Li)']['category']}")
        st.write(f"- **Melting point:** {ELEMENTS['Lithium (Li)']['melting_point']}")
        st.write(f"- **Boiling point:** {ELEMENTS['Lithium (Li)']['boiling_point']}")
        st.write(f"- **Thermal conductivity:** {ELEMENTS['Lithium (Li)']['thermal_conductivity']}")
        st.write(f"- **Electrical conductivity:** {ELEMENTS['Lithium (Li)']['electrical_conductivity']}")
        st.markdown(formula_html("Lithium (Li)"), unsafe_allow_html=True)
        st.markdown(
            "**Why it matters:** Lithium's low atomic weight and high electrochemical potential give lithium-ion batteries high energy-per-mass, enabling compact, long-range devices."
        )

    with right_col:
        st.markdown("#### 🔸 Lead (Pb)")
        st.write(f"- **Atomic number:** {ELEMENTS['Lead (Pb)']['atomic_number']}")
        st.write(f"- **Category:** {ELEMENTS['Lead (Pb)']['category']}")
        st.write(f"- **Melting point:** {ELEMENTS['Lead (Pb)']['melting_point']}")
        st.write(f"- **Boiling point:** {ELEMENTS['Lead (Pb)']['boiling_point']}")
        st.write(f"- **Thermal conductivity:** {ELEMENTS['Lead (Pb)']['thermal_conductivity']}")
        st.write(f"- **Electrical conductivity:** {ELEMENTS['Lead (Pb)']['electrical_conductivity']}")
        st.markdown(formula_html("Lead (Pb)"), unsafe_allow_html=True)
        st.markdown(
            "**Why it matters:** Lead's density and stable chemistry make lead-acid batteries cheap and robust for heavy-duty uses (cars, backups), but the toxicity of lead is a major downside."
        )

    st.markdown("---")
    st.markdown("### Quick comparison insights")
    st.markdown(
        "- **Energy density vs. stability:** Lithium offers far higher energy density (lighter, more energy per kg), while Lead offers stability and low cost.  \n"
        "- **Safety & handling:** Lithium cells require careful thermal management; lead batteries require strict recycling to avoid contamination."
    )

# ---------------- PAGE: NUCLEAR & E-WASTE ----------------
elif page == "☢️ Nuclear & E-Waste":
    st.markdown('<div class="main-title">☢️ Nuclear Notation & E-Waste Impact</div>', unsafe_allow_html=True)
    st.markdown(
        "This page covers the nuclear notation for isotopes (how to read the small numbers) and explains the environmental "
        "consequences of battery disposal and why recycling is crucial. 🌍"
    )

    st.markdown("### Nuclear notation (quick primer)")
    st.markdown(
        "- The nuclear symbol A_ZX shows the **mass number (A)** (protons+neutrons) as a superscript and the **atomic number (Z)** (protons) as a subscript.  \n"
        "- Example isotopes: <span class='highlight-li'>⁷₃Li</span> (common lithium isotope) and <span class='highlight-pb'>²⁰⁷₈₂Pb</span> (stable lead isotope).",
        unsafe_allow_html=True,
    )

    st.markdown("### Environmental & health effects of battery waste")
    st.markdown(
        """
        - 🔹 **Lithium-ion battery issues:**  
          • Damaged lithium batteries can overheat and cause fires.  \n
          • Mining for lithium can be water-intensive and disrupt local ecosystems.  \n
          • Recycling rates for lithium batteries are improving but still need scale.

        - 🔸 **Lead-acid battery issues:**  
          • Lead is highly toxic; improper disposal contaminates soil and groundwater.  \n
          • Sulfuric acid from damaged batteries causes chemical burns and environmental harm.  \n
          • Lead is recyclable and widely recycled when collection systems work well — that recycling is essential.
        """
    )

    st.markdown("### Practical advice (for students & households)")
    st.markdown(
        "- Do not throw batteries in the regular trash.  \n"
        "- Use local battery-recycle drop-off points or community hazardous waste collection days.  \n"
        "- For damaged batteries (bulging, leaking), avoid handling them directly and contact local hazardous waste services."
    )

    st.markdown("---")
    st.markdown("**Formulas reminder:**")
    st.markdown(formula_html("Lithium (Li)"), unsafe_allow_html=True)
    st.markdown(formula_html("Lead (Pb)"), unsafe_allow_html=True)

# ---------------- END ----------------
