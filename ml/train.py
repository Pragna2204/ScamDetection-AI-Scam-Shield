import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)


# Load dataset
data = pd.read_csv("phishing_features.csv")

print("Original dataset shape:", data.shape)

# Remove duplicate URLs
data = data.drop_duplicates(subset="url")

print("After removing duplicates:", data.shape)


# -----------------------------
# BALANCE DATASET
# -----------------------------

phishing = data[data["label"] == 1]
legitimate = data[data["label"] == 0]

# Use equal number from both classes
phishing_sample = phishing.sample(
    n=len(legitimate),
    random_state=42
)

balanced_data = pd.concat(
    [phishing_sample, legitimate]
)

# Shuffle
balanced_data = balanced_data.sample(
    frac=1,
    random_state=42
).reset_index(drop=True)


print("\nBalanced dataset:")
print(balanced_data["label"].value_counts())


# -----------------------------
# FEATURES
# -----------------------------

features = [
    "url_length",
    "num_dots",
    "has_https",
    "has_ip",
    "num_subdirs",
    "num_params",
    "suspicious_words",
    "special_char_count",
    "digits_count",
    "entropy"
]

X = balanced_data[features]
y = balanced_data["label"]


# -----------------------------
# TRAIN / TEST SPLIT
# -----------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# -----------------------------
# RANDOM FOREST
# LIMIT MODEL COMPLEXITY
# -----------------------------

model = RandomForestClassifier(
    n_estimators=100,

    max_depth=10,

    min_samples_split=10,

    min_samples_leaf=5,

    max_features="sqrt",

    random_state=42,

    class_weight="balanced"
)


print("\nTraining model...")

model.fit(X_train, y_train)


# -----------------------------
# TRAINING ACCURACY
# -----------------------------

train_predictions = model.predict(X_train)

train_accuracy = accuracy_score(
    y_train,
    train_predictions
)

print("\nTraining Accuracy:",
      round(train_accuracy * 100, 2))


# -----------------------------
# TEST ACCURACY
# -----------------------------

test_predictions = model.predict(X_test)

test_accuracy = accuracy_score(
    y_test,
    test_predictions
)

print("Testing Accuracy:",
      round(test_accuracy * 100, 2))


# -----------------------------
# CLASSIFICATION REPORT
# -----------------------------

print("\nClassification Report:")

print(
    classification_report(
        y_test,
        test_predictions
    )
)


# -----------------------------
# CONFUSION MATRIX
# -----------------------------

print("\nConfusion Matrix:")

print(
    confusion_matrix(
        y_test,
        test_predictions
    )
)


# -----------------------------
# SAVE MODEL
# -----------------------------

with open("model.pkl", "wb") as file:
    pickle.dump(model, file)

print("\nModel saved successfully!")