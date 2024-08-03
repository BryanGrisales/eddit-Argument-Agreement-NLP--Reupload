import spacy

def extract_features(text):
    # Example feature extraction using spaCy
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    features = {
        "num_tokens": len(doc),
        "num_entities": len(doc.ents),
    }
    return features

if __name__ == "__main__":
    # Example usage
    text = "This is a sample argument."
    features = extract_features(text)
    print(features)
