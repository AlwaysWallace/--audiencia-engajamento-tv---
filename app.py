import streamlit as st
import pandas as pd
from src.limpeza_dados import limpar_audiencia, limpar_redes_sociais
from src.visualizacoes import plot_audiencia, plot_engajamento

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