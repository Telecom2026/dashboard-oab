import streamlit as st
import pandas as pd
import os
from dotenv import load_dotenv

# ================= CONFIG =================
st.set_page_config(
    page_title="IP Dedicado",
    layout="wide"
)

# ================= SESSION =================
if "logado" not in st.session_state:
    st.session_state["logado"] = False

# ================= CSS =================
if not st.session_state["logado"]:

    st.markdown("""
    <style>

    section[data-testid="stSidebar"] {
        display: none;
    }

    .stApp {
        background-color: #f5f7fb;
    }

    .login-title {
        font-size: 34px;
        font-weight: 700;
        text-align: center;
        margin-bottom: 5px;
    }

    .login-subtitle {
        text-align: center;
        color: #666;
        margin-bottom: 30px;
    }

    div[data-testid="stTextInput"] input {
        height: 45px;
        border-radius: 10px;
        border: 1px solid #dcdcdc;
        background-color: white;
    }

    div.stButton > button {
        height: 45px;
        border-radius: 10px;
        font-size: 16px;
        font-weight: 600;
    }

    </style>
    """, unsafe_allow_html=True)

# ================= LOGIN =================
load_dotenv()

USUARIO = os.getenv("USUARIO")
SENHA = os.getenv("SENHA")

def login():

    esquerda, centro, direita = st.columns([3,2,3])

    with centro:

        st.markdown(
            '<div class="login-title">🔐 Acesso</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="login-subtitle">Entre para acessar o relatório</div>',
            unsafe_allow_html=True
        )

        st.markdown("### 👤 Usuário")

        usuario = st.text_input(
            "",
            key="usuario"
        )

        st.markdown("### 🔒 Senha")

        senha = st.text_input(
            "",
            type="password",
            key="senha"
        )

        st.markdown("<br>", unsafe_allow_html=True)

        if st.button(
            "Entrar",
            use_container_width=True
        ):

            if usuario == USUARIO and senha == SENHA:

                st.session_state["logado"] = True
                st.rerun()

            else:
                st.error("Usuário ou senha inválidos")

# ================= CONTROLE LOGIN =================
if not st.session_state["logado"]:
    login()
    st.stop()

# ================= BOTÃO SAIR =================
col1, col2 = st.columns([15, 2.2])

with col2:

    st.markdown("""
    <style>

    div.stButton > button {
        width: 115px !important;
        height: 42px !important;
        border-radius: 10px !important;
        font-size: 15px !important;
        font-weight: 600 !important;

        display: flex !important;
        align-items: center !important;
        justify-content: center !important;

        gap: 8px !important;

        white-space: nowrap !important;
        overflow: hidden !important;

        padding: 0 14px !important;
    }

    </style>
    """, unsafe_allow_html=True)

    if st.button("🚪 Sair"):
        st.session_state["logado"] = False
        st.rerun()

# ================= HEADER =================
st.title("📡 Controle de IP Dedicado")

st.markdown(
    "Monitoramento de IP Dedicado"
)

# ================= DADOS =================
dados = [

    ["0439387231",
     "IP Dedicado",
     "Atendimento (Justiça Federal)",
     "0877 DJ",
     "27/05"]

]

df = pd.DataFrame(
    dados,
    columns=[
        "NRC",
        "Produto",
        "Corresponde a",
        "Contrato",
        "Vencimento"
    ]
)

# ================= TABELA =================
st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
)

# ================= DOWNLOAD =================
st.download_button(
    "📥 Exportar CSV",
    df.to_csv(index=False),
    "ip_dedicado.csv",
    "text/csv"
)

# ================= INFO =================
st.info(
    "ℹ️ Monitoramento do circuito IP Dedicado."
)
