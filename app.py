import streamlit as st
import pandas as pd
import os
from dotenv import load_dotenv

# ================= CONFIG =================
st.set_page_config(page_title="Dashboard de Chamados", layout="wide")

# ================= ESTILO =================
st.markdown("""
<style>

/* FUNDO */
.stApp {
    background: linear-gradient(135deg, #1c2f38, #0f2027);
}

/* ESCONDE SIDEBAR NO LOGIN */
[data-testid="stSidebar"] {display: none;}

/* LOGO NO TOPO DIREITO */
.logo {
    position: absolute;
    top: 20px;
    right: 30px;
}

.logo img {
    width: 120px;   /* 🔥 tamanho pequeno tipo logo */
}

/* TÍTULO */
.login-title {
    font-size: 24px;
    font-weight: 700;
    color: white;
}

/* SUBTÍTULO */
.login-subtitle {
    color: #cbd5e1;
    font-size: 13px;
    margin-bottom: 15px;
}

/* LABEL CUSTOM */
.custom-label {
    color: white;
    font-weight: 600;
    margin-top: 10px;
    margin-bottom: 3px;
    font-size: 14px;
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

/* FOCO */
div[data-testid="stTextInput"] input:focus {
    border: 2px solid #0A66C2;
    box-shadow: 0 0 5px rgba(10,102,194,0.5);
}

/* BOTÃO */
div.stButton > button {
    background: linear-gradient(90deg, #0A66C2, #004182);
    color: white;
    height: 34px;
    font-size: 14px;
    border-radius: 6px;
    border: none;
    font-weight: 600;
}

</style>
""", unsafe_allow_html=True)

# ================= LOGIN =================
load_dotenv()
USUARIO = os.getenv("USUARIO")
SENHA = os.getenv("SENHA")

def login():

    # LOGO
    if os.path.exists("logo.png"):
        st.markdown('<div class="logo">', unsafe_allow_html=True)
        st.image("logo.png")
        st.markdown('</div>', unsafe_allow_html=True)

    # CENTRALIZA LOGIN
    col1, col2, col3 = st.columns([2,1,2])

    with col2:
        st.markdown('<div class="login-title">🔐 Acesso</div>', unsafe_allow_html=True)
        st.markdown('<div class="login-subtitle">Entre para acessar o dashboard</div>', unsafe_allow_html=True)

        # 🔥 CAMPOS DESTACADOS
        st.markdown('<div class="custom-label">👤 Usuário</div>', unsafe_allow_html=True)
        usuario = st.text_input("", key="user")

        st.markdown('<div class="custom-label">🔒 Senha</div>', unsafe_allow_html=True)
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

# ================= CATEGORIA =================
def padronizar_motivo(motivo):
    motivo = motivo.lower()

    if "linha muda" in motivo or "não funciona" in motivo:
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

local = st.sidebar.multiselect("Local", df["Local"].unique(), default=df["Local"].unique())
categoria = st.sidebar.multiselect("Categoria", df["Categoria"].unique(), default=df["Categoria"].unique())

df_filtrado = df[(df["Local"].isin(local)) & (df["Categoria"].isin(categoria))]

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
st.download_button("📥 Exportar CSV",
                   df_filtrado.to_csv(index=False),
                   "chamados.csv",
                   "text/csv")

# ================= INFO =================
st.info("ℹ️ Todos os chamados estão em andamento.")
