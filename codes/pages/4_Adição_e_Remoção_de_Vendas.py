from pathlib import Path
from datetime import datetime
import streamlit as st
import pandas as pd
from utilidades import leitura_de_dados

leitura_de_dados()

df_vendas =  st.session_state['dados']['df_vendas']
df_filiais = st.session_state['dados']['df_filiais']
df_produtos = st.session_state['dados']['df_produtos']

st.sidebar.markdown('## *Adição de vendas*')

filial_selected = st.sidebar.selectbox('Selecione a filial:', 
                                       sorted(df_vendas['Filial'].unique()),
                                       index=None,
                                       placeholder='Filiais')
if filial_selected:
    vendedores_filial = df_filiais[df_filiais['Cidade'] == filial_selected]['Vendedores'].values[0]
    vendedores_filial = vendedores_filial.split(';')
else:
    vendedores_filial = []
vendedor_selected = st.sidebar.selectbox('Selecione o vendedor:', 
                                        sorted(vendedores_filial),
                                        index=None,
                                        placeholder='Vendedores')

col1, col2 = st.sidebar.columns(2)
produto_selected = col1.selectbox('Selecione o produto:', 
                                        sorted(list(df_vendas['Nome_produto'].unique())),
                                        index=None,
                                        placeholder='Produtos')                  
quantidade_produto = col2._number_input('Quantidade do produto:',
                                        step=1 ,
                                        format='%d')

valor_compra = st.sidebar._number_input('Valor da compra:', 
                                        step=0.01,
                                        format='%.2f')

nome_cliente = st.sidebar.text_input('Nome do cliente:',
                                     placeholder='Nome')

genero_cliente = st.sidebar.selectbox('Gênero do cliente:', 
                                    sorted(list(df_vendas['Genero_cliente'].unique())),
                                    index=None,
                                    placeholder='Gênero')
forma_pagamento = st.sidebar.selectbox('Forma de pagamento:',
                                       sorted(list(df_vendas['Forma_pagamento'].unique())),
                                       index=None,
                                       placeholder='Forma de pagamento')
botao_adicionar_venda = st.sidebar.button('Adicionar venda',use_container_width=False)

if botao_adicionar_venda:
    lista_adicionar = [df_vendas['ID_venda'].max() + 1,
                    filial_selected,
                    vendedor_selected,
                    produto_selected,
                    quantidade_produto,
                    valor_compra,
                    nome_cliente,
                    genero_cliente,
                    forma_pagamento,
                    ]
    hora_adicionar = datetime.now()
    df_vendas.loc[hora_adicionar] = lista_adicionar
    caminho_datasets = st.session_state['caminho_datasets']
    df_vendas.to_csv(caminho_datasets / 'vendas.csv' , decimal=',', sep=';')


st.sidebar.markdown('## Remoção de Vendas')
id_remocao = st.sidebar.number_input('Id da venda a ser removida:',
                                     min_value=0,
                                     max_value=df_vendas['ID_venda'].max())
botao_remover_venda = st.sidebar.button('Remover venda',use_container_width=False)
if botao_remover_venda:
    df_vendas = df_vendas[df_vendas['ID_venda'] != id_remocao]
    caminho_datasets = st.session_state['caminho_datasets']
    df_vendas.to_csv(caminho_datasets / 'vendas.csv' , decimal=',', sep=';')
    st.session_state['dados']['df_vendas'] = df_vendas

st.dataframe(df_vendas, height=800)






