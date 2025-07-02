from pathlib import Path
import streamlit as st
import pandas as pd
from utilidades import leitura_de_dados

leitura_de_dados()


df_vendas =  st.session_state['dados']['df_vendas']
df_filiais = st.session_state['dados']['df_filiais']
df_produtos = st.session_state['dados']['df_produtos']



def mostra_tabela_produtos():
    st.dataframe(df_produtos)

def mostra_tabela_filiais():
    st.dataframe(df_filiais)

def mostra_tabela_vendas():
    st.sidebar.divider()
    st.sidebar.markdown('### Filtrar tabela')
    select_columns_for_tabela = st.sidebar.multiselect(label='Selecione as colunas da tabela:',
                                                options=list(df_vendas.columns),
                                                default= list(df_vendas.columns))
    col1, col2 = st.sidebar.columns(2)
    coluna_filtrada = col1.selectbox('Filtrar coluna',
                                    list(df_vendas.columns))
    valores_unicos_coluna_filtrada = list(df_vendas[coluna_filtrada].unique())  #seleciona os valores únicos de uma coluna, representados nas linhas e que são considerados apenas uma vez.
    valor_filtro = col2.selectbox('Valor do filtro', 
                                  valores_unicos_coluna_filtrada)
    filtrar = col1.button('Filtrar')
    limpar = col2.button('Limpar')

    if filtrar:
        st.dataframe(df_vendas.loc[df_vendas[coluna_filtrada] == valor_filtro, select_columns_for_tabela])
    elif limpar:
        st.dataframe(df_vendas[select_columns_for_tabela], height=700)
    else:
        st.dataframe(df_vendas[select_columns_for_tabela], height=700)


st.sidebar.markdown('## Seleção de Tabelas')
tabelas_selecionada = st.sidebar.selectbox('Selecione a tabela que você deseja ver:',
                                            ['Vendas','Produtos','Filiais'])


st.markdown(f'## {tabelas_selecionada}')  # título da tabela
if tabelas_selecionada == 'Produtos':
    mostra_tabela_produtos()
elif tabelas_selecionada == 'Filiais':
    mostra_tabela_filiais()
elif tabelas_selecionada == 'Vendas':
    mostra_tabela_vendas()

    


















