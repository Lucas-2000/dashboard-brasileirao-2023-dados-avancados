import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt

st.title("Gere os gráficos")

dataset_directory = "datasets"

datasets = sorted(os.listdir(dataset_directory))

dataset = st.sidebar.selectbox("Datasets", datasets)

if dataset:
    dataset_path = os.path.join(dataset_directory, dataset)
    
    if dataset.endswith('.csv'):
        df = pd.read_csv(dataset_path)
        
        st.write("## Dados:")
        st.write(df)
        
        filtro1 = st.sidebar.selectbox("Eixo X", df.columns, key="x")
        filtro2 = st.sidebar.selectbox("Eixo Y", df.columns, key="y")
        
        tipo_grafico = st.sidebar.selectbox("Tipo Gráfico", ['Selecione o tipo de gráfico', 'Gráfico de Linhas', 'Gráfico de Barras', 'Gráfico de Dispersão', 'Histograma'])
        
        if tipo_grafico != 'Selecione o tipo de gráfico':
            st.write("## Gráfico")
            if tipo_grafico in ['Gráfico de Linhas', 'Gráfico de Barras']:
                if tipo_grafico == 'Gráfico de Linhas':
                    st.line_chart(df.set_index(filtro1)[filtro2])
                elif tipo_grafico == 'Gráfico de Barras':
                    st.bar_chart(df.set_index(filtro1)[filtro2])
            elif tipo_grafico == 'Gráfico de Dispersão':
                st.write("## Gráfico de Dispersão")
                fig, ax = plt.subplots()
                ax.scatter(df[filtro1], df[filtro2])
                for i, txt in enumerate(df['Squad']):
                    ax.annotate(txt, (df[filtro1][i], df[filtro2][i]))
                st.pyplot(fig)
            elif tipo_grafico == 'Histograma':
                st.write("## Histograma")
                plt.hist(df[filtro1])
                st.pyplot()
        else:
            st.info("Por favor, selecione um tipo de gráfico. Caso deseje utilizar o histograma, o Eixo X é utilizado como base para geração.")
    else:
        st.error("Este exemplo só suporta arquivos CSV.")
