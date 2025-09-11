import streamlit as st
import plotly.graph_objects as go
import numpy as np
import pandas as pd

# --- Page Config ---
st.set_page_config(page_title="Battery Elements Explorer", layout="wide")
st.markdown("<h1 style='text-align:center;color:#00ffff'>🔬 Battery Elements Explorer</h1>", unsafe_allow_html=True)

# --- Sidebar ---
st.sidebar.title("⚡ Explore Elements")
element = st.sidebar.selectbox("Select Element", ["Lithium (Li)", "Lead (Pb)"])
page = st.sidebar.radio("Navigate", ["⚛️ Atomic Model", "📊 Physical Properties", "☢️ Nuclear & E-Waste"])

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
        "e_waste": "⚠️ Can leak toxic electrolytes, high water usage in mining."
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
        "e_waste": "☣️ Highly toxic, unsafe recycling pollutes soil & water."
    }
}
data = element_data[element]

# --- Page 1: Atomic Model ---
if page == "⚛️ Atomic Model":
    st.markdown(f"<h2 style='color:#00ff00'>⚛️ Atomic Model of {element}</h2>", unsafe_allow_html=True)
    st.markdown(f"<b style='color:#ffff00'>Discharge Formula:</b> <span style='color:#ffffff'>{data['formula']}</span>", unsafe_allow_html=True)

    shells = data['electrons']
    radii = np.linspace(15, 40, len(shells))  # bigger radii for orbits
    n_frames = 60
    frames = []

    # Nucleus positions
    proton_positions = np.random.uniform(-2,2,(data['protons'],3))

    # Neutrons stick to random protons
    neutron_positions = np.zeros((data['neutrons'],3))
    for i in range(data['neutrons']):
        p_idx = np.random.randint(0, data['protons'])
        neutron_positions[i] = proton_positions[p_idx] + np.random.uniform(-0.5,0.5,3)

    angles = np.linspace(0, 2*np.pi, n_frames)
    for t in angles:
        frame_data = []

        # Protons
        frame_data.append(go.Scatter3d(
            x=proton_positions[:,0],
            y=proton_positions[:,1],
            z=proton_positions[:,2],
            mode='markers',
            marker=dict(size=12,color='red',opacity=0.9),
            name='Protons'
        ))

        # Neutrons
        frame_data.append(go.Scatter3d(
            x=neutron_positions[:,0],
            y=neutron_positions[:,1],
            z=neutron_positions[:,2],
            mode='markers',
            marker=dict(size=12,color='pink',opacity=0.9),
            name='Neutrons'
        ))

        # Electrons
        for i, num in enumerate(shells):
            x, y, z = [], [], []
            tilt = np.pi/8*(i+1)
            for j in range(num):
                angle = t + j*2*np.pi/num
                x.append(radii[i]*np.cos(angle))
                y.append(radii[i]*np.sin(angle)*np.cos(tilt))
                z.append(radii[i]*np.sin(angle)*np.sin(tilt))
            frame_data.append(go.Scatter3d(
                x=x, y=y, z=z,
                mode='markers+lines',
                line=dict(color='yellow', width=2, dash='dot'),
                marker=dict(size=7,color='yellow',opacity=0.9),
                name=f'Shell {i+1}'
            ))
        frames.append(go.Frame(data=frame_data))

    fig = go.Figure(data=frames[0].data, frames=frames)
    fig.update_layout(
        paper_bgcolor="#111111",
        plot_bgcolor="#111111",
        font_color="#00ffff",
        updatemenus=[dict(
            type="buttons",
            buttons=[dict(label="Play",
                          method="animate",
                          args=[None, {"frame":{"duration":80,"redraw":True},
                                       "fromcurrent":True, "transition":{"duration":0}}])],
            showactive=True
        )],
        scene=dict(
            xaxis=dict(showbackground=False, visible=False),
            yaxis=dict(showbackground=False, visible=False),
            zaxis=dict(showbackground=False, visible=False),
            bgcolor="#111111"
        ),
        margin=dict(l=0,r=0,t=0,b=0)
    )
    st.plotly_chart(fig, use_container_width=True)

# --- Page 2: Physical Properties ---
elif page == "📊 Physical Properties":
    st.markdown(f"<h2 style='color:#00ff00'>📊 Physical Properties of {element}</h2>", unsafe_allow_html=True)
    properties = {
        "Property": ["Boiling Point", "Melting Point", "Heat Capacity", "Electrical Conductivity",
                     "Periodic Table Group", "Protons", "Neutrons", "Electrons"],
        element: [data['boiling'], data['melting'], data['heat_capacity'], data['conductivity'],
                  data['group'], data['protons'], data['neutrons'], sum(shells)]
    }
    df = pd.DataFrame(properties)
    def highlight_props(x):
        important = ['Boiling Point','Melting Point','Electrical Conductivity','Protons','Neutrons','Electrons']
        return ['background-color:#444444; color:#ffff00' if v in important else 'background-color:#222222; color:#00ffff' for v in x]
    st.dataframe(df.style.apply(highlight_props, axis=0))

# --- Page 3: Nuclear & E-Waste ---
elif page == "☢️ Nuclear & E-Waste":
    st.markdown(f"<h2 style='color:#00ff00'>☢️ Nuclear Info & Environmental Impact of {element}</h2>", unsafe_allow_html=True)
    st.markdown(f"<b style='color:#ffff00'>Symbol:</b> <span style='color:#ffffff'>{data['nuclear_symbol']}</span>", unsafe_allow_html=True)
    st.markdown(f"<b style='color:#ffff00'>Atomic Number:</b> <span style='color:#ffffff'>{data['atomic_number']}</span>", unsafe_allow_html=True)
    st.markdown(f"<b style='color:#ff3333'>E-Waste Effect:</b> <span style='color:#ffffff'>{data['e_waste']}</span>", unsafe_allow_html=True)
    st.success("✅ Always recycle batteries responsibly!")
