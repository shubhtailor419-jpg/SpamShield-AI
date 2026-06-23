import pandas as pd
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

df = pd.read_csv("spam.csv")

vectorizer = TfidfVectorizer(stop_words="english")

X = vectorizer.fit_transform(df["text"])

y = df["label"]

model = MultinomialNB()

model.fit(X, y)

joblib.dump(model, "spam_model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("Model created successfully")