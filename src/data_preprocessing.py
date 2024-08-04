import pandas as pd

def load_data(filepath):
    # Load data from file
    df = pd.read_csv(filepath)
    return df

def clean_data(df):
    # Clean data (e.g., remove NaNs, duplicates)
    df = df.dropna()
    return df

if __name__ == "__main__":
    data = load_data('data/raw/debate_data.csv')
    clean_data = clean_data(data)
    clean_data.to_csv('data/processed/cleaned_data.csv', index=False)