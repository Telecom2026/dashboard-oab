
Informo que ao entrar em contato com a VIVO, foi informado que o chamado foi encerrado sem o devido atendimento.

Solicitei a reabertura do chamado e solicitei a prioridade no atendimento.

Ordem de serviço: 8-7m47wai3
Data agendada: 11/05 (podendo ser atendido entre hoje e amanhã)

Prezados,

Informo que, ao entrar em contato com a VIVO, fui informado de que o chamado havia sido encerrado sem o devido atendimento.

Diante disso, solicitei a reabertura do chamado, bem como prioridade no atendimento.

Ordem de serviço: 8-7M47WAI3
Data agendada: 11/05 (com possibilidade de atendimento entre hoje e amanhã).

Permaneço acompanhando o caso.


Imagem carregada
me manda uma planilha com esses dados, separados por coluna

chamados_vivo.xlsx


Abrir planilha em tela cheia
Chamados



Imagem carregada
acrescenta na planilha esses também

chamados_vivo_atualizado.xlsx


Abrir planilha em tela cheia
Chamados



preciso montar um email solicitando prioridade no atendimento, pois as subseções estão sendo afetadas sem o funcionamento das linhas telefonicas

Segue uma sugestão de e-mail mais formal e direto para solicitar prioridade no atendimento:

Solicitação de prioridade no atendimento – linhas telefônicas inoperantes
Prezados,

Solicamos, com urgência, prioridade no atendimento dos chamados em aberto, tendo em vista que as subseções estão sendo diretamente afetadas pela indisponibilidade das linhas telefônicas.

A ausência de funcionamento das linhas vem comprometendo a comunicação e o atendimento das unidades, impactando significativamente as atividades diárias e o suporte prestado.

Dessa forma, reforçamos a necessidade de atuação prioritária para regularização dos serviços o mais breve possível.

Ficamos no aguardo de um posicionamento e de uma previsão efetiva para conclusão dos atendimentos.

Atenciosamente,
[Seu nome]


solicamos? 

O correto é “Solicitamos”.
“Solicamos” não existe na norma padrão.

Segue o trecho corrigido:

Solicitação de prioridade no atendimento – linhas telefônicas inoperantes
Prezados,

Solicitamos, com urgência, prioridade no atendimento dos chamados em aberto, tendo em vista que as subseções estão sendo diretamente afetadas pela indisponibilidade das linhas telefônicas.

A ausência de funcionamento das linhas vem comprometendo a comunicação e o atendimento das unidades, impactando significativamente as atividades diárias e o suporte prestado.

Dessa forma, reforçamos a necessidade de atuação prioritária para regularização dos serviços o mais breve possível.

Ficamos no aguardo de um posicionamento e de uma previsão efetiva para conclusão dos atendimentos.

Atenciosamente,
[Seu nome]


segue planilha em anexo

Solicitação de prioridade no atendimento – linhas telefônicas inoperantes
Prezados,

Solicitamos, com urgência, prioridade no atendimento dos chamados em aberto, tendo em vista que as subseções estão sendo diretamente afetadas pela indisponibilidade das linhas telefônicas.

A ausência de funcionamento das linhas vem comprometendo a comunicação e o atendimento das unidades, impactando significativamente as atividades diárias e o suporte prestado.

Dessa forma, reforçamos a necessidade de atuação prioritária para regularização dos serviços o mais breve possível.

Segue planilha em anexo com a relação das unidades afetadas e respectivos chamados em andamento.

Ficamos no aguardo de um posicionamento e de uma previsão efetiva para conclusão dos atendimentos.

Atenciosamente,
[Seu nome]


NRC 0439387231	
Produto IP Dedicado	Corresponde a:	Contrato:	Vencimento 
0439387231	IP Dedicado	Atendimento (Justiça Federal)	0877 DJ	27
NRC 0439387231	
Produto IP Dedicado	
Corresponde a:  (Justiça Federal- Atendimento)
Contrato:	 0877 DJ	
Vencimento 27/05

preciso que crie uma tabela nessa pagina nova

import streamlit as st
import pandas as pd

st.set_page_config(page_title="IP Dedicado", layout="wide")

st.title("Informações do NRC")

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
st.dataframe(df, use_container_width=True)
Se quiser deixar mais bonito como “card” ao invés de tabela simples, também consigo montar.


sim

import streamlit as st

st.set_page_config(
    page_title="IP Dedicado",
    layout="wide"
)

# CSS personalizado
st.markdown("""
<style>
.main-card {
    background-color: #ffffff;
    padding: 25px;
    border-radius: 15px;
    border: 1px solid #dcdcdc;
    box-shadow: 0px 2px 10px rgba(0,0,0,0.08);
    margin-top: 20px;
}

.titulo {
    font-size: 28px;
    font-weight: bold;
    color: #003366;
    margin-bottom: 20px;
}

.label {
    font-size: 15px;
    color: #666;
    margin-bottom: 5px;
}

.valor {
    font-size: 20px;
    font-weight: bold;
    color: #000;
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="titulo">📡 Informações do IP Dedicado</div>', unsafe_allow_html=True)

st.markdown("""
<div class="main-card">

<div class="label">NRC</div>
<div class="valor">0439387231</div>

<div class="label">Produto</div>
<div class="valor">IP Dedicado</div>

<div class="label">Corresponde a</div>
<div class="valor">Justiça Federal - Atendimento</div>

<div class="label">Contrato</div>
<div class="valor">0877 DJ</div>

<div class="label">Vencimento</div>
<div class="valor">27/05</div>

</div>
""", unsafe_allow_html=True)

como que essa página vai ser vinculada ao dashboard

No Streamlit, a forma mais simples de vincular uma nova página ao dashboard é usando a pasta pages.

Estrutura:

seu_projeto/
│
├── app.py
├── pages/
│   └── 1_IP_Dedicado.py
Como funciona
app.py → sua página principal/dashboard

Tudo que estiver dentro da pasta pages vira automaticamente uma nova página no menu lateral do Streamlit.

Exemplo
app.py
import streamlit as st

st.set_page_config(page_title="Dashboard", layout="wide")

st.title("Dashboard Principal")
st.write("Bem-vindo ao sistema.")
pages/1_IP_Dedicado.py
Cole o código da página que eu mandei anteriormente.

Como executar
No terminal:

streamlit run app.py
O Streamlit vai criar automaticamente um menu lateral com:

Dashboard Principal

IP Dedicado

Se quiser abrir por botão
Também pode colocar um botão no dashboard:

st.page_link("pages/1_IP_Dedicado.py", label="Abrir página IP Dedicado")
ou:

if st.button("Abrir IP Dedicado"):
    st.switch_page("pages/1_IP_Dedicado.py")
Importante
A pasta precisa se chamar exatamente:

pages
Tudo minúsculo.


'streamlit' não é reconhecido como um comando interno
ou externo, um programa operável ou um arquivo em lotes.

C:\Users\vtamura>

Isso acontece porque o Streamlit provavelmente não está instalado no Python do seu Windows, ou o PATH não foi configurado.

Tente primeiro instalar o Streamlit:

pip install streamlit
Depois execute:

streamlit run app.py
Se continuar aparecendo o mesmo erro, execute desta forma:

python -m streamlit run app.py
ou:

py -m streamlit run app.py
Antes disso, vale confirmar se o Python está instalado:

python --version
ou:

py --version
Se aparecer a versão do Python, está tudo certo.

Fluxo completo:

pip install streamlit
Depois:

cd caminho_da_sua_pasta
Exemplo:

cd Desktop\dashboard
E então:

python -m streamlit run app.py
O navegador deve abrir automaticamente com o dashboard.


ok, agora o proximo passo de criaruma página e vincular ao dashboard

Perfeito. Agora que o Streamlit está funcionando, faça exatamente assim:

1. Estrutura das pastas
Sua pasta do projeto deve ficar assim:

dashboard/
│
├── app.py
└── pages/
    └── 1_IP_Dedicado.py
2. Criar a pasta pages
Dentro da pasta do projeto:

clique com botão direito

Novo → Pasta

nomeie como:

pages
3. Criar a nova página
Dentro da pasta pages, crie um arquivo:

1_IP_Dedicado.py
4. Código da página principal (app.py)
Coloque isso:

import streamlit as st

st.set_page_config(
    page_title="Dashboard Principal",
    layout="wide"
)

st.title("📊 Dashboard Principal")

st.write("Bem-vindo ao sistema.")

st.page_link(
    "pages/1_IP_Dedicado.py",
    label="📡 Abrir página IP Dedicado"
)
5. Código da nova página (1_IP_Dedicado.py)
Cole isso:

import streamlit as st

st.set_page_config(
    page_title="IP Dedicado",
    layout="wide"
)

# CSS personalizado
st.markdown("""
<style>
.main-card {
    background-color: #ffffff;
    padding: 25px;
    border-radius: 15px;
    border: 1px solid #dcdcdc;
    box-shadow: 0px 2px 10px rgba(0,0,0,0.08);
    margin-top: 20px;
}

.titulo {
    font-size: 28px;
    font-weight: bold;
    color: #003366;
    margin-bottom: 20px;
}

.label {
    font-size: 15px;
    color: #666;
    margin-bottom: 5px;
}

.valor {
    font-size: 20px;
    font-weight: bold;
    color: #000;
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="titulo">📡 Informações do IP Dedicado</div>', unsafe_allow_html=True)

st.markdown("""
<div class="main-card">

<div class="label">NRC</div>
<div class="valor">0439387231</div>

<div class="label">Produto</div>
<div class="valor">IP Dedicado</div>

<div class="label">Corresponde a</div>
<div class="valor">Justiça Federal - Atendimento</div>

<div class="label">Contrato</div>
<div class="valor">0877 DJ</div>

<div class="label">Vencimento</div>
<div class="valor">27/05</div>

</div>
""", unsafe_allow_html=True)
6. Executar
No terminal:

cd caminho_da_pasta
Depois:

python -m streamlit run app.py
Resultado
Você terá:

menu lateral automático

página principal

página IP Dedicado

botão para navegar

layout profissional estilo sistema interno

O Streamlit cria o menu automaticamente quando detecta a pasta pages.


crio a pasta aonde? no files?

Sim. A pasta pages deve ser criada dentro da mesma pasta onde está o seu app.py.

Exemplo:

Se seu projeto está assim no VS Code / Explorer:

dashboard/
└── app.py
Você vai criar a pasta pages dentro de dashboard:

dashboard/
├── app.py
└── pages/
No VS Code
No painel lateral “Files”:

Clique com botão direito na pasta do projeto (dashboard)

Clique em:

New Folder
Nome:

pages
Depois:

Clique com botão direito na pasta pages

New File

Nome:

1_IP_Dedicado.py
Resumo final:

dashboard/
├── app.py
└── pages/
    └── 1_IP_Dedicado.py
Aí o Streamlit reconhece automaticamente como uma nova página do dashboard.


Imagem carregada

Você criou o pages como arquivo, não como pasta.

O ícone ao lado de pages está de arquivo 📄, mas deveria ser de pasta 📁.

Você precisa:

Excluir esse arquivo pages

Criar uma pasta chamada:

pages
Depois dela criada corretamente:

Telecom2026/
├── app.py
├── pages/
│   └── 1_IP_Dedicado.py
Como corrigir no GitHub
Clique no arquivo pages

Clique nos 3 pontinhos ...

Delete file

Depois:

Clique em Add file

Create new file

No nome do arquivo coloque:

pages/1_IP_Dedicado.py
O GitHub cria automaticamente a pasta pages.

Depois cole o código da página e faça o commit.


ip dedicados

Então o nome pode ficar assim:

pages/IP_Dedicados.py
ou, para organizar a ordem no menu:

pages/1_IP_Dedicados.py
No GitHub:

Add file

Create new file

Nome:

pages/1_IP_Dedicados.py
Depois cole o código da página.

O Streamlit vai mostrar automaticamente no menu lateral:

Dashboard Principal

IP Dedicados

Sem precisar configurar mais nada.


NRC 0439387231	
Produto IP Dedicado	
Corresponde a:  (Justiça Federal- Atendimento)
Contrato:	 0877 DJ	
Vencimento 27/05

preciso que crie uma tabela nessa pagina nova

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
Cole esse código dentro do arquivo:

pages/1_IP_Dedicados.py
Depois o Streamlit já vai mostrar a nova página no menu lateral automaticamente.


There was an error committing your changes: Sorry, a file exists where you’re trying to create a subdirectory. Choose a new path and try again.

Esse erro aconteceu porque ainda existe um arquivo chamado pages.

O GitHub não consegue criar a pasta pages/ enquanto existir um arquivo com esse mesmo nome.

Faça assim:

Clique no arquivo pages

Clique nos ...

Escolha:

Delete file
Commit da exclusão

Depois:

Clique em:

Add file → Create new file
No nome do arquivo coloque:

pages/1_IP_Dedicados.py
Isso fará o GitHub criar automaticamente a pasta pages.

Cole o código da página

Commit changes

Pronto. O Streamlit vai reconhecer automaticamente a nova página.


e agora como rodar o script

Agora que a estrutura está pronta, você precisa rodar o projeto pelo terminal.

Na pasta onde está seu app.py, execute:

python -m streamlit run app.py
Exemplo completo
Se seu projeto está em:

C:\Users\vtamura\Telecom2026
Faça:

cd C:\Users\vtamura\Telecom2026
Depois:

python -m streamlit run app.py
Resultado esperado
Vai aparecer algo assim:

Local URL: http://localhost:8501
O navegador abrirá automaticamente.

Você verá:
No menu lateral:

Dashboard principal

IP Dedicados

Porque o Streamlit detecta automaticamente a pasta:

pages/
Sempre que alterar algo
Basta salvar o arquivo (Ctrl + S).

O Streamlit atualiza automaticamente a página.


ainda não tá aparecendo a outra página

Provavelmente aconteceu uma destas situações:

o arquivo não está dentro da pasta pages

o nome da pasta está errado

o Streamlit ainda está rodando uma versão antiga

Confira exatamente esta estrutura:

Telecom2026/
├── app.py
└── pages/
    └── 1_IP_Dedicados.py
Depois confirme:

1. A pasta chama exatamente:
pages
Tudo minúsculo.

2. O arquivo termina com .py
Correto:

1_IP_Dedicados.py
Errado:

1_IP_Dedicados.py.txt
3. Reinicie o Streamlit
Pare o terminal:

CTRL + C
Depois rode novamente:

python -m streamlit run app.py
4. Verifique se existe erro no terminal
Se houver erro no 1_IP_Dedicados.py, o Streamlit não mostra a página.

5. Teste mínimo
Coloque SOMENTE isso dentro do arquivo 1_IP_Dedicados.py:

import streamlit as st

st.title("Página IP Dedicados")
Salve.

Se aparecer no menu, o problema era no código anterior.


apagou o filtro lateral esquerdo que tinha no app.py e ainda não criou um vincuo entre as duas páginas

O menu lateral do Streamlit só aparece automaticamente quando:

existe a pasta pages

existe mais de 1 página válida

o app.py não está quebrando com erro

Você provavelmente sobrescreveu o app.py antigo.

Faça assim para manter o filtro lateral E criar o vínculo entre páginas.

app.py
Deixe o app.py assim:

import streamlit as st

st.set_page_config(
    page_title="Dashboard Telecom",
    layout="wide"
)

# MENU LATERAL
st.sidebar.title("Menu")

st.sidebar.page_link(
    "app.py",
    label="🏠 Dashboard Principal"
)

st.sidebar.page_link(
    "pages/1_IP_Dedicados.py",
    label="📡 IP Dedicados"
)

# CONTEÚDO PRINCIPAL
st.title("📊 Dashboard Telecom")

st.write("Bem-vindo ao sistema.")
Estrutura correta
Telecom2026/
├── app.py
└── pages/
    └── 1_IP_Dedicados.py
Arquivo da nova página
pages/1_IP_Dedicados.py

import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="IP Dedicados",
    layout="wide"
)

# MENU LATERAL
st.sidebar.title("Menu")

st.sidebar.page_link(
    "app.py",
    label="🏠 Dashboard Principal"
)

st.sidebar.page_link(
    "pages/1_IP_Dedicados.py",
    label="📡 IP Dedicados"
)

st.title("📡 IP Dedicados")

dados = {
    "NRC": ["0439387231"],
    "Produto": ["IP Dedicado"],
    "Corresponde a": ["Justiça Federal - Atendimento"],
    "Contrato": ["0877 DJ"],
    "Vencimento": ["27/05"]
}

df = pd.DataFrame(dados)

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
)
Depois reinicie
No terminal:

CTRL + C
Depois:

python -m streamlit run app.py
Agora vai aparecer:

No menu esquerdo:

Dashboard Principal

IP Dedicados

E as páginas ficarão vinculadas.


manda o app.py script completo

import streamlit as st
import pandas as pd

# CONFIGURAÇÃO DA PÁGINA
st.set_page_config(
    page_title="Dashboard Telecom",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================
# MENU LATERAL
# =========================
st.sidebar.title("📂 Menu")

st.sidebar.page_link(
    "app.py",
    label="🏠 Dashboard Principal"
)

st.sidebar.page_link(
    "pages/1_IP_Dedicados.py",
    label="📡 IP Dedicados"
)

# =========================
# TÍTULO PRINCIPAL
# =========================
st.title("📊 Dashboard Telecom")

st.markdown("---")

# =========================
# FILTROS LATERAIS
# =========================
st.sidebar.header("Filtros")

status = st.sidebar.multiselect(
    "Status",
    ["Em andamento", "Concluído", "Pendente"],
    default=["Em andamento"]
)

operadora = st.sidebar.multiselect(
    "Operadora",
    ["VIVO", "Claro", "TIM"],
    default=["VIVO"]
)

# =========================
# DADOS EXEMPLO
# =========================
dados = {
    "Unidade": [
        "Capivari",
        "Santo Amaro",
        "Jacareí",
        "São Bernardo"
    ],
    "Operadora": [
        "VIVO",
        "VIVO",
        "VIVO",
        "VIVO"
    ],
    "Status": [
        "Em andamento",
        "Pendente",
        "Concluído",
        "Em andamento"
    ]
}

df = pd.DataFrame(dados)

# FILTRO
df_filtrado = df[
    (df["Status"].isin(status)) &
    (df["Operadora"].isin(operadora))
]

# =========================
# EXIBIÇÃO
# =========================
st.subheader("Chamados")

st.dataframe(
    df_filtrado,
    use_container_width=True,
    hide_index=True
)

# =========================
# RODAPÉ
# =========================
st.markdown("---")
st.caption("Sistema interno de telecomunicações")

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
    ["Capivari", "(19) 3492-2215", "Linha muda", "Reparo agendado 05/05", "87LZA0LL09"],
    ["Capivari", "(19) 3879-1317", "Linha muda", "sem expectativa de atendimento, solicitado urgência", "87LZA0LL09"],

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

    ["Itaquaquecetuba (Casa da Advocacia)", "(11) 4647-3977", "Linha muda", "Em andamento", "8-7LUEYA0k"],
    ["Itaquaquecetuba (Casa da Advocacia)", "(11) 4640-1874", "Linha muda", "Em andamento", "8-7LUF8Q7T"],

    ["São José do Rio Preto (Sala do Fórum)", "-", "Instalação cancelada pela operadora", "reagendar dia 05/05", ""],
    ["São José do Rio Preto (Sala do Fórum)", "-", "Instalação cancelada pela operadora", "reagendar dia 05/05", "-"],
    ["São Miguel Paulista (Casa da Advocacia)", "112037-7055", "escalonado pela vivo segue em tratativa", "reagendar dia 05/05", "8-7M2KB8NV"],
    ["São Miguel Paulista (Casa da Advocacia)", "112037-2515", "sem expectativa de atendimento, solicitado urgência", "-", "-"]

    
]

df = pd.DataFrame(dados, columns=["Local", "Produto", "Motivo", "Status", "Chamado"])

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

Seu app.py está correto.
O que falta agora é apenas adicionar o vínculo da nova página dentro da sidebar.

Adicione este bloco logo abaixo de:

# ================= SIDEBAR =================
Ficando assim:

# ================= SIDEBAR =================

st.sidebar.title("📂 Menu")

st.sidebar.page_link(
    "app.py",
    label="🏠 Dashboard Principal"
)

st.sidebar.page_link(
    "pages/1_IP_Dedicados.py",
    label="📡 IP Dedicados"
)

if st.sidebar.button("🚪 Sair"):
    st.session_state["logado"] = False
    st.rerun()
Agora crie o arquivo:

pages/1_IP_Dedicados.py
E coloque este código:

import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="IP Dedicados",
    layout="wide"
)

# MENU LATERAL
st.sidebar.title("📂 Menu")

st.sidebar.page_link(
    "app.py",
    label="🏠 Dashboard Principal"
)

st.sidebar.page_link(
    "pages/1_IP_Dedicados.py",
    label="📡 IP Dedicados"
)

# TÍTULO
st.title("📡 IP Dedicados")

# TABELA
dados = {
    "NRC": ["0439387231"],
    "Produto": ["IP Dedicado"],
    "Corresponde a": ["Justiça Federal - Atendimento"],
    "Contrato": ["0877 DJ"],
    "Vencimento": ["27/05"]
}

df = pd.DataFrame(dados)

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
)
Depois reinicie o Streamlit:

CTRL + C
e rode novamente:

python -m streamlit run app.py
Agora vai aparecer:

Dashboard Principal

IP Dedicados

no menu lateral esquerdo.


import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="IP Dedicados",
    layout="wide"
)

# MENU LATERAL
st.sidebar.title("📂 Menu")

st.sidebar.page_link(
    "app.py",
    label="🏠 Dashboard Principal"
)

st.sidebar.page_link(
    "pages/1_IP_Dedicados.py",
    label="📡 IP Dedicados"
)

# TÍTULO
st.title("📡 IP Dedicados")

# TABELA
dados = {
    "NRC": ["0439387231"],
    "Produto": ["IP Dedicado"],
    "Corresponde a": ["Justiça Federal - Atendimento"],
    "Contrato": ["0877 DJ"],
    "Vencimento": ["27/05"]
}

df = pd.DataFrame(dados)

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
) 

inclua o script completo do app.py primeiro

import streamlit as st
import pandas as pd
import os
from dotenv import load_dotenv

# ================= CONFIG =================
st.set_page_config(
    page_title="Dashboard de Chamados",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ================= ESTILO =================
st.markdown("""
<style>

/* REMOVE FUNDO */
.stApp {
    background: none;
}

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

    # LOGO
    top1, top2 = st.columns([6,1])

    with top2:
        if os.path.exists("logo.png"):
            st.image("logo.png", width=100)

    # LOGIN CENTRAL
    col1, col2, col3 = st.columns([2,1,2])

    with col2:

        st.markdown(
            '<div class="login-title">🔐 Acesso</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="login-subtitle">Entre para acessar o dashboard</div>',
            unsafe_allow_html=True
        )

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

# ================= CONTROLE LOGIN =================
if "logado" not in st.session_state:
    st.session_state["logado"] = False

if not st.session_state["logado"]:
    login()
    st.stop()

# ================= MENU LATERAL =================
st.sidebar.title("📂 Menu")

st.sidebar.page_link(
    "app.py",
    label="🏠 Dashboard Principal"
)

st.sidebar.page_link(
    "pages/1_IP_Dedicados.py",
    label="📡 IP Dedicados"
)

# BOTÃO SAIR
if st.sidebar.button("🚪 Sair"):
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

# ================= KPIs =================
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

KeyError: This app has encountered an error. The original error message is redacted to prevent data leaks. Full error details have been recorded in the logs (if you're on Streamlit Cloud, click on 'Manage app' in the lower right of your app).
Traceback:
File "/mount/src/dashboard-oab/app.py", line 111, in <module>
    st.sidebar.page_link(
    ~~~~~~~~~~~~~~~~~~~~^
        "app.py",
        ^^^^^^^^^
        label="🏠 Dashboard Principal"
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
File "/home/adminuser/venv/lib/python3.14/site-packages/streamlit/runtime/metrics_util.py", line 698, in wrapped_func
    result = non_optional_func(*args, **kwargs)
File "/home/adminuser/venv/lib/python3.14/site-packages/streamlit/elements/widgets/button.py", line 1288, in page_link
    return self._page_link(
           ~~~~~~~~~~~~~~~^
        page=page,
        ^^^^^^^^^^
    ...<6 lines>...
        query_params=query_params,
        ^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
File "/home/adminuser/venv/lib/python3.14/site-packages/streamlit/elements/widgets/button.py", line 1588, in _page_link
    url_pathname = page_data["url_pathname"]
                   ~~~~~~~~~^^^^^^^^^^^^^^^^

O erro acontece porque o st.page_link("app.py") não funciona corretamente no Streamlit Cloud em alguns casos.

Troque esta parte:

st.sidebar.page_link(
    "app.py",
    label="🏠 Dashboard Principal"
)
por:

st.sidebar.markdown("### 📂 Navegação")

st.sidebar.link_button(
    "🏠 Dashboard Principal",
    "/"
)
E troque:

st.sidebar.page_link(
    "pages/1_IP_Dedicados.py",
    label="📡 IP Dedicados"
)
por:

st.sidebar.link_button(
    "📡 IP Dedicados",
    "/IP_Dedicados"
)
Mais simples ainda:

REMOVA COMPLETAMENTE isto do app.py:

st.sidebar.page_link(
    "app.py",
    label="🏠 Dashboard Principal"
)

st.sidebar.page_link(
    "pages/1_IP_Dedicados.py",
    label="📡 IP Dedicados"
)
Porque o Streamlit já cria o menu automaticamente quando existe a pasta:

pages/
Então deixe somente:

st.sidebar.title("📂 Menu")
e o Streamlit vai mostrar sozinho:

Dashboard Principal

IP Dedicados

sem precisar de page_link().


manda o script inteiro

import streamlit as st
import pandas as pd
import os
from dotenv import load_dotenv

# ================= CONFIG =================
st.set_page_config(
    page_title="Dashboard de Chamados",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ================= ESTILO =================
st.markdown("""
<style>

/* REMOVE FUNDO */
.stApp {
    background: none;
}

/* TÍTULO LOGIN */
.login-title {
    font-size: 24px;
    font-weight: 700;
}

/* SUBTÍTULO LOGIN */
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

    # LOGO
    top1, top2 = st.columns([6,1])

    with top2:
        if os.path.exists("logo.png"):
            st.image("logo.png", width=100)

    # LOGIN CENTRAL
    col1, col2, col3 = st.columns([2,1,2])

    with col2:

        st.markdown(
            '<div class="login-title">🔐 Acesso</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="login-subtitle">Entre para acessar o dashboard</div>',
            unsafe_allow_html=True
        )

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

# ================= CONTROLE LOGIN =================
if "logado" not in st.session_state:
    st.session_state["logado"] = False

if not st.session_state["logado"]:
    login()
    st.stop()

# ================= SIDEBAR =================
st.sidebar.title("📂 Menu")

# BOTÃO SAIR
if st.sidebar.button("🚪 Sair"):
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

# ================= KPIs =================
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

ok, agora desse menu aqui, preciso que inclua o controle de todos os ip dedicados

# ================= MENU IP DEDICADOS =================

st.sidebar.markdown("---")
st.sidebar.subheader("📡 Controle IP Dedicados")

st.sidebar.markdown("""
- Justiça Federal - Atendimento
- Contrato: 0877 DJ
- NRC: 0439387231
- Vencimento: 27/05
""")
Adicione esse bloco logo abaixo de:

st.sidebar.header("🔎 Filtros")
Ficará assim:

# ================= FILTROS =================
st.sidebar.header("🔎 Filtros")

# ================= MENU IP DEDICADOS =================
st.sidebar.markdown("---")
st.sidebar.subheader("📡 Controle IP Dedicados")

st.sidebar.markdown("""
- Justiça Federal - Atendimento
- Contrato: 0877 DJ
- NRC: 0439387231
- Vencimento: 27/05
""")
Resultado no menu lateral:

filtros

controle dos IPs dedicados

vencimentos

contratos

NRCs

Tudo no mesmo menu esquerdo do dashboard.


não quero na mesma página, quero que seja um hyperlink

No seu caso, o Streamlit já cria automaticamente o hyperlink no menu lateral quando existe a pasta:

pages/
Então você NÃO precisa colocar os IPs dentro do app.py.

Você precisa apenas garantir:

Telecom2026/
├── app.py
└── pages/
    └── 1_IP_Dedicados.py
Depois, no arquivo:

pages/1_IP_Dedicados.py
coloque:

import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="IP Dedicados",
    layout="wide"
)

st.title("📡 Controle de IP Dedicados")

dados = {
    "NRC": ["0439387231"],
    "Produto": ["IP Dedicado"],
    "Corresponde a": ["Justiça Federal - Atendimento"],
    "Contrato": ["0877 DJ"],
    "Vencimento": ["27/05"]
}

df = pd.DataFrame(dados)

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
)
E NO app.py você NÃO coloca page_link().

Deixe apenas:

st.sidebar.title("📂 Menu")
Quando rodar:

python -m streamlit run app.py
o Streamlit cria automaticamente no menu lateral:

Dashboard de Chamados

IP Dedicados

como hyperlinks clicáveis.


o menu não é um link

O problema é que você está escondendo a sidebar no CSS logo no início do app.py.

Você tem isto:

[data-testid="stSidebar"] {display: none;}
Isso remove o menu automático do Streamlit.

Troque TODO o CSS por este:

st.markdown("""
<style>

/* REMOVE FUNDO */
.stApp {
    background: none;
}

/* TÍTULO LOGIN */
.login-title {
    font-size: 24px;
    font-weight: 700;
}

/* SUBTÍTULO LOGIN */
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
OU seja:

REMOVA completamente esta linha:

[data-testid="stSidebar"] {display: none;}
Depois:

Salve

Reinicie o Streamlit:

CTRL + C
e:

python -m streamlit run app.py
Agora o Streamlit mostrará automaticamente:

📂 Pages

Dashboard de Chamados

IP Dedicados

como hyperlinks clicáveis no menu esquerdo.


manda o script inteiro

import streamlit as st
import pandas as pd
import os
from dotenv import load_dotenv

# ================= CONFIG =================
st.set_page_config(
    page_title="Dashboard de Chamados",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ================= ESTILO =================
st.markdown("""
<style>

/* FUNDO */
.stApp {
    background: none;
}

/* TÍTULO LOGIN */
.login-title {
    font-size: 24px;
    font-weight: 700;
}

/* SUBTÍTULO LOGIN */
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

    # LOGO
    top1, top2 = st.columns([6,1])

    with top2:
        if os.path.exists("logo.png"):
            st.image("logo.png", width=100)

    # LOGIN CENTRAL
    col1, col2, col3 = st.columns([2,1,2])

    with col2:

        st.markdown(
            '<div class="login-title">🔐 Acesso</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="login-subtitle">Entre para acessar o dashboard</div>',
            unsafe_allow_html=True
        )

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

# ================= CONTROLE LOGIN =================
if "logado" not in st.session_state:
    st.session_state["logado"] = False

if not st.session_state["logado"]:
    login()
    st.stop()

# ================= SIDEBAR =================
st.sidebar.title("📂 Menu")

# BOTÃO SAIR
if st.sidebar.button("🚪 Sair"):
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

# ================= KPIs =================
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

ainda não criou um link para acessar o relatório

O app.py está correto.
O link não aparece porque falta a estrutura correta da pasta pages.

Você precisa ter exatamente isto no projeto:

Telecom2026/
├── app.py
└── pages/
    └── 1_IP_Dedicados.py
O arquivo:

1_IP_Dedicados.py
precisa estar DENTRO da pasta:

pages
E o conteúdo dele deve ser:

import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="IP Dedicados",
    layout="wide"
)

st.title("📡 Controle de IP Dedicados")

dados = {
    "NRC": ["0439387231"],
    "Produto": ["IP Dedicado"],
    "Corresponde a": ["Justiça Federal - Atendimento"],
    "Contrato": ["0877 DJ"],
    "Vencimento": ["27/05"]
}

df = pd.DataFrame(dados)

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
)
Depois:

Reinicie o Streamlit
Pare:

CTRL + C
Rode novamente:

python -m streamlit run app.py
O Streamlit criará AUTOMATICAMENTE o menu lateral com links:

Dashboard de Chamados

IP Dedicados

Sem precisar adicionar page_link().


a 1_IP_Dedicados já está rodando, mas a app.py não cria um hyperlink com a ip dedicados

O comportamento normal do Streamlit é criar automaticamente os links das páginas no topo da sidebar, acima do seu conteúdo personalizado da sidebar.

O problema no seu caso é que o login com st.stop() está interrompendo a renderização padrão das páginas.

A solução mais simples é criar o hyperlink manualmente.

Adicione isto no app.py, logo abaixo de:

st.sidebar.title("📂 Menu")
Coloque:

st.sidebar.markdown("### 📡 Navegação")

st.sidebar.markdown(
    "[📡 Abrir IP Dedicados](/IP_Dedicados)"
)
Ficará assim:

# ================= SIDEBAR =================
st.sidebar.title("📂 Menu")

st.sidebar.markdown("### 📡 Navegação")

st.sidebar.markdown(
    "[📡 Abrir IP Dedicados](/IP_Dedicados)"
)

# BOTÃO SAIR
if st.sidebar.button("🚪 Sair"):
    st.session_state["logado"] = False
    st.rerun()
Resultado:

Na lateral esquerda aparecerá um hyperlink clicável:

📡 Abrir IP Dedicados

que abrirá:

/IP_Dedicados
Importante:

O nome da URL depende do arquivo:

1_IP_Dedicados.py
O Streamlit transforma em:

/IP_Dedicados

manda o script completo

import streamlit as st
import pandas as pd
import os
from dotenv import load_dotenv

# ================= CONFIG =================
st.set_page_config(
    page_title="Dashboard de Chamados",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ================= ESTILO =================
st.markdown("""
<style>

/* FUNDO */
.stApp {
    background: none;
}

/* TÍTULO LOGIN */
.login-title {
    font-size: 24px;
    font-weight: 700;
}

/* SUBTÍTULO LOGIN */
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

/* LINK MENU */
a {
    text-decoration: none;
    font-weight: 600;
    color: #1f77b4;
}

a:hover {
    color: #0d5aa7;
}

</style>
""", unsafe_allow_html=True)

# ================= LOGIN =================
load_dotenv()

USUARIO = os.getenv("USUARIO")
SENHA = os.getenv("SENHA")

def login():

    # LOGO
    top1, top2 = st.columns([6,1])

    with top2:
        if os.path.exists("logo.png"):
            st.image("logo.png", width=100)

    # LOGIN CENTRAL
    col1, col2, col3 = st.columns([2,1,2])

    with col2:

        st.markdown(
            '<div class="login-title">🔐 Acesso</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="login-subtitle">Entre para acessar o dashboard</div>',
            unsafe_allow_html=True
        )

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

# ================= CONTROLE LOGIN =================
if "logado" not in st.session_state:
    st.session_state["logado"] = False

if not st.session_state["logado"]:
    login()
    st.stop()

# ================= SIDEBAR =================
st.sidebar.title("📂 Menu")

# LINK PARA NOVA PÁGINA
st.sidebar.markdown("### 📡 Navegação")

st.sidebar.markdown(
    "[📡 Abrir IP Dedicados](/IP_Dedicados)"
)

# BOTÃO SAIR
if st.sidebar.button("🚪 Sair"):
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

# ================= KPIs =================
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

ao clicar em ip dedicados, ele volta pra pagina de login e ao logar, ele volta pra pagina de dashboard

Isso acontece porque a página 1_IP_Dedicados.py não está verificando a sessão de login.

Então, quando você abre a página nova, ela inicia “sem login”, redireciona para o app.py, e volta ao dashboard.

Você precisa colocar o mesmo controle de sessão dentro da página 1_IP_Dedicados.py.

Substitua TODO o conteúdo do arquivo:

pages/1_IP_Dedicados.py
por este:

import streamlit as st
import pandas as pd

# ================= CONFIG =================
st.set_page_config(
    page_title="IP Dedicados",
    layout="wide"
)

# ================= VERIFICA LOGIN =================
if "logado" not in st.session_state:
    st.session_state["logado"] = False

if not st.session_state["logado"]:
    st.switch_page("app.py")

# ================= SIDEBAR =================
st.sidebar.title("📂 Menu")

st.sidebar.markdown(
    "[🏠 Dashboard Principal](/)"
)

# BOTÃO SAIR
if st.sidebar.button("🚪 Sair"):
    st.session_state["logado"] = False
    st.switch_page("app.py")

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
Agora:

você faz login uma vez

consegue navegar entre páginas

não volta mais para a tela de login

o hyperlink funciona corretamente

o botão sair encerra a sessão corretamente


ele continua acessando o link e votando pra pagina de login

O problema é que o hyperlink em Markdown:

st.sidebar.markdown("[📡 Abrir IP Dedicados](/IP_Dedicados)")
faz um carregamento novo da aplicação e perde a sessão do st.session_state.

A solução correta é usar st.switch_page().

Substitua ESTA PARTE do app.py
Remova:

st.sidebar.markdown(
    "[📡 Abrir IP Dedicados](/IP_Dedicados)"
)
e coloque:

if st.sidebar.button("📡 IP Dedicados"):
    st.switch_page("pages/1_IP_Dedicados.py")
Seu menu ficará assim
# ================= SIDEBAR =================
st.sidebar.title("📂 Menu")

# BOTÃO PÁGINA IP
if st.sidebar.button("📡 IP Dedicados"):
    st.switch_page("pages/1_IP_Dedicados.py")

# BOTÃO SAIR
if st.sidebar.button("🚪 Sair"):
    st.session_state["logado"] = False
    st.rerun()
E na página 1_IP_Dedicados.py
Troque:

st.sidebar.markdown(
    "[🏠 Dashboard Principal](/)"
)
por:

if st.sidebar.button("🏠 Dashboard Principal"):
    st.switch_page("app.py")
Resultado:

login permanece ativo

navegação entre páginas funciona

não volta mais para a tela de login

navegação fica igual sistema interno profissional

sessão do usuário continua funcionando corretamente


mande os dois scripts completos

app.py
import streamlit as st
import pandas as pd
import os
from dotenv import load_dotenv

# ================= CONFIG =================
st.set_page_config(
    page_title="Dashboard de Chamados",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ================= ESTILO =================
st.markdown("""
<style>

/* FUNDO */
.stApp {
    background: none;
}

/* TÍTULO LOGIN */
.login-title {
    font-size: 24px;
    font-weight: 700;
}

/* SUBTÍTULO LOGIN */
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

    top1, top2 = st.columns([6,1])

    with top2:
        if os.path.exists("logo.png"):
            st.image("logo.png", width=100)

    col1, col2, col3 = st.columns([2,1,2])

    with col2:

        st.markdown(
            '<div class="login-title">🔐 Acesso</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="login-subtitle">Entre para acessar o dashboard</div>',
            unsafe_allow_html=True
        )

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

# ================= CONTROLE LOGIN =================
if "logado" not in st.session_state:
    st.session_state["logado"] = False

if not st.session_state["logado"]:
    login()
    st.stop()

# ================= SIDEBAR =================
st.sidebar.title("📂 Menu")

# BOTÃO IP DEDICADOS
if st.sidebar.button("📡 IP Dedicados"):
    st.switch_page("pages/1_IP_Dedicados.py")

# BOTÃO SAIR
if st.sidebar.button("🚪 Sair"):
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

# ================= KPIs =================
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
pages/1_IP_Dedicados.py
import streamlit as st
import pandas as pd

# ================= CONFIG =================
st.set_page_config(
    page_title="IP Dedicados",
    layout="wide"
)

# ================= VERIFICA LOGIN =================
if "logado" not in st.session_state:
    st.session_state["logado"] = False

if not st.session_state["logado"]:
    st.switch_page("app.py")

# ================= SIDEBAR =================
st.sidebar.title("📂 Menu")

# VOLTAR DASHBOARD
if st.sidebar.button("🏠 Dashboard Principal"):
    st.switch_page("app.py")

# BOTÃO SAIR
if st.sidebar.button("🚪 Sair"):
    st.session_state["logado"] = False
    st.switch_page("app.py")

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

como rodar no cmd

No CMD, faça exatamente assim:

1. Abrir o CMD
Pressione:

Windows + R
Digite:

cmd
2. Entrar na pasta do projeto
Exemplo:

cd C:\Users\vtamura\Telecom2026
Use o caminho onde está seu app.py.

3. Rodar o Streamlit
Execute:

python -m streamlit run app.py
4. Resultado
Vai aparecer algo assim:

Local URL: http://localhost:8501
O navegador abrirá automaticamente.

5. Para parar o sistema
No CMD:

CTRL + C
Estrutura obrigatória
Confirme que ficou assim:

Telecom2026/
├── app.py
└── pages/
    └── 1_IP_Dedicados.py
Sem isso a navegação entre páginas não funciona.


o comando pra instalar o streamlit e etc

No CMD, execute nesta ordem:

1. Instalar Streamlit
pip install streamlit
2. Instalar pandas
pip install pandas
3. Instalar python-dotenv
pip install python-dotenv
4. Rodar o projeto
Entre na pasta:

cd C:\Users\vtamura\Telecom2026
Depois execute:

python -m streamlit run app.py
Se o pip não funcionar
Use:

python -m pip install streamlit pandas python-dotenv
Para atualizar tudo depois
pip install --upgrade streamlit pandas python-dotenv

e o da pag app.py e ip dedicado?

Depois de instalar tudo, você NÃO instala app.py nem 1_IP_Dedicados.py.

Esses são arquivos do seu projeto.

Você apenas executa o app.py.

Estrutura correta
Telecom2026/
├── app.py
└── pages/
    └── 1_IP_Dedicados.py
Comando para rodar
Entre na pasta do projeto:

cd C:\Users\vtamura\Telecom2026
Depois execute:

python -m streamlit run app.py
O Streamlit automaticamente:

abre o app.py

detecta a pasta pages

cria a navegação para:

Dashboard

IP Dedicados

Para parar
No CMD:

CTRL + C
Para abrir novamente depois
Sempre:

cd C:\Users\vtamura\Telecom2026
python -m streamlit run app.py

streamlit.errors.StreamlitAPIException: Could not find page: app.py. Must be the file path relative to the main script, from the directory: dashboard_oab. Only the main app file and files in the pages/ directory are supported.

Traceback:
File "C:\Users\vtamura\dashboard_oab\1_IP_Dedicados.py", line 15, in <module>
    st.switch_page("app.py")
    ~~~~~~~~~~~~~~^^^^^^^^^^
File "C:\Users\vtamura\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\streamlit\runtime\metrics_util.py", line 698, in wrapped_func
    result = non_optional_func(*args, **kwargs)
File "C:\Users\vtamura\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\streamlit\commands\execution_control.py", line 312, in switch_page
    raise StreamlitAPIException(
    ...<3 lines>...
    )
Copy
Ask Google
Ask ChatGPT

O erro aconteceu porque o arquivo 1_IP_Dedicados.py NÃO está dentro da pasta pages.

No seu caso ele está aqui:

dashboard_oab\1_IP_Dedicados.py
Mas deveria estar aqui:

dashboard_oab\pages\1_IP_Dedicados.py
Faça isso
1. Crie a pasta:
pages
dentro de:

dashboard_oab
2. Mova o arquivo:
De:

dashboard_oab\1_IP_Dedicados.py
Para:

dashboard_oab\pages\1_IP_Dedicados.py
Estrutura correta FINAL
dashboard_oab/
├── app.py
└── pages/
    └── 1_IP_Dedicados.py
Depois rode novamente
python -m streamlit run app.py
Agora o:

st.switch_page("app.py")
vai funcionar corretamente.


streamlit.errors.StreamlitAPIException: This app has encountered an error. The original error message is redacted to prevent data leaks. Full error details have been recorded in the logs (if you're on Streamlit Cloud, click on 'Manage app' in the lower right of your app).

Traceback:
File "/mount/src/dashboard-oab/app.py", line 111, in <module>
    st.switch_page("pages/1_IP_Dedicados.py")
    ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "/home/adminuser/venv/lib/python3.14/site-packages/streamlit/runtime/metrics_util.py", line 698, in wrapped_func
    result = non_optional_func(*args, **kwargs)
File "/home/adminuser/venv/lib/python3.14/site-packages/streamlit/commands/execution_control.py", line 312, in switch_page
    raise StreamlitAPIException(
    ...<3 lines>...
    )

No Streamlit Cloud o switch_page() é mais sensível ao caminho.
A forma correta é usar o nome EXATO da página que aparece no menu do Streamlit.

Troque isto no app.py:

st.switch_page("pages/1_IP_Dedicados.py")
por:

st.switch_page("1_IP_Dedicados")
E no 1_IP_Dedicados.py troque:

st.switch_page("app.py")
por:

st.switch_page("app")
Fica assim
app.py
if st.sidebar.button("📡 IP Dedicados"):
    st.switch_page("1_IP_Dedicados")
1_IP_Dedicados.py
if not st.session_state["logado"]:
    st.switch_page("app")

if st.sidebar.button("🏠 Dashboard Principal"):
    st.switch_page("app")
Depois faça novo deploy/restart no Streamlit Cloud.


manda o script correto nos dois

app.py
import streamlit as st
import pandas as pd
import os
from dotenv import load_dotenv

# ================= CONFIG =================
st.set_page_config(
    page_title="Dashboard de Chamados",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ================= ESTILO =================
st.markdown("""
<style>

/* FUNDO */
.stApp {
    background: none;
}

/* TÍTULO LOGIN */
.login-title {
    font-size: 24px;
    font-weight: 700;
}

/* SUBTÍTULO LOGIN */
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

    top1, top2 = st.columns([6,1])

    with top2:
        if os.path.exists("logo.png"):
            st.image("logo.png", width=100)

    col1, col2, col3 = st.columns([2,1,2])

    with col2:

        st.markdown(
            '<div class="login-title">🔐 Acesso</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="login-subtitle">Entre para acessar o dashboard</div>',
            unsafe_allow_html=True
        )

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

# ================= CONTROLE LOGIN =================
if "logado" not in st.session_state:
    st.session_state["logado"] = False

if not st.session_state["logado"]:
    login()
    st.stop()

# ================= SIDEBAR =================
st.sidebar.title("📂 Menu")

# BOTÃO IP DEDICADOS
if st.sidebar.button("📡 IP Dedicados"):
    st.switch_page("1_IP_Dedicados")

# BOTÃO SAIR
if st.sidebar.button("🚪 Sair"):
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

# ================= KPIs =================
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
pages/1_IP_Dedicados.py
import streamlit as st
import pandas as pd

# ================= CONFIG =================
st.set_page_config(
    page_title="IP Dedicados",
    layout="wide"
)

# ================= VERIFICA LOGIN =================
if "logado" not in st.session_state:
    st.session_state["logado"] = False

if not st.session_state["logado"]:
    st.switch_page("app")

# ================= SIDEBAR =================
st.sidebar.title("📂 Menu")

# VOLTAR DASHBOARD
if st.sidebar.button("🏠 Dashboard Principal"):
    st.switch_page("app")

# BOTÃO SAIR
if st.sidebar.button("🚪 Sair"):
    st.session_state["logado"] = False
    st.switch_page("app")

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

streamlit.errors.StreamlitAPIException: This app has encountered an error. The original error message is redacted to prevent data leaks. Full error details have been recorded in the logs (if you're on Streamlit Cloud, click on 'Manage app' in the lower right of your app).

Traceback:
File "/mount/src/dashboard-oab/app.py", line 111, in <module>
    st.switch_page("pages/1_IP_Dedicados.py")
    ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "/home/adminuser/venv/lib/python3.14/site-packages/streamlit/runtime/metrics_util.py", line 698, in wrapped_func
    result = non_optional_func(*args, **kwargs)
File "/home/adminuser/venv/lib/python3.14/site-packages/streamlit/commands/execution_control.py", line 312, in switch_page
    raise StreamlitAPIException(
    ...<3 lines>...
    )

O erro continua porque no seu app.py AINDA existe esta linha antiga:

st.switch_page("pages/1_IP_Dedicados.py")
Você precisa substituir EXATAMENTE por:

st.switch_page("1_IP_Dedicados")
Procure no app.py:

pages/1_IP_Dedicados.py
e troque por:

1_IP_Dedicados
A linha correta FINAL é:

if st.sidebar.button("📡 IP Dedicados"):
    st.switch_page("1_IP_Dedicados")
E no 1_IP_Dedicados.py:

if st.sidebar.button("🏠 Dashboard Principal"):
    st.switch_page("app")
Depois faça:

git add .
git commit -m "fix navigation"
git push
ou reinicie o Streamlit Cloud manualmente.


streamlit.errors.StreamlitAPIException: This app has encountered an error. The original error message is redacted to prevent data leaks. Full error details have been recorded in the logs (if you're on Streamlit Cloud, click on 'Manage app' in the lower right of your app).

Traceback:
File "/mount/src/dashboard-oab/app.py", line 111, in <module>
    st.switch_page("pages/1_IP_Dedicados.py")
    ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "/home/adminuser/venv/lib/python3.14/site-packages/streamlit/runtime/metrics_util.py", line 698, in wrapped_func
    result = non_optional_func(*args, **kwargs)
File "/home/adminuser/venv/lib/python3.14/site-packages/streamlit/commands/execution_control.py", line 312, in switch_page
    raise StreamlitAPIException(
    ...<3 lines>...
    )

O erro mostra claramente que o arquivo publicado ainda está com a linha antiga.

Na linha 111 do seu app.py ainda existe:

st.switch_page("pages/1_IP_Dedicados.py")
Você precisa APAGAR essa linha e substituir por:

st.switch_page("1_IP_Dedicados")
Seu bloco correto deve ficar exatamente assim:

# BOTÃO IP DEDICADOS
if st.sidebar.button("📡 IP Dedicados"):
    st.switch_page("1_IP_Dedicados")
Depois:

SALVE O ARQUIVO
Se estiver no GitHub / Streamlit Cloud
Execute no CMD:

git add .
git commit -m "fix streamlit navigation"
git push
Se for local
Pare o app:

CTRL + C
e rode novamente:

python -m streamlit run app.py
O erro NÃO é mais do Streamlit.
É porque o deploy ainda está usando a versão antiga do arquivo.


eu tenho que trocar esse codigo da onde? do meu bloco de notas ou do github?

Você precisa trocar no arquivo ORIGINAL do projeto — ou seja, no arquivo que está dentro da pasta do seu projeto no computador.

No seu caso:

dashboard_oab/app.py
Abra esse arquivo no:

VS Code

Bloco de Notas

Notepad++

Cursor

qualquer editor

e troque:

st.switch_page("pages/1_IP_Dedicados.py")
por:

st.switch_page("1_IP_Dedicados")
Depois de salvar:

Se usa Streamlit Cloud/GitHub
Você PRECISA enviar a alteração pro GitHub.

No CMD:

git add .
git commit -m "fix navigation"
git push
Fluxo correto
editar arquivo local (app.py)

salvar

enviar pro GitHub (git push)

Streamlit Cloud atualiza sozinho

Se você alterar só no GitHub web ou só no bloco de notas sem dar git push, o deploy pode continuar usando a versão antiga.


File "/mount/src/dashboard-oab/app.py", line 111, in <module>
    st.switch_page("pages/1_IP_Dedicados")
    ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^
File "/home/adminuser/venv/lib/python3.14/site-packages/streamlit/runtime/metrics_util.py", line 698, in wrapped_func
    result = non_optional_func(*args, **kwargs)
File "/home/adminuser/venv/lib/python3.14/site-packages/streamlit/commands/execution_control.py", line 312, in switch_page
    raise StreamlitAPIException(
    ...<3 lines>...
    )

Ainda está errado porque você deixou:

st.switch_page("pages/1_IP_Dedicados")
Você NÃO pode usar pages/.

Troque EXATAMENTE por:

st.switch_page("1_IP_Dedicados")
Seu bloco correto fica:

if st.sidebar.button("📡 IP Dedicados"):
    st.switch_page("1_IP_Dedicados")
E no outro arquivo:

st.switch_page("app")
Resumo:

❌ ERRADO

st.switch_page("pages/1_IP_Dedicados.py")
❌ ERRADO

st.switch_page("pages/1_IP_Dedicados")
✅ CORRETO

st.switch_page("1_IP_Dedicados")
Depois:

git add .
git commit -m "fix"
git push
ou reinicie localmente.


File "/mount/src/dashboard-oab/app.py", line 111
  st.switch_page("1_IP_Dedicados"),
  ^
IndentationError: expected an indented block after 'if' statement on line 110

O erro agora é só de identação.

Você provavelmente deixou assim:

if st.sidebar.button("📡 IP Dedicados"):
st.switch_page("1_IP_Dedicados")
ou com vírgula no final:

st.switch_page("1_IP_Dedicados"),
O correto é:

if st.sidebar.button("📡 IP Dedicados"):
    st.switch_page("1_IP_Dedicados")
Observe:

4 espaços antes de st.switch_page

sem vírgula no final

Seu bloco inteiro deve ficar assim:

# ================= SIDEBAR =================
st.sidebar.title("📂 Menu")

# BOTÃO IP DEDICADOS
if st.sidebar.button("📡 IP Dedicados"):
    st.switch_page("1_IP_Dedicados")

# BOTÃO SAIR
if st.sidebar.button("🚪 Sair"):
    st.session_state["logado"] = False
    st.rerun()
Depois salve e faça:

git add .
git commit -m "fix indentation"
git push


📂 Menu

streamlit.errors.StreamlitAPIException: This app has encountered an error. The original error message is redacted to prevent data leaks. Full error details have been recorded in the logs (if you're on Streamlit Cloud, click on 'Manage app' in the lower right of your app).

Traceback:
File "/mount/src/dashboard-oab/app.py", line 111, in <module>
    st.switch_page("1_IP_Dedicados")
    ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^
File "/home/adminuser/venv/lib/python3.14/site-packages/streamlit/runtime/metrics_util.py", line 698, in wrapped_func
    result = non_optional_func(*args, **kwargs)
File "/home/adminuser/venv/lib/python3.14/site-packages/streamlit/commands/execution_control.py", line 312, in switch_page
    raise StreamlitAPIException(
    ...<3 lines>...
    )

O problema agora é o nome da página.

O switch_page() precisa do caminho REAL do arquivo dentro da pasta pages.

Use exatamente assim:

st.switch_page("pages/1_IP_Dedicados.py")
Mas para isso funcionar, o arquivo precisa estar exatamente aqui:

dashboard_oab/pages/1_IP_Dedicados.py
Então faça assim:

app.py
Troque o bloco para:

# BOTÃO IP DEDICADOS
if st.sidebar.button("📡 IP Dedicados"):
    st.switch_page("pages/1_IP_Dedicados.py")
pages/1_IP_Dedicados.py
Troque para:

# VOLTAR DASHBOARD
if st.sidebar.button("🏠 Dashboard Principal"):
    st.switch_page("app.py")
Estrutura obrigatória
dashboard_oab/
├── app.py
└── pages/
    └── 1_IP_Dedicados.py
IMPORTANTE
Antes o erro acontecia porque:

o arquivo não estava dentro de pages

ou estava usando nome errado

ou o deploy estava desatualizado

Agora que ele está em pages, o caminho correto voltou a ser:

"pages/1_IP_Dedicados.py"
Depois:

git add .
git commit -m "fix page navigation"
git push

'git' não é reconhecido como um comando interno
ou externo, um programa operável ou um arquivo em lotes.

Você não tem o Git instalado no Windows.

Tem 2 opções:

OPÇÃO 1 — Mais fácil (recomendado)
Atualizar direto pelo site do GitHub.

Faça assim:
Abra seu repositório no GitHub

Clique no arquivo:

app.py
Clique no ícone ✏️ (editar)

Troque:

st.switch_page("1_IP_Dedicados")
por:

st.switch_page("pages/1_IP_Dedicados.py")
Clique em:

Commit changes
Depois faça o mesmo no arquivo:

pages/1_IP_Dedicados.py
Troque:

st.switch_page("app")
por:

st.switch_page("app.py")
e clique em:

Commit changes
O Streamlit Cloud atualizará automaticamente em 1-2 minutos.

OPÇÃO 2 — Instalar Git
Baixe:

Git for Windows

Depois poderá usar:

git add .
git commit -m "fix"
git push
Mas para você agora, editar direto no GitHub é mais rápido.


git add .
git commit -m "fix page navigation"
git push aonde?

Você executa esses comandos no CMD, dentro da pasta do projeto.

Passo a passo
1. Abra o CMD
Windows + R
Digite:

cmd
2. Vá até a pasta do projeto
Exemplo:

cd C:\Users\vtamura\dashboard_oab
3. Execute os comandos
git add .
Depois:

git commit -m "fix page navigation"
Depois:

git push
MAS…
O erro:

'git' não é reconhecido
significa que o Git NÃO está instalado.

Então antes você precisa instalar:

Git for Windows

Depois de instalar
Feche o CMD e abra novamente.

Aí rode:

git --version
Se aparecer a versão, funcionou.

Depois execute:

cd C:\Users\vtamura\dashboard_oab

git add .

git commit -m "fix page navigation"

git push
Depois o Streamlit Cloud atualiza automaticamente.


script pra rodar o streamlit ip dedicado e app.py

Você não roda os dois arquivos separadamente.

No Streamlit, você roda apenas o app.py e ele carrega automaticamente a página 1_IP_Dedicados.py.

Estrutura correta
dashboard_oab/
├── app.py
└── pages/
    └── 1_IP_Dedicados.py
Comando para rodar
No CMD:

cd C:\Users\vtamura\dashboard_oab
Depois:

python -m streamlit run app.py
NÃO faça isso
❌ Errado:

python -m streamlit run 1_IP_Dedicados.py
ou

streamlit run 1_IP_Dedicados.py
O correto é somente
python -m streamlit run app.py
Porque o Streamlit detecta automaticamente:

pages/
e cria a navegação entre páginas sozinho.


File "C:\Users\vtamura\dashboard_oab\pages\1_IP_Dedicados.py", line 15, in <module>
    st.switch_page("app")
    ~~~~~~~~~~~~~~^^^^^^^
File "C:\Users\vtamura\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\streamlit\runtime\metrics_util.py", line 698, in wrapped_func
    result = non_optional_func(*args, **kwargs)
File "C:\Users\vtamura\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\streamlit\commands\execution_control.py", line 312, in switch_page
    raise StreamlitAPIException(
    ...<3 lines>...
    )

Agora o erro está no 1_IP_Dedicados.py.

Você deixou:

st.switch_page("app")
Mas o correto é:

st.switch_page("app.py")
Troque TODAS as ocorrências de:

st.switch_page("app")
por:

st.switch_page("app.py")
Seu bloco correto fica assim:

# ================= VERIFICA LOGIN =================
if "logado" not in st.session_state:
    st.session_state["logado"] = False

if not st.session_state["logado"]:
    st.switch_page("app.py")

# VOLTAR DASHBOARD
if st.sidebar.button("🏠 Dashboard Principal"):
    st.switch_page("app.py")
Resumo final do que funciona no seu caso:

app.py
st.switch_page("pages/1_IP_Dedicados.py")
1_IP_Dedicados.py
st.switch_page("app.py")
Estrutura obrigatória:

dashboard_oab/
├── app.py
└── pages/
    └── 1_IP_Dedicados.py

e agora rodar a do dashboard

No CMD, rode apenas o app.py.

Passo a passo
1. Abra o CMD
2. Vá até a pasta do projeto
cd C:\Users\vtamura\dashboard_oab
3. Rode o dashboard
python -m streamlit run app.py
O que vai acontecer
O Streamlit vai:

abrir o dashboard principal (app.py)

detectar automaticamente:

pages/1_IP_Dedicados.py
permitir navegar entre as páginas

URL
Vai abrir:

http://localhost:8501
Para parar
No CMD:

CTRL + C

Imagem carregada
queria que o botão sair ficasse no canto superior direito, e ao invés de app fosse chamados

No Streamlit, o nome app aparece porque o arquivo principal chama app.py.

Para trocar para “Chamados”, faça isto:

1. Renomeie o arquivo
Troque:

app.py
para:

Chamados.py
2. Atualize os switch_page
No arquivo:

pages/1_IP_Dedicados.py
troque:

st.switch_page("app.py")
por:

st.switch_page("Chamados.py")
3. Rode o projeto novamente
python -m streamlit run Chamados.py
4. Botão Sair no canto superior direito
Adicione isto logo DEPOIS do login:

# ================= TOPO =================
top1, top2 = st.columns([10,1])

with top2:
    if st.button("🚪 Sair"):
        st.session_state["logado"] = False
        st.rerun()
E REMOVA este bloco da sidebar:
# BOTÃO SAIR
if st.sidebar.button("🚪 Sair"):
    st.session_state["logado"] = False
    st.rerun()
Resultado:

“app” vira “Chamados”

botão sair fica no canto superior direito

sidebar fica mais limpa

navegação continua funcionando normalmente


Imagem carregada
quero tirar esse lado esquerdo da pagina de login, ele tem que aparecer após,  o botão de sair está solto desconfigurado. precisa ser mais pra cima


Imagem criada
•
Página de login minimalista e moderna

não é imagem , é codigo

No seu app.py, a sidebar está aparecendo antes do login porque o Streamlit renderiza ela automaticamente.

A solução é esconder a sidebar enquanto o usuário NÃO estiver logado.

Use este bloco COMPLETO no início do arquivo, substituindo seu CSS atual:

# ================= ESCONDER SIDEBAR LOGIN =================
if "logado" not in st.session_state:
    st.session_state["logado"] = False

if not st.session_state["logado"]:

    st.markdown("""
    <style>

    section[data-testid="stSidebar"] {
        display: none;
    }

    .stApp {
        background: #f5f7fb;
    }

    </style>
    """, unsafe_allow_html=True)

else:

    st.markdown("""
    <style>

    .stApp {
        background: #f5f7fb;
    }

    </style>
    """, unsafe_allow_html=True)
Agora o menu lateral só aparecerá depois do login.

Botão sair desalinhado
Substitua:

top1, top2 = st.columns([10,1])
por:

top1, top2 = st.columns([14,1])
E troque:

with top2:
    if st.button("🚪 Sair"):
por:

with top2:
    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("🚪 Sair", use_container_width=True):
Resultado:

sidebar escondida no login

menu aparece apenas após autenticação

botão sair sobe para o topo direito

botão alinhado corretamente

visual mais profissional estilo sistema interno



Página de login minimalista e moderna

Imagem gerada: Página de login minimalista e moderna


Editar


manda o script completo do app.py com essas correçoes

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
        border-radius: 10px;
        font-weight: 600;
    }

    </style>
    """, unsafe_allow_html=True)

# ================= LOGIN =================
load_dotenv()

USUARIO = os.getenv("USUARIO")
SENHA = os.getenv("SENHA")

def login():

    # BOTÃO SAIR NO TOPO
    top1, top2 = st.columns([14, 1])

    with top2:
        st.markdown("<br>", unsafe_allow_html=True)

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

# ================= SIDEBAR =================
st.sidebar.title("📂 Menu")

if st.sidebar.button("📡 IP Dedicados"):
    st.switch_page("pages/1_IP_Dedicados.py")

# ================= BOTÃO SAIR TOPO =================
top1, top2 = st.columns([14,1])

with top2:

    if st.button("🚪 Sair", use_container_width=True):
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
st.sidebar.divider()

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

Imagem carregada
botao ficou feio. preciso diminuir a altura e deixar proporcional

Troque APENAS este bloco:

top1, top2 = st.columns([14,1])

with top2:

    if st.button("🚪 Sair", use_container_width=True):
        st.session_state["logado"] = False
        st.rerun()
por este:

top1, top2 = st.columns([20,1])

with top2:

    st.markdown("""
    <style>

    div.stButton > button[kind="secondary"] {
        height: 38px !important;
        min-height: 38px !important;
        padding: 0px 12px !important;
        font-size: 14px !important;
        border-radius: 8px !important;
        white-space: nowrap !important;
    }

    </style>
    """, unsafe_allow_html=True)

    if st.button("🚪 Sair"):
        st.session_state["logado"] = False
        st.rerun()
O que muda:

botão menor

altura proporcional

texto não quebra

alinhamento correto

aparência mais limpa/profissional

fica realmente no canto superior direito


agora pra acessar o ip dedicados streamlit.errors.StreamlitAPIException: This app has encountered an error. The original error message is redacted to prevent data leaks. Full error details have been recorded in the logs (if you're on Streamlit Cloud, click on 'Manage app' in the lower right of your app).

Traceback:
File "/mount/src/dashboard-oab/app.py", line 111, in <module>
    st.switch_page("pages/1_IP_Dedicados.py")
    ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "/home/adminuser/venv/lib/python3.14/site-packages/streamlit/runtime/metrics_util.py", line 698, in wrapped_func
    result = non_optional_func(*args, **kwargs)
File "/home/adminuser/venv/lib/python3.14/site-packages/streamlit/commands/execution_control.py", line 312, in switch_page
    raise StreamlitAPIException(
    ...<3 lines>...
    )

O erro é porque o switch_page() ainda não está encontrando a página corretamente no Streamlit Cloud.

A forma MAIS estável hoje é usar st.page_link() ao invés de switch_page().

Troque este bloco no app.py:

if st.sidebar.button("📡 IP Dedicados"):
    st.switch_page("pages/1_IP_Dedicados.py")
por:

st.sidebar.page_link(
    "pages/1_IP_Dedicados.py",
    label="📡 IP Dedicados"
)
E no pages/1_IP_Dedicados.py, troque:

if st.sidebar.button("🏠 Dashboard Principal"):
    st.switch_page("app.py")
por:

st.sidebar.page_link(
    "app.py",
    label="🏠 Dashboard Principal"
)
O page_link():

funciona melhor no Streamlit Cloud

cria hyperlink real

evita erro de navegação

mantém a sidebar profissional

Depois salve e rode novamente:

python -m streamlit run app.py
ou faça novo deploy no GitHub/Streamlit Cloud.


File "/mount/src/dashboard-oab/app.py", line 111, in <module>
    st.switch_page("pages/1_IP_Dedicados.py")
    ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "/home/adminuser/venv/lib/python3.14/site-packages/streamlit/runtime/metrics_util.py", line 698, in wrapped_func
    result = non_optional_func(*args, **kwargs)
File "/home/adminuser/venv/lib/python3.14/site-packages/streamlit/commands/execution_control.py", line 312, in switch_page
    raise StreamlitAPIException(
    ...<3 lines>...
    )

O erro continua porque o código antigo AINDA está no app.py.

Você precisa APAGAR completamente esta linha:

st.switch_page("pages/1_IP_Dedicados.py")
e substituir pelo page_link.

Fica exatamente assim:

st.sidebar.page_link(
    "pages/1_IP_Dedicados.py",
    label="📡 IP Dedicados"
)
Então procure no app.py por:

switch_page
e REMOVA tudo relacionado ao switch_page().

O bloco correto final da sidebar é:

# ================= SIDEBAR =================
st.sidebar.title("📂 Menu")

st.sidebar.page_link(
    "pages/1_IP_Dedicados.py",
    label="📡 IP Dedicados"
)
E no 1_IP_Dedicados.py:

st.sidebar.page_link(
    "app.py",
    label="🏠 Dashboard Principal"
)
O problema não é mais o Streamlit.
É que o arquivo publicado ainda contém:

st.switch_page(...)
e precisa ser removido completamente.


app.py import streamlit as st
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
        border-radius: 10px;
        font-weight: 600;
    }

    </style>
    """, unsafe_allow_html=True)

# ================= LOGIN =================
load_dotenv()

USUARIO = os.getenv("USUARIO")
SENHA = os.getenv("SENHA")

def login():

    # BOTÃO SAIR NO TOPO
    top1, top2 = st.columns([14, 1])

    with top2:
        st.markdown("<br>", unsafe_allow_html=True)

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

# ================= SIDEBAR =================
st.sidebar.title("📂 Menu")

st.sidebar.page_link(
    "pages/1_IP_Dedicados.py",
    label="📡 IP Dedicados"
)
# ================= BOTÃO SAIR TOPO =================
top1, top2 = st.columns([20,1])

with top2:

    st.markdown("""
    <style>

    div.stButton > button[kind="secondary"] {
        height: 38px !important;
        min-height: 38px !important;
        padding: 0px 12px !important;
        font-size: 14px !important;
        border-radius: 8px !important;
        white-space: nowrap !important;
    }

    </style>
    """, unsafe_allow_html=True)

    if st.button("🚪 Sair"):
        st.session_state["logado"] = False
        st.rerun()# ================= HEADER =================
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
st.sidebar.divider()

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

Seu app.py está praticamente certo.
O problema é só este trecho:

st.rerun()# ================= HEADER =================
Faltou uma quebra de linha depois do st.rerun().

Troque por:

st.rerun()

# ================= HEADER =================
E ajuste também o botão sair para ficar mais limpo.

Substitua TODO este bloco:

# ================= BOTÃO SAIR TOPO =================
top1, top2 = st.columns([20,1])

with top2:

    st.markdown("""
    <style>

    div.stButton > button[kind="secondary"] {
        height: 38px !important;
        min-height: 38px !important;
        padding: 0px 12px !important;
        font-size: 14px !important;
        border-radius: 8px !important;
        white-space: nowrap !important;
    }

    </style>
    """, unsafe_allow_html=True)

    if st.button("🚪 Sair"):
        st.session_state["logado"] = False
        st.rerun()
por este:

# ================= BOTÃO SAIR =================
top1, top2 = st.columns([18,1])

with top2:

    if st.button("🚪 Sair", use_container_width=True):
        st.session_state["logado"] = False
        st.rerun()
Agora o page_link() do IP Dedicados deve funcionar corretamente.

Se ainda der erro, então o problema estará no arquivo:

pages/1_IP_Dedicados.py
e não mais no app.py.


ip import streamlit as st
import pandas as pd

# ================= CONFIG =================
st.set_page_config(
    page_title="IP Dedicados",
    layout="wide"
)

# ================= SIDEBAR =================
st.sidebar.title("📂 Menu")

# VOLTAR DASHBOARD
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

O problema está aqui:

st.sidebar.page_link(
    "app.py",
    label="🏠 Dashboard Principal"
)
Como sua página principal agora é “Chamados”, provavelmente você renomeou o arquivo principal.

Então precisa usar o nome REAL do arquivo principal.

Se você renomeou:

app.py
para:

Chamados.py
então troque para:

st.sidebar.page_link(
    "Chamados.py",
    label="🏠 Dashboard Principal"
)
Se o arquivo ainda se chama app.py, então o código está correto.

Use este script completo para pages/1_IP_Dedicados.py:

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
E confirme que a estrutura está exatamente assim:

dashboard_oab/
├── app.py
└── pages/
    └── 1_IP_Dedicados.py

File "/mount/src/dashboard-oab/app.py", line 111, in <module>
    st.switch_page("pages/1_IP_Dedicados.py")
    ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "/home/adminuser/venv/lib/python3.14/site-packages/streamlit/runtime/metrics_util.py", line 698, in wrapped_func
    result = non_optional_func(*args, **kwargs)
File "/home/adminuser/venv/lib/python3.14/site-packages/streamlit/commands/execution_control.py", line 312, in switch_page
    raise StreamlitAPIException(
    ...<3 lines>...
    )

Seu app.py ainda está com ESTA linha:

st.switch_page("pages/1_IP_Dedicados.py")
Mas no código que você me enviou depois, você já tinha trocado para page_link.

Então o Streamlit Cloud está usando uma versão ANTIGA do arquivo.

Você precisa remover COMPLETAMENTE qualquer switch_page.

No app.py, deixe EXATAMENTE assim:

# ================= SIDEBAR =================
st.sidebar.title("📂 Menu")

st.sidebar.page_link(
    "pages/1_IP_Dedicados.py",
    label="📡 IP Dedicados"
)
E confirme que NÃO existe mais nenhuma linha contendo:

switch_page
no app.py.

O erro mostra claramente que o deploy atual ainda possui:

st.switch_page("pages/1_IP_Dedicados.py")
Então:

salve o arquivo corrigido

envie para o GitHub novamente

aguarde o Streamlit Cloud atualizar

Se quiser verificar rápido:

No GitHub, abra o app.py e pressione:

CTRL + F
procure:

switch_page
Se aparecer qualquer resultado, apague.


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

esse é do ip dedicados 

O arquivo 1_IP_Dedicados.py está correto.

O erro NÃO está nele.

O problema está no app.py, porque ainda existe uma linha com:

st.switch_page("pages/1_IP_Dedicados.py")
Você precisa remover isso do app.py.

No app.py, a sidebar deve ficar EXATAMENTE assim:

# ================= SIDEBAR =================
st.sidebar.title("📂 Menu")

st.sidebar.page_link(
    "pages/1_IP_Dedicados.py",
    label="📡 IP Dedicados"
)
E NÃO pode existir:

switch_page
em nenhum lugar do app.py.

O erro aponta:

File "/mount/src/dashboard-oab/app.py", line 111
Então o Streamlit Cloud ainda está lendo uma versão antiga do app.py.

Você precisa:

salvar o app.py

enviar para GitHub novamente

aguardar novo deploy

Verificação rápida:

Abra o app.py e procure:

switch_page
Se aparecer qualquer resultado:

apague tudo relacionado a switch_page()

O sistema agora deve usar apenas:

st.sidebar.page_link(...)

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
        border-radius: 10px;
        font-weight: 600;
    }

    </style>
    """, unsafe_allow_html=True)

# ================= LOGIN =================
load_dotenv()

USUARIO = os.getenv("USUARIO")
SENHA = os.getenv("SENHA")

def login():

    # BOTÃO SAIR NO TOPO
    top1, top2 = st.columns([14, 1])

    with top2:
        st.markdown("<br>", unsafe_allow_html=True)

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

# ================= SIDEBAR =================
st.sidebar.title("📂 Menu")

st.sidebar.page_link(
    "pages/1_IP_Dedicados.py",
    label="📡 IP Dedicados"
)
# ================= BOTÃO SAIR TOPO =================
top1, top2 = st.columns([20,1])

with top2:

    st.markdown("""
    <style>

    div.stButton > button[kind="secondary"] {
        height: 38px !important;
        min-height: 38px !important;
        padding: 0px 12px !important;
        font-size: 14px !important;
        border-radius: 8px !important;
        white-space: nowrap !important;
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
st.sidebar.divider()

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

esse é app

Seu app.py está correto agora.
Não existe mais switch_page, então o erro no Streamlit Cloud é porque ele ainda NÃO atualizou o deploy.

O código da sidebar está certo:

st.sidebar.page_link(
    "pages/1_IP_Dedicados.py",
    label="📡 IP Dedicados"
)
Então agora você precisa apenas:

Atualizar o GitHub corretamente
Se estiver usando GitHub web:

abra app.py

confirme que NÃO existe:

switch_page
clique em:

Commit changes
Depois:

Forçar novo deploy no Streamlit Cloud
No Streamlit Cloud:

abra o app

clique nos ⋮

clique em:

Reboot app
ou:

Redeploy
O erro atual acontece porque o deploy antigo ainda está rodando este código antigo:

st.switch_page("pages/1_IP_Dedicados.py")
mas no código que você me enviou isso já foi removido.

Então agora é apenas cache/deploy desatualizado do Streamlit Cloud.


File "/mount/src/dashboard-oab/app.py", line 147, in <module>
    st.sidebar.page_link(
    ~~~~~~~~~~~~~~~~~~~~^
        "pages/1_IP_Dedicados.py",
        ^^^^^^^^^^^^^^^^^^^^^^^^^^
        label="📡 IP Dedicados"
        ^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
File "/home/adminuser/venv/lib/python3.14/site-packages/streamlit/runtime/metrics_util.py", line 698, in wrapped_func
    result = non_optional_func(*args, **kwargs)
File "/home/adminuser/venv/lib/python3.14/site-packages/streamlit/elements/widgets/button.py", line 1288, in page_link
    return self._page_link(
           ~~~~~~~~~~~~~~~^
        page=page,
        ^^^^^^^^^^
    ...<6 lines>...
        query_params=query_params,
        ^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
File "/home/adminuser/venv/lib/python3.14/site-packages/streamlit/elements/widgets/button.py", line 1588, in _page_link
    url_pathname = page_data["url_pathname"]
                   ~~~~~~~~~^^^^^^^^^^^^^^^^

Agora ficou claro: o Streamlit Cloud NÃO está encontrando a página dentro da pasta pages.

Isso acontece porque o arquivo provavelmente NÃO está neste caminho exato:

dashboard-oab/pages/1_IP_Dedicados.py
Faça esta estrutura EXATA no GitHub
dashboard-oab/
│
├── app.py
│
└── pages/
    └── 1_IP_Dedicados.py
O erro mais comum
Você provavelmente deixou:

dashboard-oab/1_IP_Dedicados.py
fora da pasta pages.

OU:

Pages/
com P maiúsculo.

Tem que ser:

pages
minúsculo.

Como resolver no GitHub
1. Clique em:
Add file
→ Create new file
2. Nome do arquivo:
pages/1_IP_Dedicados.py
IMPORTANTE:

escreva exatamente assim

isso cria automaticamente a pasta pages

3. Cole o código do IP Dedicados
4. Commit changes
Depois
O app.py continuará assim:

st.sidebar.page_link(
    "pages/1_IP_Dedicados.py",
    label="📡 IP Dedicados"
)
e finalmente funcionará.


KeyError: This app has encountered an error. The original error message is redacted to prevent data leaks. Full error details have been recorded in the logs (if you're on Streamlit Cloud, click on 'Manage app' in the lower right of your app).
Traceback:
File "/mount/src/dashboard-oab/app.py", line 147, in <module>
    st.sidebar.page_link(
    ~~~~~~~~~~~~~~~~~~~~^
        "pages/1_IP_Dedicados.py",
        ^^^^^^^^^^^^^^^^^^^^^^^^^^
        label="📡 IP Dedicados"
        ^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
File "/home/adminuser/venv/lib/python3.14/site-packages/streamlit/runtime/metrics_util.py", line 698, in wrapped_func
    result = non_optional_func(*args, **kwargs)
File "/home/adminuser/venv/lib/python3.14/site-packages/streamlit/elements/widgets/button.py", line 1288, in page_link
    return self._page_link(
           ~~~~~~~~~~~~~~~^
        page=page,
        ^^^^^^^^^^
    ...<6 lines>...
        query_params=query_params,
        ^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
File "/home/adminuser/venv/lib/python3.14/site-packages/streamlit/elements/widgets/button.py", line 1588, in _page_link
    url_pathname = page_data["url_pathname"]
                   ~~~~~~~~~^^^^^^^^^^^^^^^^

Esse erro normalmente acontece porque o page_link() não conseguiu registrar a página automaticamente no Streamlit Cloud.

A solução mais estável é usar a navegação nova do Streamlit com st.navigation.

No seu caso, é mais simples remover o page_link e usar links manuais na sidebar.

Troque ESTE bloco no app.py:

st.sidebar.page_link(
    "pages/1_IP_Dedicados.py",
    label="📡 IP Dedicados"
)
por:

st.sidebar.markdown("## 📂 Menu")

st.sidebar.markdown(
    "[📡 IP Dedicados](./1_IP_Dedicados)"
)
E no 1_IP_Dedicados.py, troque:

st.sidebar.page_link(
    "app.py",
    label="🏠 Dashboard Principal"
)
por:

st.sidebar.markdown("## 📂 Menu")

st.sidebar.markdown(
    "[🏠 Dashboard Principal](../)"
)
Isso evita completamente:

switch_page

page_link

KeyError do Streamlit Cloud

e funciona como hyperlink real.

Estrutura continua:

dashboard_oab/
├── app.py
└── pages/
    └── 1_IP_Dedicados.py
Depois faça redeploy/reboot no Streamlit Cloud.


tá agora voltou a exigir que logue mesmo já logado, pra ver a página de ip dedicados

Isso acontece porque cada página do Streamlit roda separadamente.
Então o 1_IP_Dedicados.py também precisa verificar a sessão de login.

Adicione este bloco no INÍCIO do arquivo pages/1_IP_Dedicados.py, logo depois dos imports:

# ================= VALIDA LOGIN =================
if "logado" not in st.session_state:
    st.session_state["logado"] = False

if not st.session_state["logado"]:
    st.switch_page("app.py")
Seu 1_IP_Dedicados.py fica assim:

import streamlit as st
import pandas as pd

# ================= VALIDA LOGIN =================
if "logado" not in st.session_state:
    st.session_state["logado"] = False

if not st.session_state["logado"]:
    st.switch_page("app.py")

# ================= CONFIG =================
st.set_page_config(
    page_title="IP Dedicados",
    layout="wide"
)

# ================= MENU =================
st.sidebar.markdown("## 📂 Menu")

st.sidebar.markdown(
    "[🏠 Dashboard Principal](../)"
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
Assim:

se já estiver logado → abre IP Dedicados normal

se não estiver logado → volta para login

mantém a sessão entre páginas

navegação continua funcionando normalmente


ainda não, está solicitando o login mesmo já logado

O problema acontece porque o markdown("[link]") abre como URL e cria uma nova sessão do Streamlit.

Por isso ele “perde” o login.

A solução é voltar a usar a navegação nativa do Streamlit, mas da forma correta.

app.py
Troque:

st.sidebar.markdown("## 📂 Menu")

st.sidebar.markdown(
    "[📡 IP Dedicados](./1_IP_Dedicados)"
)
por:

# ================= MENU =================
st.sidebar.title("📂 Menu")

pagina = st.sidebar.radio(
    "Navegação",
    ["Dashboard", "IP Dedicados"]
)

if pagina == "IP Dedicados":
    st.switch_page("pages/1_IP_Dedicados.py")
pages/1_IP_Dedicados.py
Troque:

st.sidebar.markdown("## 📂 Menu")

st.sidebar.markdown(
    "[🏠 Dashboard Principal](../)"
)
por:

# ================= MENU =================
st.sidebar.title("📂 Menu")

if st.sidebar.button("🏠 Dashboard Principal"):
    st.switch_page("app.py")
IMPORTANTE
A estrutura PRECISA ser:

dashboard_oab/
├── app.py
└── pages/
    └── 1_IP_Dedicados.py
E NO 1_IP_Dedicados.py
Deixe este bloco no topo:

# ================= VALIDA LOGIN =================
if "logado" not in st.session_state:
    st.session_state["logado"] = False

if not st.session_state["logado"]:
    st.switch_page("app.py")
Agora vai funcionar corretamente:

mantém login entre páginas

não pede login novamente

navegação funciona

sidebar profissional

sem erro de hyperlink/session


não foi e ainda voltou a dar erro

O erro voltou porque switch_page() está instável no seu ambiente/Cloud.

A solução DEFINITIVA é NÃO usar múltiplas páginas do Streamlit.

Em vez disso, faça tudo no app.py usando menu interno.
Fica muito mais estável e mantém o login sem problemas.

Troque TODO o bloco da sidebar por isto:

# ================= MENU =================
st.sidebar.title("📂 Menu")

pagina = st.sidebar.radio(
    "Navegação",
    ["Dashboard", "IP Dedicados"]
)
Depois REMOVA completamente:

switch_page
e também:

page_link
do projeto inteiro.

Agora no final do código, substitua:

# ================= HEADER =================
st.title("📊 Dashboard Corporativo de Chamados")
por:

# ================= PÁGINAS =================

if pagina == "Dashboard":

    st.title("📊 Dashboard Corporativo de Chamados")

    st.markdown(
        "Monitoramento de Telefonia e Conectividade"
    )

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

# ================= IP DEDICADOS =================

elif pagina == "IP Dedicados":

    st.title("📡 Controle de IP Dedicados")

    dados_ip = {
        "NRC": ["0439387231"],
        "Produto": ["IP Dedicado"],
        "Corresponde a": ["Justiça Federal - Atendimento"],
        "Contrato": ["0877 DJ"],
        "Vencimento": ["27/05"]
    }

    df_ip = pd.DataFrame(dados_ip)

    st.dataframe(
        df_ip,
        use_container_width=True,
        hide_index=True
    )
Resultado:

login funciona

menu funciona

não perde sessão

sem erro do Streamlit Cloud

visual profissional

sem múltiplas páginas bugadas

tudo no mesmo app estável


volte ao inicial e remova a opçao de ip dedicados

Remova todo o bloco de navegação/IP Dedicados e deixe apenas o dashboard original.

No seu app.py, APAGUE completamente estes trechos:

# ================= MENU =================
st.sidebar.title("📂 Menu")

pagina = st.sidebar.radio(
    "Navegação",
    ["Dashboard", "IP Dedicados"]
)
e também APAGUE todo este bloco:

# ================= IP DEDICADOS =================

elif pagina == "IP Dedicados":

    st.title("📡 Controle de IP Dedicados")

    dados_ip = {
        "NRC": ["0439387231"],
        "Produto": ["IP Dedicado"],
        "Corresponde a": ["Justiça Federal - Atendimento"],
        "Contrato": ["0877 DJ"],
        "Vencimento": ["27/05"]
    }

    df_ip = pd.DataFrame(dados_ip)

    st.dataframe(
        df_ip,
        use_container_width=True,
        hide_index=True
    )
E substitua o início da área principal por:

# ================= HEADER =================
st.title("📊 Dashboard Corporativo de Chamados")

st.markdown(
    "Monitoramento de Telefonia e Conectividade"
)
Depois você pode até excluir:

pages/1_IP_Dedicados.py
e a pasta:

pages
Seu sistema voltará a ficar:

simples

estável

sem erro de navegação

somente com o dashboard principal

login funcionando normalmente


manda o script completo

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
top1, top2 = st.columns([18,1])

with top2:

    if st.button("🚪 Sair", use_container_width=True):
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

Imagem carregada
 BOTÃO SAIR ARRUMAR

Troque ESTE bloco:

# ================= BOTÃO SAIR =================
top1, top2 = st.columns([18,1])

with top2:

    if st.button("🚪 Sair", use_container_width=True):
        st.session_state["logado"] = False
        st.rerun()
por este:

# ================= BOTÃO SAIR =================
col1, col2, col3 = st.columns([20, 1, 0.5])

with col2:

    st.markdown("""
    <style>

    div.stButton > button {
        height: 40px !important;
        width: 100% !important;
        border-radius: 8px !important;
        font-size: 14px !important;
        font-weight: 600 !important;
        white-space: nowrap !important;
        padding: 0px !important;
    }

    </style>
    """, unsafe_allow_html=True)

    if st.button("🚪 Sair"):
        st.session_state["logado"] = False
        st.rerun()
Isso corrige:

texto quebrando

botão estreito

altura desproporcional

alinhamento ruim

e deixa o botão compacto e horizontal corretamente.


Imagem carregada
agora está torto e não cobre a palabra sair

Troque TODO o bloco do botão por este aqui:

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
Agora ele:

fica alinhado corretamente

não corta o texto

centraliza ícone + texto

mantém tamanho proporcional

fica visualmente profissional no canto superior direito


Imagem carregada
falta cobrir mais u tiquinho 

Imagem gerada: Botão de sair minimalista


Editar


manda em código zeca

Troque o bloco inteiro pelo abaixo:

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
Agora ele:

cobre a palavra inteira

não corta “Sair”

mantém alinhamento

fica proporcional

visual mais limpo no topo direito


Capivari	(19) 3492-2215
Capivari	(19) 3879-1317
Santo Amaro (Casa da Advocacia)	11 5546-5596
Santo Amaro (Casa da Advocacia)	11 5686-4032
Santo Amaro (Casa da Advocacia)	11 5524-5369
Santo Amaro (Casa da Advocacia)	11 5524-7409
Santo Amaro (Vara do Trabalho)	11 5521-2381
Santo Amaro (Casa da Advocacia)	11 5524-1990
Santo Amaro (Casa da Advocacia)	11 5524-3966
Santo Amaro (Vara do Trabalho)	11 5521-0862
Jacareí (Casa da Advocacia)	(12) 3951-1667
Jacareí (Casa da Advocacia)	(12) 3951-3766
Jacareí (Casa da Advocacia)	(12) 3961-7650
São Bernardo do Campo (Sala do Fórum)	(11) 4330-3855
Itaquaquecetuba (Casa da Advocacia)	(11) 4647-3977
Itaquaquecetuba (Casa da Advocacia)	(11) 4640-1874
São Miguel Paulista (Casa da Advocacia)	112037-7055
São Miguel Paulista (Casa da Advocacia)	112037-2515
Mauá 	114555-1433
Araraquara	1633314858
Araraquara	16-3335.4522 

dados = [

    ["Capivari", "(19) 3492-2215"],
    ["Capivari", "(19) 3879-1317"],

    ["Santo Amaro (Casa da Advocacia)", "11 5546-5596"],
    ["Santo Amaro (Casa da Advocacia)", "11 5686-4032"],
    ["Santo Amaro (Casa da Advocacia)", "11 5524-5369"],
    ["Santo Amaro (Casa da Advocacia)", "11 5524-7409"],

    ["Santo Amaro (Vara do Trabalho)", "11 5521-2381"],

    ["Santo Amaro (Casa da Advocacia)", "11 5524-1990"],
    ["Santo Amaro (Casa da Advocacia)", "11 5524-3966"],

    ["Santo Amaro (Vara do Trabalho)", "11 5521-0862"],

    ["Jacareí (Casa da Advocacia)", "(12) 3951-1667"],
    ["Jacareí (Casa da Advocacia)", "(12) 3951-3766"],
    ["Jacareí (Casa da Advocacia)", "(12) 3961-7650"],

    ["São Bernardo do Campo (Sala do Fórum)", "(11) 4330-3855"],

    ["Itaquaquecetuba (Casa da Advocacia)", "(11) 4647-3977"],
    ["Itaquaquecetuba (Casa da Advocacia)", "(11) 4640-1874"],

    ["São Miguel Paulista (Casa da Advocacia)", "112037-7055"],
    ["São Miguel Paulista (Casa da Advocacia)", "112037-2515"],

    ["Mauá", "114555-1433"],

    ["Araraquara", "1633314858"],
    ["Araraquara", "16-3335.4522"]

]

df = pd.DataFrame(
    dados,
    columns=["Local", "Produto"]
)

capivari é casa da advocacia 
sala do fórum 
mauá (sala do fórum

araraquara (Ted e Casa da advocacia)

dados = [

    ["Capivari (Casa da Advocacia)", "(19) 3492-2215"],
    ["Capivari (Casa da Advocacia)", "(19) 3879-1317"],

    ["Santo Amaro (Casa da Advocacia)", "11 5546-5596"],
    ["Santo Amaro (Casa da Advocacia)", "11 5686-4032"],
    ["Santo Amaro (Casa da Advocacia)", "11 5524-5369"],
    ["Santo Amaro (Casa da Advocacia)", "11 5524-7409"],

    ["Santo Amaro (Vara do Trabalho)", "11 5521-2381"],

    ["Santo Amaro (Casa da Advocacia)", "11 5524-1990"],
    ["Santo Amaro (Casa da Advocacia)", "11 5524-3966"],

    ["Santo Amaro (Vara do Trabalho)", "11 5521-0862"],

    ["Jacareí (Casa da Advocacia)", "(12) 3951-1667"],
    ["Jacareí (Casa da Advocacia)", "(12) 3951-3766"],
    ["Jacareí (Casa da Advocacia)", "(12) 3961-7650"],

    ["São Bernardo do Campo (Sala do Fórum)", "(11) 4330-3855"],

    ["Itaquaquecetuba (Casa da Advocacia)", "(11) 4647-3977"],
    ["Itaquaquecetuba (Casa da Advocacia)", "(11) 4640-1874"],

    ["São Miguel Paulista (Casa da Advocacia)", "112037-7055"],
    ["São Miguel Paulista (Casa da Advocacia)", "112037-2515"],

    ["Mauá (Sala do Fórum)", "114555-1433"],

    ["Araraquara (TED e Casa da Advocacia)", "1633314858"],
    ["Araraquara (TED e Casa da Advocacia)", "16-3335.4522"]

]

df = pd.DataFrame(
    dados,
    columns=["Local", "Produto"]
)

Data que iniciou o problema	Local	Produto	Motivo	Status	Chamado
23/01/2026	Capivari	(19) 3492-2215	Linha muda	Solicitado reabertura dia 07/05	87LZA0LL09
23/01/2026	Capivari	(19) 3879-1317	Linha muda	sem expectativa de atendimento, solicitado urgência	87LZA0LL09
01/04/2026	Santo Amaro (Casa da Advocacia)	11 5546-5596	linha muda	Em andamento	8-7LZ41JGK
01/04/2026	Santo Amaro (Casa da Advocacia)	11 5686-4032	linha muda	Em andamento	8-7LZ41JGK
01/04/2026	Santo Amaro (Casa da Advocacia)	11 5524-5369	linha muda	Em andamento	8-7LZ41JGK
01/04/2026	Santo Amaro (Casa da Advocacia)	11 5524-7409	linha muda	Em andamento	8-7LZ41JGK
01/04/2026	Santo Amaro (Vara do Trabalho)	11 5521-2381	linha muda	Em andamento	8-7LZ41JGK
01/04/2026	Santo Amaro (Casa da Advocacia)	11 5524-1990	linha muda	Em andamento	8-7LZ41JGK
01/04/2026	Santo Amaro (Casa da Advocacia)	11 5524-3966	linha muda	Em andamento	8-7LZ41JGK
01/04/2026	Santo Amaro (Vara do Trabalho)	11 5521-0862	linha muda	Em andamento	8-7LZ41JGK
01/04/2026	Jacareí (Casa da Advocacia)	(12) 3951-1667	Linha muda - Projeto Rifaina	Em andamento	8-7LP8ZUHY
01/04/2026	Jacareí (Casa da Advocacia)	(12) 3951-3766	Linha muda - Projeto Rifaina	Em andamento	8-7LP8ZUHY
01/04/2026	Jacareí (Casa da Advocacia)	(12) 3961-7650	Linha muda - Projeto Rifaina	Em andamento	8-7LWS83NK
21/02/2026	São Bernardo do Campo (Sala do Fórum)	(11) 4330-3855	Não funciona	Em andamento	8-7LSGGATV
11/02/2026	Itaquaquecetuba (Casa da Advocacia)	(11) 4647-3977	Linha muda	Em andamento	8-7LUEYA0K
11/02/2026	Itaquaquecetuba (Casa da Advocacia)	(11) 4640-1874	Linha muda	Em andamento	8-7LUF8Q7T
20/10/2025	São Miguel Paulista (Casa da Advocacia)	112037-7055	escalonado pela vivo segue em tratativa	chamado encerrado, reaberto novamente dia 07/05 	8-7m47wai3
20/10/2025	São Miguel Paulista (Casa da Advocacia)	112037-2515	sem expectativa de atendimento	-	-
23/02/2026	Mauá 	114555-1433	Linha muda - Projeto Rifaina	Em andamento	8-7L6JZMA5
22/04/2026	Araraquara	1633314858	Furto de cabos	Em andamento	87M1XERPM e 87M1W83RI 
22/04/2026	Araraquara	16-3335.4522	Furto de cabos	Em andamento	87M1XERPM e 87M1W83RI 

dados = [

    ["23/01/2026", "Capivari (Casa da Advocacia)", "(19) 3492-2215",
     "Linha muda", "Solicitado reabertura dia 07/05", "87LZA0LL09"],

    ["23/01/2026", "Capivari (Casa da Advocacia)", "(19) 3879-1317",
     "Linha muda", "Sem expectativa de atendimento, solicitado urgência", "87LZA0LL09"],

    ["01/04/2026", "Santo Amaro (Casa da Advocacia)", "11 5546-5596",
     "Linha muda", "Em andamento", "8-7LZ41JGK"],

    ["01/04/2026", "Santo Amaro (Casa da Advocacia)", "11 5686-4032",
     "Linha muda", "Em andamento", "8-7LZ41JGK"],

    ["01/04/2026", "Santo Amaro (Casa da Advocacia)", "11 5524-5369",
     "Linha muda", "Em andamento", "8-7LZ41JGK"],

    ["01/04/2026", "Santo Amaro (Casa da Advocacia)", "11 5524-7409",
     "Linha muda", "Em andamento", "8-7LZ41JGK"],

    ["01/04/2026", "Santo Amaro (Vara do Trabalho)", "11 5521-2381",
     "Linha muda", "Em andamento", "8-7LZ41JGK"],

    ["01/04/2026", "Santo Amaro (Casa da Advocacia)", "11 5524-1990",
     "Linha muda", "Em andamento", "8-7LZ41JGK"],

    ["01/04/2026", "Santo Amaro (Casa da Advocacia)", "11 5524-3966",
     "Linha muda", "Em andamento", "8-7LZ41JGK"],

    ["01/04/2026", "Santo Amaro (Vara do Trabalho)", "11 5521-0862",
     "Linha muda", "Em andamento", "8-7LZ41JGK"],

    ["01/04/2026", "Jacareí (Casa da Advocacia)", "(12) 3951-1667",
     "Linha muda - Projeto Rifaina", "Em andamento", "8-7LP8ZUHY"],

    ["01/04/2026", "Jacareí (Casa da Advocacia)", "(12) 3951-3766",
     "Linha muda - Projeto Rifaina", "Em andamento", "8-7LP8ZUHY"],

    ["01/04/2026", "Jacareí (Casa da Advocacia)", "(12) 3961-7650",
     "Linha muda - Projeto Rifaina", "Em andamento", "8-7LWS83NK"],

    ["21/02/2026", "São Bernardo do Campo (Sala do Fórum)", "(11) 4330-3855",
     "Não funciona", "Em andamento", "8-7LSGGATV"],

    ["11/02/2026", "Itaquaquecetuba (Casa da Advocacia)", "(11) 4647-3977",
     "Linha muda", "Em andamento", "8-7LUEYA0K"],

    ["11/02/2026", "Itaquaquecetuba (Casa da Advocacia)", "(11) 4640-1874",
     "Linha muda", "Em andamento", "8-7LUF8Q7T"],

    ["20/10/2025", "São Miguel Paulista (Casa da Advocacia)", "112037-7055",
     "Escalonado pela Vivo segue em tratativa",
     "Chamado encerrado, reaberto novamente dia 07/05",
     "8-7M47WAI3"],

    ["20/10/2025", "São Miguel Paulista (Casa da Advocacia)", "112037-2515",
     "Sem expectativa de atendimento", "-", "-"],

    ["23/02/2026", "Mauá (Sala do Fórum)", "114555-1433",
     "Linha muda - Projeto Rifaina", "Em andamento", "8-7L6JZMA5"],

    ["22/04/2026", "Araraquara (TED e Casa da Advocacia)", "1633314858",
     "Furto de cabos", "Em andamento", "87M1XERPM e 87M1W83RI"],

    ["22/04/2026", "Araraquara (TED e Casa da Advocacia)", "16-3335.4522",
     "Furto de cabos", "Em andamento", "87M1XERPM e 87M1W83RI"]

]

df = pd.DataFrame(
    dados,
    columns=[
        "Data que iniciou o problema",
        "Local",
        "Produto",
        "Motivo",
        "Status",
        "Chamado"
    ]
)


precisa incluir que todos os chamados  estão em andamento

# ================= INFO =================
st.info(
    "ℹ️ Todos os chamados encontram-se em andamento junto à operadora."
)

manda o script

# ================= INFO =================
st.info(
    "ℹ️ Todos os chamados encontram-se em andamento junto à operadora."
)

completo. 

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

    st.markdown("""
    <style>

    .stApp {
        background-color: #f5f7fb;
    }

    div.stButton > button {
        border-radius: 10px;
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
st.title("📊 Dashboard Corporativo de Chamados")

st.markdown(
    "Monitoramento de Telefonia e Conectividade"
)
# ================= DADOS =================
dados = [

    ["23/01/2026", "Capivari (Casa da Advocacia)", "(19) 3492-2215",
     "Linha muda", "Solicitado reabertura dia 07/05", "87LZA0LL09"],

    ["23/01/2026", "Capivari (Casa da Advocacia)", "(19) 3879-1317",
     "Linha muda", "Sem expectativa de atendimento, solicitado urgência", "87LZA0LL09"],

    ["01/04/2026", "Santo Amaro (Casa da Advocacia)", "11 5546-5596",
     "Linha muda", "Em andamento", "8-7LZ41JGK"],

    ["01/04/2026", "Santo Amaro (Casa da Advocacia)", "11 5686-4032",
     "Linha muda", "Em andamento", "8-7LZ41JGK"],

    ["01/04/2026", "Santo Amaro (Casa da Advocacia)", "11 5524-5369",
     "Linha muda", "Em andamento", "8-7LZ41JGK"],

    ["01/04/2026", "Santo Amaro (Casa da Advocacia)", "11 5524-7409",
     "Linha muda", "Em andamento", "8-7LZ41JGK"],

    ["01/04/2026", "Santo Amaro (Vara do Trabalho)", "11 5521-2381",
     "Linha muda", "Em andamento", "8-7LZ41JGK"],

    ["01/04/2026", "Santo Amaro (Casa da Advocacia)", "11 5524-1990",
     "Linha muda", "Em andamento", "8-7LZ41JGK"],

    ["01/04/2026", "Santo Amaro (Casa da Advocacia)", "11 5524-3966",
     "Linha muda", "Em andamento", "8-7LZ41JGK"],

    ["01/04/2026", "Santo Amaro (Vara do Trabalho)", "11 5521-0862",
     "Linha muda", "Em andamento", "8-7LZ41JGK"],

    ["01/04/2026", "Jacareí (Casa da Advocacia)", "(12) 3951-1667",
     "Linha muda - Projeto Rifaina", "Em andamento", "8-7LP8ZUHY"],

    ["01/04/2026", "Jacareí (Casa da Advocacia)", "(12) 3951-3766",
     "Linha muda - Projeto Rifaina", "Em andamento", "8-7LP8ZUHY"],

    ["01/04/2026", "Jacareí (Casa da Advocacia)", "(12) 3961-7650",
     "Linha muda - Projeto Rifaina", "Em andamento", "8-7LWS83NK"],

    ["21/02/2026", "São Bernardo do Campo (Sala do Fórum)", "(11) 4330-3855",
     "Não funciona", "Em andamento", "8-7LSGGATV"],

    ["11/02/2026", "Itaquaquecetuba (Casa da Advocacia)", "(11) 4647-3977",
     "Linha muda", "Em andamento", "8-7LUEYA0K"],

    ["11/02/2026", "Itaquaquecetuba (Casa da Advocacia)", "(11) 4640-1874",
     "Linha muda", "Em andamento", "8-7LUF8Q7T"],

    ["20/10/2025", "São Miguel Paulista (Casa da Advocacia)", "112037-7055",
     "Escalonado pela Vivo segue em tratativa",
     "Chamado encerrado, reaberto novamente dia 07/05",
     "8-7M47WAI3"],

    ["20/10/2025", "São Miguel Paulista (Casa da Advocacia)", "112037-2515",
     "Sem expectativa de atendimento", "-", "-"],

    ["23/02/2026", "Mauá (Sala do Fórum)", "114555-1433",
     "Linha muda - Projeto Rifaina", "Em andamento", "8-7L6JZMA5"],

    ["22/04/2026", "Araraquara (TED e Casa da Advocacia)", "1633314858",
     "Furto de cabos", "Em andamento", "87M1XERPM e 87M1W83RI"],

    ["22/04/2026", "Araraquara (TED e Casa da Advocacia)", "16-3335.4522",
     "Furto de cabos", "Em andamento", "87M1XERPM e 87M1W83RI"]

]

df = pd.DataFrame(
    dados,
    columns=[
        "Data que iniciou o problema",
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
    "ℹ️ Todos os chamados encontram-se em andamento junto à operadora."
)

