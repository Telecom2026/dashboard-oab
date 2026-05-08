import streamlit as st
import pandas as pd

# ================= CONFIG =================
st.set_page_config(
    page_title="IP Dedicados",
    layout="wide"
)

# ================= SIDEBAR =================
st.sidebar.title("📂 Menu")

st.sidebar.page_link(
    "app.py",
    label="🏠 Dashboard Principal"
)

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
