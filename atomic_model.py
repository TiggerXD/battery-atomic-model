import streamlit as st
import plotly.graph_objects as go
import numpy as np

# --- Page Config ---
st.set_page_config(page_title="Battery Elements Explorer", layout="wide")
st.markdown("<h1 style='text-align:center;color:#00ffff'>🔬 Battery Elements Explorer</h1>", unsafe_allow_html=True)

# --- Sidebar ---
st.sidebar.title("⚡ Explore Elements")
element = st.sidebar.selectbox("Select Element", ["Lithium (Li)", "Lead (Pb)"])
page = st.sidebar.radio("Navigate", ["⚛️ Atomic Model"])

# --- Element Data ---
element_data = {
    "Lithium (Li)": {"protons": 3, "neutrons": 4, "electrons": [2, 1]},
    "Lead (Pb)": {"protons": 82, "neutrons": 125, "electrons": [2,8,18,32,18,4]}
}
data = element_data[element]

# --- Atomic Model ---
if page == "⚛️ Atomic Model":
    st.markdown(f"<h2 style='color:#00ff00'>⚛️ Atomic Model of {element}</h2>", unsafe_allow_html=True)

    shells = data['electrons']
    n_frames = 60
    radii = np.linspace(15, 40, len(shells))  # orbit radii
    frames = []

    # Nucleus coordinates (clustered protons and neutrons)
    proton_positions = np.random.uniform(-2,2,(data['protons'],3))
    neutron_positions = proton_positions + np.random.uniform(-0.5,0.5,(data['neutrons'],3))

    angles = np.linspace(0, 2*np.pi, n_frames)
    for t in angles:
        frame_data = []

        # Protons (red, central)
        frame_data.append(go.Scatter3d(
            x=proton_positions[:,0],
            y=proton_positions[:,1],
            z=proton_positions[:,2],
            mode='markers',
            marker=dict(size=12,color='red',opacity=0.9),
            name='Protons'
        ))

        # Neutrons (pink, stick to protons)
        frame_data.append(go.Scatter3d(
            x=neutron_positions[:,0],
            y=neutron_positions[:,1],
            z=neutron_positions[:,2],
            mode='markers',
            marker=dict(size=12,color='pink',opacity=0.8),
            name='Neutrons'
        ))

        # Electrons orbiting
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
