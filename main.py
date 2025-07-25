import streamlit as st
import pandas as pd

# Carregar a planilha
df = pd.read_excel("bd_rodadas.xlsx")

st.title("📈 Painel de Preços de Energia")
st.markdown("Filtre os dados abaixo e veja a tabela e o gráfico interativo.")

# Filtros
subs = df['SUB'].unique()
filtro_sub = st.multiselect("Submercado:", subs, default=subs)

revisoes = df['REVISAO'].unique()
filtro_rev = st.multiselect("Revisão:", revisoes, default=revisoes)

datas = sorted(df['DATA'].unique())
filtro_data = st.multiselect("Data:", datas, default=datas)

# Aplicar filtros
df_filtrado = df[
    df['SUB'].isin(filtro_sub) &
    df['REVISAO'].isin(filtro_rev) &
    df['DATA'].isin(filtro_data)
]

st.subheader("📋 Tabela filtrada")
st.dataframe(df_filtrado)

# Mostrar gráfico de preços
st.subheader("📊 Evolução do preço")
if not df_filtrado.empty:
    df_plot = df_filtrado[['DATA', 'SUB', 'PRECO']].sort_values(by='DATA')
    st.line_chart(df_plot, x='DATA', y='PRECO', color='SUB')
else:
    st.warning("Nenhum dado encontrado com os filtros selecionados.")
