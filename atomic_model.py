import streamlit as st
import plotly.graph_objects as go
import numpy as np
import time

st.set_page_config(layout="wide")
st.title("⚛️ 3D Atomic Model - Animated & Locked Nucleus")

# Sidebar
element = st.sidebar.selectbox("Select Element", ["Lithium (Li)", "Lead (Pb)"])

# Element info
elements = {
    "Lithium (Li)": {"protons": 3, "neutrons": 4, "electrons": [2, 1]},
    "Lead (Pb)": {"protons": 82, "neutrons": 125, "electrons": [2, 8, 18, 32, 18, 4]}
}

info = elements[element]
shells = info["electrons"]
radii = np.linspace(10, 30, len(shells))

# --- Nucleus coordinates (locked) ---
nucleus_protons = np.zeros((info["protons"], 3))
nucleus_neutrons = np.zeros((info["neutrons"], 3))

# --- Create 3D figure ---
fig = go.Figure()

# Protons
fig.add_trace(go.Scatter3d(
    x=nucleus_protons[:,0], y=nucleus_protons[:,1], z=nucleus_protons[:,2],
    mode='markers', marker=dict(size=8, color='red'), name='Protons'
))

# Neutrons
fig.add_trace(go.Scatter3d(
    x=nucleus_neutrons[:,0], y=nucleus_neutrons[:,1], z=nucleus_neutrons[:,2],
    mode='markers', marker=dict(size=8, color='blue'), name='Neutrons'
))

# Electron traces placeholders
electron_traces = []
for i, num in enumerate(shells):
    angles = np.linspace(0, 2*np.pi, num, endpoint=False)
    x = radii[i] * np.cos(angles)
    y = radii[i] * np.sin(angles)
    z = np.zeros_like(x)
    trace = go.Scatter3d(
        x=x, y=y, z=z, mode='markers', marker=dict(size=4, color='yellow'), name=f'Shell {i+1}'
    )
    electron_traces.append(trace)
    fig.add_trace(trace)

fig.update_layout(
    scene=dict(
        xaxis=dict(showbackground=False, visible=False),
        yaxis=dict(showbackground=False, visible=False),
        zaxis=dict(showbackground=False, visible=False)
    ),
    margin=dict(l=0, r=0, t=0, b=0)
)

plotly_chart = st.plotly_chart(fig, use_container_width=True)

# --- Animate electrons ---
angle = 0
while True:
    angle += 0.05
    for i, num in enumerate(shells):
        theta = np.linspace(0, 2*np.pi, num, endpoint=False) + angle*(i+1)
        phi = np.linspace(0, np.pi, num)  # give slight tilt for 3D orbit
        x = radii[i]*np.cos(theta)
        y = radii[i]*np.sin(theta)*np.cos(theta)  # 3D twist
        z = radii[i]*np.sin(theta)*np.sin(theta)
        fig.data[2+i].x = x
        fig.data[2+i].y = y
        fig.data[2+i].z = z
    plotly_chart.plotly_chart(fig, use_container_width=True)
    time.sleep(0.05)
