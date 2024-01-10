import streamlit as st
import pandas as pd
import webbrowser

# if "data" not in st.session_state:
#   df_data = pd.read_csv("datasets/regular_overall_season_serie_a.csv", index_col=0)

#   # Gravando dataframe no cache da sessão
#   st.session_state["data"] = df_data
  
st.write("# Dados avançados do campeonato brasileiro! ⚽")
st.sidebar.markdown("Desenvolvido por [Lucas Marchesoni](https://www.linkedin.com/in/lucasmarchesoni/)")
  
st.markdown(
  """
    O conjunto dados contém informações avançadas até a rodada 38 do campeonato brasileiro de 2023.
    Possui uma ampla gama de métricas como xG, xGA, Saves%, Passes, etc. Possibilitando realizar uma análise
    mais a fundo dentro de uma partida de futebol e todas suas nuances.
    
    Para poder explorar cada dado possui **24 bases** para poderem ser analisadas, extraídos insights, gerado gráficos
    e poder exportar os resultados para poder compartilhar em outros meios.
    
    Todos os dados foram retirados do site [Football Reference](https://fbref.com/en/comps/24/Serie-A-Stats).
    
    Para acessar os datasets separadamente [clique aqui](https://github.com/Lucas-2000/api-sports-stats).
  """
)