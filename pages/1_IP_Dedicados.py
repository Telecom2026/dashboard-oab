import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="IP Dedicados",
    layout="wide"
)

st.title("📡 IP Dedicados")

# Dados da tabela
dados = {
    "NRC": ["0439387231"],
    "Produto": ["IP Dedicado"],
    "Corresponde a": ["Justiça Federal - Atendimento"],
    "Contrato": ["0877 DJ"],
    "Vencimento": ["27/05"]
}

# Criando DataFrame
df = pd.DataFrame(dados)

# Exibindo tabela
st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
)
