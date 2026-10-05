import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Expresso Mobilidade",
    layout="wide"
)

dados_rotas = pd.DataFrame({
    "Linha": ["510", "520", "550", "620"],
    "Origem": [
        "Centro",
        "Terminal Norte",
        "Centro",
        "Terminal Sul"
    ],
    "Destino": [
        "Bairro Industrial",
        "Centro",
        "Universidade",
        "Shopping Metropolitano"
    ],
    "Horário": [
        "06:30 - 23:00",
        "05:50 - 22:30",
        "06:00 - 00:00",
        "05:30 - 23:30"
    ],
    "Ônibus": [12, 10, 15, 8]
})

st.title("🚌 Expresso Mobilidade")
st.header("Painel do Operador de Transporte")

st.markdown("""
### Bem-vindo ao painel operacional!

Utilize as ferramentas abaixo para consultar linhas,
selecionar rotas e simular a distribuição da frota.
""")

st.sidebar.title("⚙️ Controle Operacional")

st.sidebar.markdown("""
**Expresso Mobilidade**

Painel para consulta e gerenciamento
das operações de transporte urbano.
""")



st.subheader("👤 Identificação do Operador")

nome = st.text_input("Digite seu nome:")

if nome:
    st.write("Olá,", nome + "! 👋")
    st.success("Operador identificado com sucesso.")

st.subheader("🔎 Consulta de Rota")

linha = st.selectbox(
    "Escolha uma linha prioritária:",
    ["510", "520", "550", "620"]
)

st.write("Linha selecionada:", linha)

rota = dados_rotas[dados_rotas["Linha"] == linha]

st.dataframe(rota, use_container_width=True)
st.subheader("📊 Relatório de Linhas")

linhas = st.multiselect(
    "Escolha as linhas para o relatório:",
    ["510", "520", "550", "620"]
)

if linhas:
    st.write("Linhas selecionadas:", linhas)

    relatorio = dados_rotas[
        dados_rotas["Linha"].isin(linhas)
    ]

    st.dataframe(
        relatorio,
        use_container_width=True
    )

st.subheader("🎛️ Parâmetros Operacionais")

col1, col2, col3 = st.columns(3)

with col1:
    passageiros = st.number_input(
        "Passageiros estimados:",
        min_value=0,
        max_value=5000,
        value=500,
        step=50
    )

with col2:
    demanda = st.slider(
        "Nível de demanda:",
        min_value=0,
        max_value=100,
        value=50
    )

with col3:
    modo = st.radio(
        "Modo de operação:",
        ["Normal", "Horário de pico", "Emergência"]
    )

st.write("Modo selecionado:", modo)

atualizacao = st.checkbox(
    "Ativar atualização operacional"
)

if atualizacao:
    st.info("🔄 Atualização operacional ativada.")

st.subheader("🚍 Distribuição de Frota")

if st.button("Calcular demanda e frota"):

    st.write("⏳ Calculando...")

    if demanda >= 80:
        frota = "Alta"
        mensagem = "É necessário aumentar a quantidade de ônibus."
    elif demanda >= 50:
        frota = "Média"
        mensagem = "A frota atual atende parcialmente à demanda."
    else:
        frota = "Baixa"
        mensagem = "A frota atual é suficiente."

    st.success("✅ Cálculo concluído!")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Passageiros",
            passageiros
        )

    with col2:
        st.metric(
            "Demanda",
            f"{demanda}%"
        )

    with col3:
        st.metric(
            "Frota necessária",
            frota
        )

    st.info(mensagem)

st.subheader("🗺️ Itinerários das Linhas")

st.dataframe(
    dados_rotas,
    use_container_width=True
)

st.subheader("📈 Quantidade de Ônibus por Linha")

grafico = dados_rotas.set_index("Linha")["Ônibus"]

st.bar_chart(grafico)
st.markdown("---")

st.markdown(
    "**Expresso Mobilidade** 🚌 | "
    "Painel Operacional — Atividade 1"
)
