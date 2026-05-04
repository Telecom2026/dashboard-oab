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

/* REMOVE ESPAÇOS */
.block-container {
    padding-top: 2rem;
}

/* ESCONDE SIDEBAR NO LOGIN */
[data-testid="stSidebar"] {display: none;}

/* LOGIN */
.login-container {
    max-width: 420px;
    margin-top: 120px;
}

/* TÍTULO */
.login-title {
    font-size: 32px;
    font-weight: 700;
    color: white;
}

/* SUBTÍTULO */
.login-subtitle {
    color: #cbd5e1;
    margin-bottom: 25px;
}

/* LABELS */
label {
    color: #e2e8f0 !important;
    font-weight: 500;
}

/* INPUTS BRANCOS */
div[data-testid="stTextInput"] input {
    background-color: white;
    color: black;
    border-radius: 10px;
    padding: 12px;
    border: 1px solid #ccc;
}

/* BOTÃO */
div.stButton > button {
    background: linear-gradient(90deg, #0A66C2, #004182);
    color: white;
    border-radius: 10px;
    height: 48px;
    font-weight: 600;
    border: none;
}

/* IMAGEM NO TOPO DIREITO */
.top-image {
    position: absolute;
    top: 40px;
    right: 60px;
}

.top-image img {
    width: 380px;  /* ~60% menor */
    border-radius: 20px;
    filter: brightness(0.6);
}

</style>
""", unsafe_allow_html=True)

# ================= LOGIN =================
load_dotenv()
USUARIO = os.getenv("USUARIO")
SENHA = os.getenv("SENHA")

def login():
    # IMAGEM NO TOPO DIREITO
    if os.path.exists("fundo.jpg"):
        st.markdown('<div class="top-image">', unsafe_allow_html=True)
        st.image("fundo.jpg")
        st.markdown('</div>', unsafe_allow_html=True)

    # LOGIN
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
