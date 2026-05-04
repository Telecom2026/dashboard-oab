import streamlit as st
import pandas as pd
import os
from dotenv import load_dotenv

# ================= CONFIG =================
st.set_page_config(page_title="Dashboard de Chamados", layout="wide")

# ================= FUNDO ESCURO =================
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #1c2f38, #0f2027);
    }

    [data-testid="stSidebar"] {display: none;}

    .login-container {
        max-width: 380px;
        margin-top: 120px;
        padding: 2rem;
        background-color: white;
        border-radius: 16px;
        box-shadow: 0 8px 25px rgba(0,0,0,0.2);
    }

    .login-title {
        font-size: 28px;
        font-weight: 600;
        margin-bottom: 5px;
    }

    .login-subtitle {
        color: #666;
        margin-bottom: 20px;
    }

    div[data-testid="stTextInput"] input {
        border-radius: 8px;
        padding: 10px;
    }

    div.stButton > button {
        background-color: #0A66C2;
        color: white;
        border-radius: 8px;
        height: 45px;
        font-weight: 600;
        border: none;
    }

    div.stButton > button:hover {
        background-color: #004182;
    }

    .image-container img {
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    }
    </style>
""", unsafe_allow_html=True)

# ================= LOGIN SEGURO =================
load_dotenv()

USUARIO = os.getenv("USUARIO")
SENHA = os.getenv("SENHA")

# ================= LOGIN =================
def login():
    col1, col2 = st.columns([1, 1.2])

    # LOGIN (ESQUERDA)
    with col1:
        st.markdown('<div class="login-container">', unsafe_allow_html=True)

        st.markdown('<div class="login-title">🔐 Acesso</div>', unsafe_allow_html=True)
        st.markdown('<div class="login-subtitle">Entre para acessar o dashboard</div>', unsafe_allow_html=True)

        usuario = st.text_input("Usuário")
        senha = st.text_input("Senha", type="password")

        if st.button("Entrar", use_container_width=True):
            if usuario == USUARIO and senha == SENHA:
                st.session_state["logado"] = True
                st.rerun()
            else:
                st.error("Usuário ou senha inválidos")

        st.markdown('</div>', unsafe_allow_html=True)

    # IMAGEM (DIREITA)
    with col2:
        if os.path.exists("fundo.jpg"):
            st.markdown('<div class="image-container">', unsafe_allow_html=True)
            st.image("fundo.jpg", use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

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
    ["Capivari", "(19) 3879-1317", "Linha muda", "Em andamento"],
    ["Capivari", "(19) 3492-2215", "Linha muda", "Em andamento"],

    ["Santo Amaro (Casa da Advocacia)", "11 5546-5596", "Linha muda", "Em andamento"],
    ["Santo Amaro (Casa da Advocacia)", "11 5686-4032", "Linha muda", "Em andamento"],
    ["Santo Amaro (Casa da Advocacia)", "11 5524-5369", "Linha muda", "Em andamento"],
    ["Santo Amaro (Casa da Advocacia)", "11 5524-7409", "Não funciona", "Em andamento"],
    ["Santo Amaro (Vara do Trabalho)", "11 5521-2381", "Apenas recebe ligações", "Em andamento"],
    ["Santo Amaro (Casa da Advocacia)", "11 5524-3966", "Apenas recebe ligações", "Em andamento"],
    ["Santo Amaro (Vara do Trabalho)", "11 5521-0862", "Não recebe ligações", "Em andamento"],

    ["Jacareí (Casa da Advocacia)", "(12) 3951-1667", "Linha muda", "Em andamento"],
    ["Jacareí (Casa da Advocacia)", "(12) 3951-3766", "Linha muda", "Em andamento"],
    ["Jacareí (Casa da Advocacia)", "(12) 3961-7650", "Fora do projeto", "Em andamento"],

    ["São Bernardo do Campo (Sala do Fórum)", "(11) 4330-3855", "Não funciona", "Em andamento"],

    ["Itaquaquecetuba (Casa da Advocacia)", "(11) 4647-3977", "Linha muda", "Em andamento"],
    ["Itaquaquecetuba (Casa da Advocacia)", "(11) 4640-1874", "Linha muda", "Em andamento"],

    ["São José do Rio Preto (Sala do Fórum)", "-", "Sem internet", "Em andamento"],
]

df = pd.DataFrame(dados, columns=["Local", "Telefone", "Motivo", "Status"])

# ================= PADRONIZAÇÃO =================
def padronizar_motivo(motivo):
    motivo = motivo.lower()

    if "linha muda" in motivo or "mudo" in motivo or "não funciona" in motivo:
        return "Falha de comunicação"
    elif "apenas recebe" in motivo:
        return "Recebimento parcial"
    elif "não recebe" in motivo:
        return "Falha de recebimento"
    elif "internet" in motivo:
        return "Sem internet"
    elif "projeto" in motivo:
        return "Configuração / Projeto"
    else:
        return "Outros"

df["Categoria"] = df["Motivo"].apply(padronizar_motivo)

# ================= FILTROS =================
st.sidebar.header("🔎 Filtros")

local = st.sidebar.multiselect(
    "Local",
    df["Local"].unique(),
    default=df["Local"].unique()
)

categoria = st.sidebar.multiselect(
    "Categoria",
    df["Categoria"].unique(),
    default=df["Categoria"].unique()
)

df_filtrado = df[
    (df["Local"].isin(local)) &
    (df["Categoria"].isin(categoria))
]

# ================= KPIs =================
col1, col2 = st.columns(2)
col1.metric("📞 Total de Chamados", len(df_filtrado))
col2.metric("🔧 Em andamento", len(df_filtrado))

st.divider()

# ================= GRÁFICO =================
st.subheader("📊 Chamados por Categoria")
st.bar_chart(df_filtrado["Categoria"].value_counts())

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
