import pickle
import re
import math
from urllib.parse import urlparse


# -----------------------------
# LOAD MODEL
# -----------------------------

with open("model.pkl", "rb") as file:
    model = pickle.load(file)


# -----------------------------
# FEATURE EXTRACTION
# -----------------------------

def extract_features(url):

    url_lower = url.lower()

    # URL length
    url_length = len(url)

    # Number of dots
    num_dots = url.count(".")

    # HTTPS
    has_https = 1 if url_lower.startswith("https://") else 0

    # IP address
    ip_pattern = r"https?://(\d{1,3}\.){3}\d{1,3}"

    has_ip = 1 if re.search(ip_pattern, url) else 0

    # Parse URL
    parsed_url = urlparse(url)

    # Number of subdirectories
    path = parsed_url.path

    num_subdirs = len(
        [part for part in path.split("/") if part]
    )

    # Number of parameters
    num_params = len(
        [param for param in parsed_url.query.split("&") if param]
    )

    # Suspicious words
    suspicious_keywords = [
        "login",
        "verify",
        "account",
        "password",
        "bank",
        "payment",
        "secure",
        "update",
        "confirm",
        "signin"
    ]

    suspicious_words = sum(
        1
        for word in suspicious_keywords
        if word in url_lower
    )

    # Special characters
    special_chars = re.findall(
        r"[^a-zA-Z0-9]",
        url
    )

    special_char_count = len(special_chars)

    # Digits
    digits_count = sum(
        char.isdigit()
        for char in url
    )

    # Entropy calculation
    entropy = 0

    if len(url) > 0:

        for char in set(url):

            probability = url.count(char) / len(url)

            entropy -= probability * math.log2(
                probability
            )


    # Return features in SAME order
    return [[
        url_length,
        num_dots,
        has_https,
        has_ip,
        num_subdirs,
        num_params,
        suspicious_words,
        special_char_count,
        digits_count,
        entropy
    ]]


# -----------------------------
# PREDICTION
# -----------------------------

def predict(url):

    features = extract_features(url)

    prediction = model.predict(features)[0]

    probability = model.predict_proba(features)[0][1]

    if prediction == 1:

        result = "PHISHING"

    else:

        result = "SAFE"


    return {
        "prediction": result,
        "probability": round(
            probability * 100,
            2
        )
    }