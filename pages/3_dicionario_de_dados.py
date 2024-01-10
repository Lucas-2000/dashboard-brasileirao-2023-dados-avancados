import streamlit as st
import os
from helpers import dicionario

st.title("Dicionário de dados")

dataset_directory = "datasets"

datasets = sorted(os.listdir(dataset_directory))

dataset = st.sidebar.selectbox("Datasets", datasets)

dic = dicionario.Dicionario()

if dataset:
    dataset_path = os.path.join(dataset_directory, dataset)
    nome_do_dataset = os.path.basename(dataset_path)
    
    if nome_do_dataset == 'standard_stats_squad_serie_a.csv':
      st.markdown(dic.standard_stats_squad_serie_a())
    
    elif nome_do_dataset == 'goalkeeping_stats_squad_opponent_serie_a.csv':
      st.markdown(dic.goalkeeping_stats_squad_opponent_serie_a())
    
    elif nome_do_dataset == 'goalkeeping_stats_squad_serie_a.csv':
      st.markdown(dic.goalkeeping_stats_squad_serie_a())
    
    elif nome_do_dataset == 'regular_overall_homeaway_serie_a.csv':
      st.markdown(dic.regular_overall_homeaway_serie_a())
    
    elif nome_do_dataset == 'regular_overall_season_serie_a.csv':
      st.markdown(dic.regular_overall_season_serie_a())
    
    elif nome_do_dataset == 'squad_advanced_defense_opponent_stats_serie_a.csv':
      st.markdown(dic.squad_advanced_defense_opponent_stats_serie_a())
    
    elif nome_do_dataset == 'squad_advanced_defense_stats_serie_a.csv':
      st.markdown(dic.squad_advanced_defense_stats_serie_a())
    
    elif nome_do_dataset == 'squad_advanced_gca_opponent_stats_serie_a.csv':
      st.markdown(dic.squad_advanced_gca_opponent_stats_serie_a())
    
    elif nome_do_dataset == 'squad_advanced_gca_stats_serie_a.csv':
      st.markdown(dic.squad_advanced_gca_stats_serie_a())
    
    elif nome_do_dataset == 'squad_advanced_goalkeeping_opponent_stats_serie_a.csv':
      st.markdown(dic.squad_advanced_goalkeeping_opponent_stats_serie_a())
    
    elif nome_do_dataset == 'squad_advanced_goalkeeping_stats_serie_a.csv':
      st.markdown(dic.squad_advanced_goalkeeping_stats_serie_a())
    
    elif nome_do_dataset == 'squad_advanced_misc_opponent_stats_serie_a.csv':
      st.markdown(dic.squad_advanced_misc_opponent_stats_serie_a())
    
    elif nome_do_dataset == 'squad_advanced_misc_stats_serie_a.csv':
      st.markdown(dic.squad_advanced_misc_stats_serie_a())
    
    elif nome_do_dataset == 'squad_advanced_passing_opponent_squad_serie_a.csv':
      st.markdown(dic.squad_advanced_passing_opponent_squad_serie_a())
    
    elif nome_do_dataset == 'squad_advanced_passing_stats_serie_a.csv':
      st.markdown(dic.squad_advanced_passing_stats_serie_a())
    
    elif nome_do_dataset == 'squad_advanced_passing_types_opponent_stats_serie_a.csv':
      st.markdown(dic.squad_advanced_passing_types_opponent_stats_serie_a())
    
    elif nome_do_dataset == 'squad_advanced_passing_types_stats_serie_a.csv':
      st.markdown(dic.squad_advanced_passing_types_stats_serie_a())
    
    elif nome_do_dataset == 'squad_advanced_passing_types_stats_serie_a.csv':
      st.markdown(dic.squad_advanced_passing_types_stats_serie_a())
    
    elif nome_do_dataset == 'squad_advanced_playing_time_opponent_stats_serie_a.csv':
      st.markdown(dic.squad_advanced_playing_time_opponent_stats_serie_a())
    
    elif nome_do_dataset == 'squad_advanced_playing_time_stats_serie_a.csv':
      st.markdown(dic.squad_advanced_playing_time_stats_serie_a())
    
    elif nome_do_dataset == 'squad_advanced_possession_opponent_stats_serie_a.csv':
      st.markdown(dic.squad_advanced_possession_opponent_stats_serie_a())
    
    elif nome_do_dataset == 'squad_advanced_possession_stats_serie_a.csv':
      st.markdown(dic.squad_advanced_possession_stats_serie_a())
    
    elif nome_do_dataset == 'squad_advanced_shooting_opponent_stats_serie_a.csv':
      st.markdown(dic.squad_advanced_shooting_opponent_stats_serie_a())
    
    elif nome_do_dataset == 'squad_advanced_shooting_stats_squad_serie_a.csv':
      st.markdown(dic.squad_advanced_shooting_stats_squad_serie_a())
    
    elif nome_do_dataset == 'squad_standard_stats_opponent_serie_a.csv':
      st.markdown(dic.squad_standard_stats_opponent_serie_a())
      