import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import joblib

# Load the dataset
df = pd.read_csv("data/scam_dataset.csv")

# Define features and labels
X = df["message"]
y = df["label"]

# Build a pipeline: TF-IDF + Naive Bayes
model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("nb", MultinomialNB())
])

# Train the model
model.fit(X, y)

# Save the trained model
joblib.dump(model, "model/scam_model.pkl")

print("✅ Model trained and saved to model/scam_model.pkl")
