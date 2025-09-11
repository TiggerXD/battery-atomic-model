import streamlit as st
import plotly.graph_objects as go
import numpy as np
import pandas as pd

# --- Page Config ---
st.set_page_config(page_title="Battery Elements Explorer", layout="wide")
st.title("🔬 Battery Elements Explorer")

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
        "electrons": [2, 1],
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
        "electrons": [2, 8, 18, 32, 18, 4],
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
    st.subheader(f"⚛️ 3D Animated Atomic Model of {element}")
    st.markdown(f"**Discharge Formula:** `{data['formula']}`")

    shells = data['electrons']
    radii = np.linspace(10, 30, len(shells))  # radius per shell
    n_frames = 60  # number of animation frames
    frames = []

    # --- Build animation frames ---
    angles = np.linspace(0, 2*np.pi, n_frames)
    for t in angles:
        frame_data = []
        # Nucleus
        frame_data.append(go.Scatter3d(
            x=[0]*data['protons'],
            y=[0]*data['protons'],
            z=[0]*data['protons'],
            mode='markers',
            marker=dict(size=8, color='red'),
            name='Protons'
        ))
        frame_data.append(go.Scatter3d(
            x=[0]*data['neutrons'],
            y=[0]*data['neutrons'],
            z=[0]*data['neutrons'],
            mode='markers',
            marker=dict(size=8, color='blue'),
            name='Neutrons'
        ))
        # Electrons
        for i, num in enumerate(shells):
            x = []
            y = []
            z = []
            tilt = np.pi/8*(i+1)  # tilt per shell for 3D effect
            for j in range(num):
                angle = t + j*2*np.pi/num
                x.append(radii[i]*np.cos(angle))
                y.append(radii[i]*np.sin(angle)*np.cos(tilt))
                z.append(radii[i]*np.sin(angle)*np.sin(tilt))
            frame_data.append(go.Scatter3d(
                x=x, y=y, z=z,
                mode='markers',
                marker=dict(size=4, color='yellow'),
                name=f'Shell {i+1}'
            ))
        frames.append(go.Frame(data=frame_data))

    fig = go.Figure(
        data=frames[0].data,
        frames=frames
    )

    fig.update_layout(
        updatemenus=[dict(
            type="buttons",
            buttons=[dict(label="Play",
                          method="animate",
                          args=[None, {"frame": {"duration": 80, "redraw": True},
                                       "fromcurrent": True, "transition": {"duration": 0}}])],
            showactive=True
        )],
        scene=dict(
            xaxis=dict(showbackground=False, visible=False),
            yaxis=dict(showbackground=False, visible=False),
            zaxis=dict(showbackground=False, visible=False)
        ),
        margin=dict(l=0, r=0, t=0, b=0)
    )

    st.plotly_chart(fig, use_container_width=True)

# --- Page 2: Physical Properties ---
elif page == "📊 Physical Properties":
    st.subheader(f"📊 Physical Properties of {element}")
    properties = {
        "Property": ["Boiling Point", "Melting Point", "Heat Capacity", "Electrical Conductivity",
                     "Periodic Table Group", "Protons", "Neutrons", "Electrons"],
        element: [data['boiling'], data['melting'], data['heat_capacity'], data['conductivity'],
                  data['group'], data['protons'], data['neutrons'], sum(shells)]
    }
    df = pd.DataFrame(properties)
    st.table(df)

# --- Page 3: Nuclear & E-Waste ---
elif page == "☢️ Nuclear & E-Waste":
    st.subheader(f"☢️ Nuclear Info & Environmental Impact of {element}")
    st.markdown(f"- **Symbol:** {data['nuclear_symbol']}")
    st.markdown(f"- **Atomic Number:** {data['atomic_number']}")
    st.markdown(f"- **E-Waste Effect:** {data['e_waste']}")
    st.success("✅ Always recycle batteries responsibly!")
