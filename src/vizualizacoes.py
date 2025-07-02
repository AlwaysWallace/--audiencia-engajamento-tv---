import matplotlib.pyplot as plt
import seaborn as sns

def plot_audiencia(df):
    plt.figure(figsize=(12,6))
    sns.lineplot(data=df, x='data', y='audiencia', hue='programa')
    plt.title('Audiência por Programa ao Longo do Tempo')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

import matplotlib.pyplot as plt
import seaborn as sns

def plot_engajamento(df, salvar=False, caminho='grafico_engajamento.png'):
    if 'data' in df.columns and 'engajamento' in df.columns and 'programa' in df.columns:
        plt.figure(figsize=(12,6))
        sns.set_style("whitegrid")
        sns.set_palette("Set2")
        sns.lineplot(data=df, x='data', y='engajamento', hue='programa')
        plt.title('Engajamento nas Redes Sociais por Programa')
        plt.xlabel('Data')
        plt.ylabel('Engajamento')
        plt.xticks(rotation=45)
        plt.tight_layout()
        if salvar:
            plt.savefig(caminho)
        plt.show()
    else:
        print("Colunas necessárias não encontradas para o gráfico de engajamento.")