import streamlit as st

# ---------------- CONFIG ----------------
st.set_page_config(page_title="Battery Elements Explorer", layout="wide")

# Custom CSS for appearance
st.markdown(
    """
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
    .highlight {
        background-color: #fff3cd;
        padding: 5px 10px;
        border-radius: 8px;
        font-weight: bold;
    }
    .stSidebar {
        background-color: #e9ecef;
        border-right: 2px solid #dee2e6;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------------- SIDEBAR ----------------
st.sidebar.title("🔬 Navigation")
page = st.sidebar.radio("Go to:", ["🏠 Home", "📊 Physical Properties", "☢️ Nuclear & E-Waste Effects"])

if page == "🏠 Home":
    st.sidebar.markdown("---")
    atom_choice = st.sidebar.selectbox("⚛️ Select an element:", ["Lithium (Li)", "Lead (Pb)"])


# ---------------- PAGE 1: HOME ----------------
if page == "🏠 Home":
    st.markdown('<div class="main-title">⚡ Atomic Models of Battery Elements ⚡</div>', unsafe_allow_html=True)

    st.write(
        """
        Welcome to the **Battery Elements Explorer**! 🚀  
        This interactive project focuses on two important elements in **battery technology**:  
        
        - 🔹 **Lithium (Li)** → The heart of modern **rechargeable lithium-ion batteries** used in smartphones, laptops, and electric vehicles.  
        - 🔸 **Lead (Pb)** → A key component of **lead-acid batteries**, one of the oldest types of rechargeable batteries, still widely used in cars and backup systems.  

        In this section, you can view **animated atomic models** showing:  
        - 🟡 **Electrons** orbiting the nucleus in specific shells  
        - 🔵 **Protons** and 🔴 **Neutrons** tightly packed in the nucleus  
        
        These simple atomic structures explain why these elements behave the way they do in **chemical reactions**.  
        """
    )

    if atom_choice == "Lithium (Li)":
        st.markdown('<div class="section-title">🔹 Lithium (Li)</div>', unsafe_allow_html=True)
        st.image("lithium.gif", caption="Lithium Atom Model (Animated)", use_container_width=True)
        st.markdown(
            """
            - **Atomic Number:** 3  
            - **Category:** Alkali Metal (very reactive)  
            - **Battery Role:** Stores and releases energy by moving between electrodes.  

            **Discharge Reaction (Lithium-ion battery):**  
            <span class='highlight'>LiC₆ + CoO₂ → C₆ + LiCoO₂</span>  

            👉 Lithium atoms are lightweight and small, making them perfect for **high-energy density** batteries.  
            """
            , unsafe_allow_html=True
        )

    elif atom_choice == "Lead (Pb)":
        st.markdown('<div class="section-title">🔸 Lead (Pb)</div>', unsafe_allow_html=True)
        st.image("lead.gif", caption="Lead Atom Model (Animated)", use_container_width=True)
        st.markdown(
            """
            - **Atomic Number:** 82  
            - **Category:** Post-Transition Metal (dense and stable)  
            - **Battery Role:** Reacts with lead dioxide and sulfuric acid to produce electricity.  

            **Discharge Reaction (Lead-acid battery):**  
            <span class='highlight'>Pb + PbO₂ + 2H₂SO₄ → 2PbSO₄ + 2H₂O</span>  

            👉 Lead is heavy, but it’s cheap and reliable, which is why **lead-acid batteries** are still common in vehicles.  
            """
            , unsafe_allow_html=True
        )


# ---------------- PAGE 2: PHYSICAL PROPERTIES ----------------
elif page == "📊 Physical Properties":
    st.markdown('<div class="main-title">📊 Physical Properties Comparison</div>', unsafe_allow_html=True)

    st.write(
        """
        The behavior of elements is strongly linked to their **physical properties**.  
        Here’s a side-by-side look at **Lithium** and **Lead**.  
        
        - Lithium is light, soft, and reacts easily, which explains why it’s useful in **fast-charging batteries**.  
        - Lead is heavy, dense, and less reactive, giving it stability and long-lasting performance in **car batteries**.  
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
            "🔴 Neutrons (common isotope)", 
            "🟡 Electrons"
        ],
        "Lithium (Li)": [
            "1342", 
            "180.5", 
            "84.8", 
            "10.6", 
            "Alkali Metal (Group 1)", 
            "3", 
            "4", 
            "3"
        ],
        "Lead (Pb)": [
            "1749", 
            "327.5", 
            "35.3", 
            "4.8", 
            "Post-Transition Metal (Group 14)", 
            "82", 
            "125", 
            "82"
        ]
    })

    st.markdown(
        """
        **Key Insights:**  
        - 🟢 Lithium’s **low melting point** and **high reactivity** make it great for **energy transfer**.  
        - 🔵 Lead’s **high density** and **moderate conductivity** make it more stable but heavier, limiting portability.  
        """
    )


# ---------------- PAGE 3: NUCLEAR & E-WASTE ----------------
elif page == "☢️ Nuclear & E-Waste Effects":
    st.markdown('<div class="main-title">☢️ Nuclear Symbols & Environmental Impact</div>', unsafe_allow_html=True)

    st.subheader("⚛️ Nuclear Symbols")
    st.markdown(
        """
        Every element can be represented by its **nuclear symbol**, which shows the number of **protons** and 
        **nucleons (protons + neutrons)**.  

        - Lithium → <span class="highlight">⁷₃Li</span>  
        - Lead → <span class="highlight">²⁰⁷₈₂Pb</span>  

        👉 These symbols are essential for **nuclear chemistry** and understanding isotopes.  
        """,
        unsafe_allow_html=True
    )

    st.subheader("🗑️ Effects of Electronic Waste")
    st.write(
        """
        Improper disposal of **used batteries** causes serious problems:  

        - 🔹 **Lithium-ion batteries**  
          - Can catch fire or explode if damaged 🔥  
          - Lithium compounds are highly reactive ⚡  

        - 🔸 **Lead-acid batteries**  
          - Leak **toxic lead** and **sulfuric acid** ☣️  
          - Contaminate soil and water 🌍  

        ### Why Recycling Matters ♻️  
        - Recovers **valuable metals** (Lithium, Lead, Cobalt)  
        - Prevents **toxic pollution**  
        - Reduces the need for harmful **mining activities**  
        - Protects **human health** and **ecosystems** 🌱  

        ✅ In conclusion: **Safe recycling = safer environment!**  
        """
    )
