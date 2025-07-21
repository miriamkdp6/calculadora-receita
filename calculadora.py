import streamlit as st

st.set_page_config(page_title="Calculadora de Receita", page_icon="📊", layout="centered")

col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("<div style='display: flex; align-items: center; justify-content: center; height: 120px;'>", unsafe_allow_html=True)
    st.image("https://tse3.mm.bing.net/th/id/OIP.Ap_nLsfv7a8pYhd25rGXYgHaHa?pid=Api", width=150)
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div style='display: flex; align-items: center; justify-content: center; height: 120px;'>", unsafe_allow_html=True)
    st.image("logo_dp6.png", width=120)
    st.markdown("</div>", unsafe_allow_html=True)

st.title("📊 Simulador de Receita do Cliente")
st.markdown("""Ajuste os parâmetros de geração de leads e conversão para simular como mudanças no processo comercial podem impactar a **receita final**.""")

st.subheader("🔧 Parâmetros de entrada")

col1, col2 = st.columns(2)
with col1:
    ticket_medio = st.number_input("🎟️ Ticket Médio (R$)", value=3000.00, step=100.0, format="%.2f")
    taxa_qualificacao = st.number_input("📈 Taxa de Qualificação (%)", value=27.52, step=0.1, format="%.2f") / 100
with col2:
    leads_mes = st.number_input("👥 Leads por mês", value=11000, step=100)
    taxa_conversao = st.number_input("🔄 Taxa de Conversão (%)", value=16.71, step=0.1, format="%.2f") / 100


receita_atual = 1517535.36

leads_qualificados = leads_mes * taxa_qualificacao
convertidos = leads_qualificados * taxa_conversao
receita_calculada = convertidos * ticket_medio
receita_incremental = receita_calculada - receita_atual

st.subheader("📊 Resultados Calculados")

col3, col4 = st.columns(2)
with col3:
    st.metric("✅ Leads Qualificados", f"{leads_qualificados:,.0f}")
    st.metric("💰 Receita Calculada", f"R$ {receita_calculada:,.2f}")
with col4:
    st.metric("🔁 Convertidos", f"{convertidos:,.0f}")
    st.metric("📈 Receita Incremental", f"R$ {receita_incremental:,.2f}", delta_color="normal")

st.markdown("---")
st.caption("Calculadora baseada nos dados do cenário atual do cliente.")
