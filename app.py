import streamlit as st
import pandas as pd
import os
from dotenv import load_dotenv

# ================= CONFIG =================
st.set_page_config(
    page_title="Chamados",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ================= SESSION =================
if "logado" not in st.session_state:
    st.session_state["logado"] = False

# ================= CSS =================
if not st.session_state["logado"]:

    # ESCONDE SIDEBAR NO LOGIN
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

else:

    # CSS DASHBOARD
    st.markdown("""
    <style>

    .stApp {
        background-color: #f5f7fb;
    }

    div.stButton > button {
        border-radius: 8px;
        font-weight: 600;
    }

    </style>
    """, unsafe_allow_html=True)

# ================= LOGIN =================
load_dotenv()

USUARIO = os.getenv("USUARIO")
SENHA = os.getenv("SENHA")

def login():

    # CENTRALIZA LOGIN
    esquerda, centro, direita = st.columns([3,2,3])

    with centro:

        st.markdown(
            '<div class="login-title">🔐 Acesso</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="login-subtitle">Entre para acessar o dashboard</div>',
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
# ================= BOTÃO SAIR =================
col1, col2 = st.columns([16, 2])

with col2:

    st.markdown("""
    <style>

    div.stButton > button {
        width: 100% !important;
        height: 42px !important;
        border-radius: 10px !important;
        font-size: 15px !important;
        font-weight: 600 !important;
        white-space: nowrap !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        gap: 6px !important;
    }

    </style>
    """, unsafe_allow_html=True)

    if st.button("🚪 Sair"):
        st.session_state["logado"] = False
        st.rerun()
        # ================= HEADER =================
st.title("📊 Dashboard Corporativo de Chamados")

st.markdown(
    "Monitoramento de Telefonia e Conectividade"
)

# ================= DADOS =================
dados = [

    ["Capivari", "(19) 3492-2215", "Linha muda",
     "Reparo agendado 05/05", "87LZA0LL09"],

    ["Capivari", "(19) 3879-1317", "Linha muda",
     "Sem expectativa de atendimento", "87LZA0LL09"],

    ["Santo Amaro (Casa da Advocacia)", "11 5546-5596",
     "Linha muda", "Em andamento", "8-7LZ41JGK"],

    ["Santo Amaro (Casa da Advocacia)", "11 5686-4032",
     "Linha muda", "Em andamento", "8-7LZ41JGK"],

    ["Jacareí (Casa da Advocacia)", "(12) 3951-1667",
     "Linha muda - Projeto Rifaina", "Em andamento", "8-7LP8ZUHY"],

    ["São Bernardo do Campo (Sala do Fórum)", "(11) 4330-3855",
     "Não funciona", "Em andamento", "8-7LSGGATV"],

    ["Itaquaquecetuba (Casa da Advocacia)", "(11) 4647-3977",
     "Linha muda", "Em andamento", "8-7LUEYA0K"],

    ["São Miguel Paulista (Casa da Advocacia)", "112037-7055",
     "Escalonado pela Vivo", "Em andamento", "8-7M2KB8NV"]

]

df = pd.DataFrame(
    dados,
    columns=[
        "Local",
        "Produto",
        "Motivo",
        "Status",
        "Chamado"
    ]
)

# ================= FILTROS =================
st.sidebar.header("🔎 Filtros")

local = st.sidebar.multiselect(
    "Local",
    df["Local"].unique(),
    default=df["Local"].unique()
)

chamado = st.sidebar.multiselect(
    "Número do Chamado",
    df["Chamado"].unique(),
    default=df["Chamado"].unique()
)

df_filtrado = df[
    (df["Local"].isin(local)) &
    (df["Chamado"].isin(chamado))
]

# ================= KPIS =================
col1, col2 = st.columns(2)

col1.metric(
    "📞 Total de Chamados",
    len(df_filtrado)
)

col2.metric(
    "🔧 Em andamento",
    len(df_filtrado)
)

st.divider()

# ================= GRÁFICO =================
st.subheader("📊 Chamados por Local")

st.bar_chart(
    df_filtrado["Local"].value_counts()
)

# ================= TABELA =================
st.subheader("📋 Detalhamento dos Chamados")

st.dataframe(
    df_filtrado,
    use_container_width=True,
    hide_index=True
)

# ================= DOWNLOAD =================
st.download_button(
    "📥 Exportar CSV",
    df_filtrado.to_csv(index=False),
    "chamados.csv",
    "text/csv"
)

# ================= INFO =================
st.info(
    "ℹ️ Todos os chamados estão em andamento."
)
