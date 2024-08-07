import pandas as pd
import spacy

nlp = spacy.load("en_core_web_sm")

def extract_features(text):
    doc = nlp(text)
    features = {
        "num_tokens": len(doc),
        "num_entities": len(doc.ents),
        "num_sentences": len(list(doc.sents))
    }
    return features

def process_data(filepath):
    df = pd.read_csv(filepath)
    features = df['cleaned_body'].apply(extract_features)
    features_df = pd.DataFrame(features.tolist())
    return pd.concat([df, features_df], axis=1)

if __name__ == "__main__":
    processed_data = process_data('data/processed/cleaned_data.csv')
    processed_data.to_csv('data/processed/features_data.csv', index=False)
    print("Features extracted and saved to data/processed/features_data.csv")
