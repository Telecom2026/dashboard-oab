import streamlit as st
import pandas as pd
import os
from dotenv import load_dotenv

# ================= CONFIG =================
st.set_page_config(page_title="Dashboard de Chamados", layout="wide")

# ================= ESTILO =================
st.markdown("""
<style>

/* REMOVE FUNDO */
.stApp {
    background: none;
}

/* ESCONDE SIDEBAR NO LOGIN */
[data-testid="stSidebar"] {display: none;}

/* TÍTULO */
.login-title {
    font-size: 24px;
    font-weight: 700;
}

/* SUBTÍTULO */
.login-subtitle {
    font-size: 13px;
    margin-bottom: 10px;
}

/* INPUT */
div[data-testid="stTextInput"] input {
    background-color: white;
    color: black;
    height: 32px;
    font-size: 13px;
    border-radius: 6px;
    border: 1px solid #ccc;
}

/* BOTÃO */
div.stButton > button {
    height: 34px;
    font-size: 14px;
    border-radius: 6px;
    font-weight: 600;
}

</style>
""", unsafe_allow_html=True)

# ================= LOGIN =================
load_dotenv()
USUARIO = os.getenv("USUARIO")
SENHA = os.getenv("SENHA")

def login():

    # LOGO NO TOPO DIREITO
    top1, top2 = st.columns([6,1])
    with top2:
        if os.path.exists("logo.png"):
            st.image("logo.png", width=100)

    # LOGIN CENTRAL
    col1, col2, col3 = st.columns([2,1,2])

    with col2:
        st.markdown('<div class="login-title">🔐 Acesso</div>', unsafe_allow_html=True)
        st.markdown('<div class="login-subtitle">Entre para acessar o dashboard</div>', unsafe_allow_html=True)

        st.markdown("**👤 Usuário**")
        usuario = st.text_input("", key="user")

        st.markdown("**🔒 Senha**")
        senha = st.text_input("", type="password", key="pass")

        if st.button("Entrar", use_container_width=True):
            if usuario == USUARIO and senha == SENHA:
                st.session_state["logado"] = True
                st.rerun()
            else:
                st.error("Usuário ou senha inválidos")

# ================= CONTROLE =================
if "logado" not in st.session_state:
    st.session_state["logado"] = False

if not st.session_state["logado"]:
    login()
    st.stop()

# ================= SIDEBAR =================
if st.sidebar.button("🚪 Sair"):
    st.session_state["logado"] = False
    st.rerun()

# ================= HEADER =================
st.title("📊 Dashboard Corporativo de Chamados")
st.markdown("Monitoramento de Telefonia e Conectividade")

# ================= DADOS =================
dados = [
    ["Capivari", "(19) 3492-2215", "Linha muda", "Em andamento", "87LZA0LL09"],
    ["Capivari", "(19) 3879-1317", "Linha muda", "Em andamento", "87LZA0LL09"],

    ["Santo Amaro (Casa da Advocacia)", "11 5546-5596", "linha muda", "Em andamento", "8-7LZ41JGK"],
    ["Santo Amaro (Casa da Advocacia)", "11 5686-4032", "linha muda", "Em andamento", "8-7LZ41JGK"],
    ["Santo Amaro (Casa da Advocacia)", "11 5524-5369", "linha muda", "Em andamento", "8-7LZ41JGK"],
    ["Santo Amaro (Casa da Advocacia)", "11 5524-7409", "linha muda", "Em andamento", "8-7LZ41JGK"],
    ["Santo Amaro (Vara do Trabalho)", "11 5521-2381", "linha muda", "Em andamento", "8-7LZ41JGK"],
    ["Santo Amaro (Casa da Advocacia)", "11 5524-1990", "linha muda", "Em andamento", "8-7LZ41JGK"],
    ["Santo Amaro (Casa da Advocacia)", "11 5524-3966", "linha muda", "Em andamento", "8-7LZ41JGK"],
    ["Santo Amaro (Vara do Trabalho)", "11 5521-0862", "linha muda", "Em andamento", "8-7LZ41JGK"],

    ["Jacareí (Casa da Advocacia)", "(12) 3951-1667", "Linha muda - Projeto Rifaina", "Em andamento", "8-7LP8ZUHY"],
    ["Jacareí (Casa da Advocacia)", "(12) 3951-3766", "Linha muda - Projeto Rifaina", "Em andamento", "8-7LP8ZUHY"],
    ["Jacareí (Casa da Advocacia)", "(12) 3961-7650", "Linha muda - Projeto Rifaina", "Em andamento", "8-7LWS83NK"],

    ["São Bernardo do Campo (Sala do Fórum)", "(11) 4330-3855", "Não funciona", "Em andamento", "8-7LSGGATV"],

    ["Itaquaquecetuba (Casa da Advocacia)", "(11) 4647-3977", "Linha muda", "Em andamento", "6801189283"],
    ["Itaquaquecetuba (Casa da Advocacia)", "(11) 4640-1874", "Linha muda", "Em andamento", "6801189284"],

    ["São José do Rio Preto (Sala do Fórum)", "-", "Instalação agendada 06/05", "Aguardo protocolo", ""],
    ["São José do Rio Preto (Sala do Fórum)", "-", "Instalação agendada 06/05", "Aguardo protocolo", "-"],
]

df = pd.DataFrame(dados, columns=["Local", "Telefone", "Motivo", "Status", "Chamado"])

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

# ================= KPIs =================
col1, col2 = st.columns(2)

col1.metric("📞 Total de Chamados", len(df_filtrado))
col2.metric("🔧 Em andamento", len(df_filtrado))

st.divider()

# ================= GRÁFICO =================
st.subheader("📊 Chamados por Local")
st.bar_chart(df_filtrado["Local"].value_counts())

# ================= TABELA =================
st.subheader("📋 Detalhamento dos Chamados")
st.dataframe(df_filtrado, use_container_width=True)

# ================= DOWNLOAD =================
st.download_button(
    "📥 Exportar CSV",
    df_filtrado.to_csv(index=False),
    "chamados.csv",
    "text/csv"
)

# ================= INFO =================
st.info("ℹ️ Todos os chamados estão em andamento.")
