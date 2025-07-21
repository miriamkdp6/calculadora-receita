import streamlit as st

st.set_page_config(page_title="Calculadora de Receita", layout="centered")

st.title("📊 Calculadora de Receita do Cliente")
st.markdown("Ajuste os parâmetros abaixo e veja como isso impacta nos resultados.")

st.subheader("🔧 Parâmetros de entrada")
ticket_medio = st.number_input("Ticket Médio (R$)", value=3000.00, step=100.0, format="%.2f")
leads_mes = st.number_input("Leads por mês", value=11000, step=100)
taxa_qualificacao = st.number_input("Taxa de Qualificação de Lead (%)", value=27.52, step=0.1, format="%.2f") / 100

taxa_conversao = st.number_input("Taxa de Conversão (%)", value=16.71, step=0.1, format="%.2f") / 100
receita_atual = 1517535.36

leads_qualificados = leads_mes * taxa_qualificacao
convertidos = leads_qualificados * taxa_conversao
receita_calculada = convertidos * ticket_medio
receita_incremental = receita_calculada - receita_atual

st.subheader("📈 Resultados Calculados")
st.metric("Leads Qualificados", f"{leads_qualificados:,.0f}")
st.metric("Convertidos", f"{convertidos:,.0f}")
st.metric("Receita Calculada", f"R$ {receita_calculada:,.2f}")
st.metric("Receita Incremental", f"R$ {receita_incremental:,.2f}", delta_color="normal")

st.markdown("---")
st.caption("Calculadora baseada nos dados do cenário atual do cliente.")
