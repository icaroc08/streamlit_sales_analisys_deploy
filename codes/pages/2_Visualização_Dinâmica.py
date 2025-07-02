####
from pathlib import Path
import streamlit as st
import pandas as pd
from utilidades import leitura_de_dados, COMISSAO

COLUNAS_ANALISE = ['Filial', 'Vendedor', 'Nome_produto', 'Genero_cliente', 'Forma_pagamento']
COLUNAS_VALOR = ['Preço', 'Comissão']
FUNCOES_AGG = {'soma': 'sum', 'contagem': 'count'}

leitura_de_dados()

df_vendas = st.session_state['dados']['df_vendas']
df_filiais = st.session_state['dados']['df_filiais']
df_produtos = st.session_state['dados']['df_produtos']

# Reset index para evitar problemas com o merge
df_vendas = df_vendas.reset_index()

# Mesclar com df_produtos para obter o preço
df_vendas = pd.merge(left=df_vendas,
                      right=df_produtos['Preço'], 
                      on='Nome_produto', 
                      how='left')
df_vendas = df_vendas.set_index('Data')


# Converter 'Preço' para numérico e calcular a comissão
df_vendas['Preço'] = pd.to_numeric(df_vendas['Preço'], errors='coerce')
df_vendas['Comissão'] = df_vendas['Preço'] * COMISSAO

# Sidebar para seleção
indices_selecionados = st.sidebar.multiselect('Selecione os índices:', COLUNAS_ANALISE)

# Filtrar as colunas disponíveis para seleção, excluindo os índices já selecionados
colunas_disponiveis = [col for col in COLUNAS_ANALISE if col not in indices_selecionados]
colunas_selecionadas = st.sidebar.multiselect('Selecione as colunas:', colunas_disponiveis)

valor_selecionado = st.sidebar.selectbox('Selecione o valor de análise:', options=COLUNAS_VALOR)
metrica_selecionada = st.sidebar.selectbox('Selecione a métrica:', list(FUNCOES_AGG.keys()))

# Criar a tabela dinâmica se houver seleções válidas
if len(indices_selecionados) > 0 and len(colunas_selecionadas) > 0:
    metrica_func = FUNCOES_AGG[metrica_selecionada]
    try:
        vendas_pivotadas = pd.pivot_table(
            df_vendas,
            index=indices_selecionados,
            columns=colunas_selecionadas,
            values=valor_selecionado,
            aggfunc=metrica_func,
            fill_value=0  # Preencher valores ausentes com 0
        )
        vendas_pivotadas['TOTAL GERAL'] = vendas_pivotadas.sum(axis=1)
        vendas_pivotadas.loc['TOTAL GERAL'] = vendas_pivotadas.sum(axis=0).to_list()
        st.dataframe(vendas_pivotadas)
    except Exception as e:
        st.error(f"Erro ao gerar a tabela: {e}")
else:
    st.warning("Por favor, selecione pelo menos um índice e uma coluna para gerar a tabela.")
####
