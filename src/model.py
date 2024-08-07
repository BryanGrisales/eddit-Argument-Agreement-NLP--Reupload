import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.pipeline import make_pipeline
import joblib

def train_model(X_train, y_train):
    model = make_pipeline(
        TfidfVectorizer(),
        SVC()
    )
    model.fit(X_train, y_train)
    joblib.dump(model, 'model.pkl')

if __name__ == "__main__":
    data = pd.read_csv('data/processed/cleaned_data.csv')
    X = data['cleaned_body']
    y = data['label']  # ensure this column exists and has more than one class
    train_model(X, y)
