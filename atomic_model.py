import streamlit as st
import matplotlib.pyplot as plt
import math

# --- Element data (simplified) ---
elements = {
    "Lithium (Li)": {"protons": 3, "neutrons": 4, "electrons": 3, "symbol": "Li"},
    "Lead (Pb)": {"protons": 82, "neutrons": 125, "electrons": 82, "symbol": "Pb"},
}

# --- Streamlit UI ---
st.title("Atomic Model of Elements for Batteries")
st.write("Choose an element to visualize its atomic structure.")

element = st.selectbox("Select Element:", list(elements.keys()))

data = elements[element]

# --- Draw atomic model ---
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_aspect("equal")
ax.axis("off")

# Draw nucleus
nucleus = f"{data['protons']}p, {data['neutrons']}n"
ax.text(0, 0, nucleus, ha="center", va="center", fontsize=12, color="red",
        bbox=dict(facecolor="yellow", alpha=0.5, boxstyle="circle"))

# Draw electron shells (very simplified Bohr model)
num_electrons = data["electrons"]
shells = [2, 8, 18, 32, 18, 8]  # Max per shell (Bohr model)
radius_step = 1.5
electrons_left = num_electrons
r = radius_step

for shell in shells:
    if electrons_left <= 0:
        break
    electrons_in_shell = min(shell, electrons_left)
    for i in range(electrons_in_shell):
        angle = 2 * math.pi * i / electrons_in_shell
        x = r * math.cos(angle)
        y = r * math.sin(angle)
        ax.plot(x, y, "bo", markersize=10)
    r += radius_step
    electrons_left -= electrons_in_shell

st.pyplot(fig)

# --- Chemical reaction explanation ---
st.subheader("Battery Chemistry Explanation")
if element == "Lithium (Li)":
    st.write("""
    Lithium is highly reactive and loses **1 electron** easily, 
    forming **Li⁺ ions**.  
    In lithium batteries, these ions move between electrodes during charge and discharge.
    """)
elif element == "Lead (Pb)":
    st.write("""
    Lead is used in **lead-acid batteries**.  
    The Pb and PbO₂ electrodes react with sulfuric acid to produce electricity.  
    Lead can change oxidation states between **Pb²⁺** and **Pb⁴⁺**.
    """)

st.write("Together, Lithium and Lead are both important in **battery technology**, though in different types of batteries (Lithium-ion vs Lead-acid).")
