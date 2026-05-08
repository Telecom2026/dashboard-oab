import streamlit as st
import pandas as pd

# ================= VALIDA LOGIN =================
if "logado" not in st.session_state:
    st.session_state["logado"] = False

if not st.session_state["logado"]:
    st.switch_page("app.py")

# ================= CONFIG =================
st.set_page_config(
    page_title="IP Dedicados",
    layout="wide"
)

# ================= MENU =================
st.sidebar.title("📂 Menu")

if st.sidebar.button("🏠 Dashboard Principal"):
    st.switch_page("app.py")
    # ================= TÍTULO =================
st.title("📡 Controle de IP Dedicados")

# ================= DADOS =================
dados = {
    "NRC": ["0439387231"],
    "Produto": ["IP Dedicado"],
    "Corresponde a": ["Justiça Federal - Atendimento"],
    "Contrato": ["0877 DJ"],
    "Vencimento": ["27/05"]
}

df = pd.DataFrame(dados)

# ================= TABELA =================
st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
)
