
import streamlit as st

# Título principal com espaçamento adicional
st.markdown('# 📊 Sales Analytics Dashboard')
st.markdown('**Transforme dados brutos em insights estratégicos para o setor de vendas**')

# Espaçamento
st.write('')

# Abas com funcionalidades
tab1, tab2, tab3 = st.tabs(["Projeto", "Tecnologias Utilizadas", "Sobre"])

# Função para adicionar informações de contato
def add_contact_info():
    st.markdown('''
    ---
    ### 📧 Entre em Contato!
    Para mais informações, dúvidas ou para discutir como posso ajudar a transformar seus dados em insights valiosos:
    - **Email profissional:** email_profissional@email.com
    ''')

# Função para adicionar rodapé com menção aos dados sintéticos
def add_footer():
    st.markdown('''
    ---
    > *Este projeto emprega dados sintéticos gerados por inteligência artificial para demonstrar aplicações práticas em cenários reais.* 
    ''')

with tab1:
    st.markdown('''
    ### ⚡Funcionalidades
    - **Visão Geral:** Analise gráficos interativos dos dados de vendas e compare-os com os resultados dos últimos 30 dias.
    - **Visualização Dinâmica:** Explore tabelas de dados personalizadas com base em seus filtros.
    - **Tabelas:** Acesse o banco de dados completo da empresa com opções de filtragem.
    - **Adição e Remoção de Vendas:** Gerencie suas vendas com facilidade, incluindo novos registros ou corrigindo erros.
    ''')
    # Destaque para o valor do projeto
    st.markdown('''
    ---
    ### 📈 Crescimento e Oportunidades
    - **Identificação de produtos mais rentáveis**
    - **Análise de desempenho por região ou canal de vendas**
    - **Detecção de oportunidades de crescimento**
    ''')
   
    # Adiciona rodapé
    add_footer()

with tab2:
    st.write('')
    st.write('')
    st.markdown('''
    ### ⚙️ Tecnologias Utilizadas''')
    st.write('')
    st.markdown('''
    | Biblioteca   | Função Principal                  |  Versão  |
    |--------------|-----------------------------------| -------- |
    | `pandas`     | Manipulação e limpeza de dados    |  2.3.0   |
    | `plotly`     | Gráficos interativos profissionais|  6.1.2   |
    | `streamlit`  | Interface web e componentes UI    |  1.46.0  |
    ''')
    st.write('')
    st.write('')
    add_footer()

 
   

with tab3:
    st.markdown('''
    ### 🌟 Oportunidades de Colaboração!
    Se você está buscando:
    - **Personalização avançada** para atender às necessidades específicas do seu negócio
    - **Integração com sistemas existentes** para um fluxo de trabalho sem interrupções
    - **Apoio contínuo** para maximizar o valor dos dados da sua empresa
    entre em contato para discutir como posso ajudar.
    ''')
    # Adiciona informações de contato
    add_contact_info()
    # Adiciona rodapé
    add_footer()

