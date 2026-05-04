import streamlit as st
import pandas as pd

# ================= CONFIG =================
st.set_page_config(page_title="Dashboard de Chamados", layout="wide")

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

    col1, col2 = st.columns([1, 1])

    # 🔹 LOGIN (ESQUERDA)
    with col1:
        st.markdown("""
            <style>
            .login-container {
                max-width: 400px;
                margin-top: 120px;
                padding: 2rem;
                background-color: #f5f5f5;
                border-radius: 12px;
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

    # 🔹 IMAGEM (DIREITA)
    with col2:
        st.image("fundo.jpg", use_container_width=True)

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

    ["Jacareí (Casa da Advocacia)", "(12) 3951-1667", "Linha muda", "Em andamento"],

    ["São José do Rio Preto", "-", "Sem internet", "Em andamento"],
]

df = pd.DataFrame(dados, columns=["Local", "Telefone", "Motivo", "Status"])

# ================= KPIs =================
col1, col2 = st.columns(2)
col1.metric("📞 Total de Chamados", len(df))
col2.metric("🔧 Em andamento", len(df))

st.divider()

# ================= GRÁFICO =================
st.subheader("📊 Chamados por Categoria")
st.bar_chart(df["Motivo"].value_counts())

# ================= TABELA =================
st.subheader("📋 Detalhamento dos Chamados")
st.dataframe(df, use_container_width=True)

# ================= DOWNLOAD =================
st.download_button(
    "📥 Exportar CSV",
    df.to_csv(index=False),
    "chamados.csv",
    "text/csv"
)

# ================= INFO =================
st.info("ℹ️ Todos os chamados estão em andamento.")
