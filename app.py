import streamlit as st
import pandas as pd

# ================= CONFIG =================
st.set_page_config(page_title="Dashboard de Chamados", layout="wide")

# ================= FUNDO (SEM IMAGEM) =================
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
    }
    </style>
""", unsafe_allow_html=True)

# ================= LOGIN (SECRETS) =================
try:
    USUARIO = st.secrets["USUARIO"]
    SENHA = st.secrets["SENHA"]
except:
    st.error("⚠️ Credenciais não configuradas em Secrets")
    st.stop()

# ================= LOGIN =================
def login():
    # esconder sidebar
    st.markdown("""
        <style>
        [data-testid="stSidebar"] {display: none;}
        </style>
    """, unsafe_allow_html=True)

    # layout com login à direita
    col1, col2 = st.columns([2, 1])

    with col2:
        st.markdown("""
            <style>
            .login-container {
                background-color: rgba(0, 0, 0, 0.75);
                padding: 2rem;
                border-radius: 12px;
                margin-top: 120px;
                color: white;
            }

            div[data-testid="stTextInput"] input {
                text-align: center;
            }
            </style>
        """, unsafe_allow_html=True)

        st.markdown('<div class="login-container">', unsafe_allow_html=True)

        st.markdown("## 🔐 Acesso ao Dashboard")

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

# ================= ESTILO DASH =================
st.markdown("""
    <style>
    .block-container {
        background-color: rgba(0, 0, 0, 0.65);
        padding: 2rem;
        border-radius: 12px;
    }

    section[data-testid="stSidebar"] {
        background-color: rgba(0, 0, 0, 0.85);
    }

    h1, h2, h3, h4, h5, h6, p, div {
        color: white !important;
    }
    </style>
""", unsafe_allow_html=True)

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
