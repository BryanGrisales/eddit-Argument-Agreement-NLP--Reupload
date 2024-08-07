import pandas as pd
import re
import json
import os

def load_data(filepath):
    with open(filepath, 'r') as f:
        data = json.load(f)
    return pd.DataFrame(data)

def clean_text(text):
    # remove URLs
    text = re.sub(r'http\S+', '', text)
    # remove special characters and digits
    text = re.sub(r'[^A-Za-z\s]', '', text)
    # convert to lowercase
    text = text.lower()
    return text

def label_data(text):
    # simple labeling logic
    if "agree" in text or "support" in text:
        return 1
    elif "disagree" in text or "oppose" in text:
        return -1
    else:
        return 0

def clean_data(df):
    # clean the body text
    df['cleaned_body'] = df['body'].apply(clean_text)
    # label the data
    df['label'] = df['body'].apply(label_data)
    # drop rows with empty cleaned body
    df = df[df['cleaned_body'].str.strip() != '']
    return df

if __name__ == "__main__":
    data = load_data('data/raw/top_posts.json')
    clean_data = clean_data(data)
    os.makedirs('data/processed', exist_ok=True)
    clean_data.to_csv('data/processed/cleaned_data.csv', index=False)
    print("Cleaned data saved to data/processed/cleaned_data.csv")
