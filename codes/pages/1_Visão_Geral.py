from pathlib import Path
from datetime import date, timedelta
import plotly.express as px
import streamlit as st
import pandas as pd
from utilidades import leitura_de_dados, COMISSAO

selecao_keys = {'Filial': 'Filial',
                'Vendedor': 'Vendedor',
                'Produto': 'Nome_produto',
                'Forma de Pagamento': 'Forma_pagamento',
                'Gênero Cliente': 'Genero_cliente'}

leitura_de_dados()

df_vendas = st.session_state['dados']['df_vendas']
df_filiais = st.session_state['dados']['df_filiais']
df_produtos = st.session_state['dados']['df_produtos']

# Reset index para evitar problemas com o merge
df_vendas = df_vendas.reset_index()

# Mesclar com df_produtos para obter o preço
print("Colunas em df_produtos:", df_produtos.columns.tolist())
df_vendas = pd.merge(left=df_vendas,
                      right=df_produtos['Preço'], 
                      on='Nome_produto', 
                      how='left')
df_vendas['Data'] = pd.to_datetime(df_vendas["Data"],dayfirst=True)
df_vendas = df_vendas.set_index('Data')

# Converter 'Preço' para numérico e calcular a comissão
df_vendas['Preço'] = pd.to_numeric(df_vendas['Preço'], errors='coerce')
df_vendas['Comissão'] = df_vendas['Preço'] * COMISSAO

data_final_def = df_vendas.index.date.max()
data_inicial_def = date(year=data_final_def.year, month=data_final_def.month, day=1)
data_inicial = st.sidebar.date_input('Data Inicial', 
                          data_inicial_def)

data_final= st.sidebar.date_input('Data Final', 
                          data_final_def)

analise_selecionada = st.sidebar.selectbox('Analisar:',
                                           list(selecao_keys.keys()))
analise_selecionada = selecao_keys[analise_selecionada]

df_vendas_corte = df_vendas[(df_vendas.index.date >= data_inicial) & (df_vendas.index.date <= data_final)]
df_vendas_corte_anterior = df_vendas[(df_vendas.index.date >= data_inicial - timedelta(days=30)) & (df_vendas.index.date <= data_final - timedelta(days=30))]

st.markdown('# Dashboard de Análise')

col1,col2,col3,col4 = st.columns(4)

valor_vendas = f'R$ {df_vendas_corte["Preço"].sum():.2f}'
dif_metrica = df_vendas_corte["Preço"].sum() - df_vendas_corte_anterior["Preço"].sum()
col1.metric('Valor de vendas no período',
            valor_vendas,
            f'{(dif_metrica):.2f}')

quantidade_vendas = df_vendas_corte["Preço"].count()
dif_metrica = df_vendas_corte["Preço"].count() - df_vendas_corte_anterior["Preço"].count()
col2.metric('Quantidade de vendas no período',
            quantidade_vendas,
            int(dif_metrica))

principal_filial = df_vendas_corte['Filial'].value_counts().index[0]
col3.metric('Principal Filial',
            principal_filial)

principal_vendedor = df_vendas_corte['Vendedor'].value_counts().index[0]
col4.metric('Principal vendedor',
            principal_vendedor)
"---"

col21, col22 = st.columns(2)

df_vendas_corte['dia_venda'] = df_vendas_corte.index.date
venda_dia = df_vendas_corte.groupby('dia_venda')['Preço'].sum()
venda_dia.name = 'Valor Venda'

fig = px.line(venda_dia)
col21.plotly_chart(fig)

fig =px.pie(df_vendas_corte,
            names = analise_selecionada,
            values='Preço')
col22.plotly_chart(fig)

st.divider()