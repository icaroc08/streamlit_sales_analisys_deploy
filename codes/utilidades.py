from pathlib import Path
import streamlit as st
import pandas as pd

COMISSAO = 0.08

def leitura_de_dados():    #lê as tabelas em formato csv.
    if not 'dados' in st.session_state:         #gera a session state para manter salvo a tabela caso reinicie o executável
        pasta_datasets = Path(__file__).parents[1] / 'datasets'           #define o path para a pasta que contém os arquivos csv
        df_vendas = pd.read_csv(pasta_datasets / 'vendas.csv', decimal=',', sep=';',parse_dates=True,index_col=0)
        df_filiais = pd.read_csv(pasta_datasets / 'filiais.csv', decimal=',', sep=';',parse_dates=True,index_col=0)
        df_produtos = pd.read_csv(pasta_datasets / 'produtos.csv', decimal=',', sep=';',parse_dates=True,index_col=0)
        dados = {'df_vendas': df_vendas,
                'df_filiais': df_filiais,
                'df_produtos': df_produtos}
        st.session_state['caminho_datasets'] = pasta_datasets
        st.session_state['dados'] = dados
    
    ######