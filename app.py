import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))
import streamlit as st
import pandas as pd
from visualizacoes import plot_audiencia, plot_engajamento
from limpeza_dados import limpar_audiencia, limpar_redes_sociais

st.set_page_config(page_title="Audiência e Engajamento", layout="wide")

st.title("📺 Análise de Audiência e Engajamento de Programas de TV")

# Carregar dados
audiencia = pd.read_csv('data/audiencia.csv')
redes = pd.read_csv('data/redes_sociais.csv')

# Limpeza
audiencia = limpar_audiencia(audiencia)
redes = limpar_redes_sociais(redes)

# Merge
df_merge = pd.merge(audiencia, redes, on=['data', 'programa'])

# Seções
st.subheader("📊 Audiência ao Longo do Tempo")
plot_audiencia(audiencia)

st.subheader("📈 Engajamento nas Redes Sociais")
plot_engajamento(redes)

st.subheader("🔗 Correlação entre Audiência e Engajamento")
st.write(df_merge[['audiencia', 'engajamento']].corr())