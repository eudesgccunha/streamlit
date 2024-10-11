import streamlit as st

# Definir um titulo
st.title('Evento | Dashboard com Python')

# Cabeçalho de uma seção
st.header('Conhecendo os elementos do Streamlit')

# subtítulo
st.subheader('Aula 2 [2/4]')

# texto simples
st.text('Nesta aula vamos entender os elementos do Streamlit')

# texto formatado usando Markdown
st.markdown('# Stremlit')

st.write('Streamlit é uma framework de alto nível do Python!')

# botão com validação | Combinando com o streamlit
if st.button('Clique aqui'):
    for Loop in range(5):
        st.write(f'Botão selecionado!{Loop}')
    
# radio - selecionar
escolha = escolha = st.radio('Qual linguagem mais utiliza:', ('Python', 'R', 'Java', 'JavaScript', 'Outra'))

# lista de frameworks
Lista_Frameworks = ['Matplotlib', 'Seaborn', 'Plotly']
opcao = st.selectbox('Escolha seu framework favorito de Data Visualization:', Lista_Frameworks)

# seleção de multiplas caixas
Lista_Estudo = ['Pandas', 'Numpy', 'Matplotlib', 'Seaborn', 'Plotly', 'Scipy', 'TensorFlow']
selecoes = st.multiselect('Escolha múltiplas opções:', Lista_Estudo )

# seleção de valor

valor = st.slider('Quantos anos trabalha com Data Science:', 0, 30, 1)

#subir um arquivo

arquivo = st.file_uploader('Escolha um arquivo', type=['csv', 'txt'])

st.image('logo_python.png', caption='Descritivo da imagem', use_column_width=True)

# importar novas bibliotecas
import pandas as pd
import numpy as np

# Criando um DataFrame base
df = pd.DataFrame(
    { 
        'Dias': [loop for loop in range(31)]
    }
)

# Adicionando novas colunas com dados fictícios
df['Valor de Venda'] = np.random.randint(100, 1000, size=31)
df['Custo'] = df['Valor de Venda'] * 0.8  
df['Lucro'] = df['Valor de Venda'] - df['Custo']
df['Quantidade Vendida'] = np.random.randint(10, 50, size=31)
df['Cliente'] = ['Cliente ' + str(i) for i in range(1, 32)]

# Incluindo a tabela no front
st.dataframe(df)

import altair as alt

# Criando um gráfico de linha com Altair
chart = alt.Chart(df).mark_line().encode(
    x='Dias',
    y='Valor de Venda'
)

# Exibindo o gráfico no Streamlit
st.altair_chart(chart)
