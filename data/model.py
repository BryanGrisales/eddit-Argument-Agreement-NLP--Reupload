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
    # Example usage with dummy data
    X_train = ["sample argument", "another argument"]
    y_train = [1, 0]
    train_model(X_train, y_train)
