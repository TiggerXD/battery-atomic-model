import streamlit as st
import pandas as pd

# --- Page Config ---
st.set_page_config(page_title="Battery Elements Explorer", layout="wide")
st.markdown("<h1 style='text-align:center;color:#00ffff'>🔬 Battery Elements Explorer</h1>", unsafe_allow_html=True)

# --- Sidebar ---
st.sidebar.title("⚡ Explore Elements")
element = st.sidebar.selectbox("Select Element", ["Lithium (Li)", "Lead (Pb)"])
page = st.sidebar.radio("Navigate", ["🧪 Atomic Model", "📊 Physical Properties", "☢️ Nuclear & E-Waste"])

# --- Element Data ---
element_data = {
    "Lithium (Li)": {
        "formula": "LiC6 + CoO2 → C6 + LiCoO2",
        "protons": 3,
        "neutrons": 4,
        "electrons": [2,1],
        "boiling": "1342°C",
        "melting": "180.5°C",
        "heat_capacity": "3.58 J/g·K",
        "conductivity": "✅ Good conductor",
        "group": "Alkali Metal (Group 1)",
        "nuclear_symbol": "Li",
        "atomic_number": 3,
        "e_waste": "⚠️ Can leak toxic electrolytes; lithium mining consumes high water resources.",
        "description": "Lithium is a soft, silvery metal used widely in rechargeable batteries. It's highly reactive and light, making it ideal for portable electronics.",
        "embed": '<iframe src="https://phet.colorado.edu/sims/html/build-an-atom/latest/build-an-atom_en.html" width="800" height="600" scrolling="no" allowfullscreen></iframe>'
    },
    "Lead (Pb)": {
        "formula": "Pb + PbO2 + 2H2SO4 → 2PbSO4 + 2H2O",
        "protons": 82,
        "neutrons": 125,
        "electrons": [2,8,18,32,18,4],
        "boiling": "1749°C",
        "melting": "327.5°C",
        "heat_capacity": "0.13 J/g·K",
        "conductivity": "⚠️ Poor conductor",
        "group": "Post-Transition Metal (Group 14)",
        "nuclear_symbol": "Pb",
        "atomic_number": 82,
        "e_waste": "☣️ Highly toxic; lead from batteries can contaminate soil and water if not recycled properly.",
        "description": "Lead is a heavy metal with low melting point, used mainly in lead-acid batteries. It is toxic but recyclable.",
        "embed": '<iframe src="https://phet.colorado.edu/sims/html/build-an-atom/latest/build-an-atom_en.html" width="800" height="600" scrolling="no" allowfullscreen></iframe>'
    }
}

data = element_data[element]

# --- Page 1: Atomic Model ---
if page == "🧪 Atomic Model":
    st.markdown(f"<h2 style='color:#00ff00'>🧪 Atomic Model of {element}</h2>", unsafe_allow_html=True)
    st.markdown(f"<b style='color:#ffff00'>Discharge Formula:</b> <span style='color:#ffffff'>{data['formula']}</span>", unsafe_allow_html=True)
    st.markdown(f"<p style='color:#ffffff'>{data['description']}</p>", unsafe_allow_html=True)

    # Embed interactive simulation
    st.components.v1.html(data['embed'], height=650, scrolling=True)

# --- Page 2: Physical Properties ---
elif page == "📊 Physical Properties":
    st.markdown(f"<h2 style='color:#00ff00'>📊 Physical Properties of {element}</h2>", unsafe_allow_html=True)
    properties = {
        "Property": ["Boiling Point", "Melting Point", "Heat Capacity", "Electrical Conductivity",
                     "Periodic Table Group", "Protons", "Neutrons", "Electrons"],
        "Value": [data['boiling'], data['melting'], data['heat_capacity'], data['conductivity'],
                  data['group'], data['protons'], data['neutrons'], sum(data['electrons'])]
    }
    df = pd.DataFrame(properties)
    st.dataframe(df.style.set_properties(**{'background-color':'#222222','color':'#00ffff','font-weight':'bold'})
                 .applymap(lambda v: 'color: #ffff00' if isinstance(v,str) and any(x in v for x in ['Boiling','Melting','Electrical','Protons','Neutrons','Electrons']) else ''))

    st.markdown(f"<p style='color:#ffffff'>{data['description']}</p>", unsafe_allow_html=True)

# --- Page 3: Nuclear & E-Waste ---
elif page == "☢️ Nuclear & E-Waste":
    st.markdown(f"<h2 style='color:#00ff00'>☢️ Nuclear & Environmental Impact of {element}</h2>", unsafe_allow_html=True)
    st.markdown(f"<b style='color:#ffff00'>Symbol:</b> <span style='color:#ffffff'>{data['nuclear_symbol']}</span>", unsafe_allow_html=True)
    st.markdown(f"<b style='color:#ffff00'>Atomic Number:</b> <span style='color:#ffffff'>{data['atomic_number']}</span>", unsafe_allow_html=True)
    st.markdown(f"<b style='color:#ff3333'>E-Waste Effect:</b> <span style='color:#ffffff'>{data['e_waste']}</span>", unsafe_allow_html=True)
    st.success("✅ Always recycle batteries responsibly!")
