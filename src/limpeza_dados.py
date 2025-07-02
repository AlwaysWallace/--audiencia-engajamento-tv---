import pandas as pd

def limpar_audiencia(df):
    try:
        df['data'] = pd.to_datetime(df['data'], errors='coerce')
        df = df.dropna(subset=['data'])  # Remove datas inválidas
        df['programa'] = df['programa'].astype(str).str.strip().str.upper()
    except Exception as e:
        print(f"Erro ao limpar audiência: {e}")
    return df

def limpar_redes_sociais(df):
    try:
        if 'data' in df.columns and 'hashtags' in df.columns:
            df['data'] = pd.to_datetime(df['data'], errors='coerce')
            df = df.dropna(subset=['data'])  # Remove datas inválidas
            df['hashtags'] = df['hashtags'].astype(str).str.lower()
        else:
            print("Colunas esperadas não encontradas.")
    except Exception as e:
        print(f"Erro ao limpar redes sociais: {e}")
    return df
