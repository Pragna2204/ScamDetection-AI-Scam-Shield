# 🛡️ Phishing and Scam Detection Platform

A machine learning-based web application that analyzes URLs and detects potential phishing websites using a **Random Forest classification model**.

The platform allows users to enter a URL through a web interface. The request is processed through a **Node.js/Express backend**, which communicates with a **Python Flask Machine Learning API** to predict whether the URL is **SAFE** or **PHISHING**.

---

## 🚀 Features

* 🔗 URL phishing detection
* 🤖 Machine Learning-based prediction
* 🌲 Random Forest classifier
* 📊 Phishing risk score
* ⚠️ SAFE or PHISHING classification
* 🔍 URL feature extraction
* 🌐 Web-based user interface
* 🔄 Integration between Node.js and Python
* 🧠 REST API architecture

---

## 🏗️ System Architecture

```text
                    USER
                      │
                      ▼
             ┌─────────────────┐
             │    Frontend     │
             │ HTML/CSS/JS     │
             └────────┬────────┘
                      │
                      ▼
             ┌─────────────────┐
             │ Node.js/Express │
             │   Backend API   │
             └────────┬────────┘
                      │
                      ▼
             ┌─────────────────┐
             │   Flask API     │
             │   Python ML     │
             └────────┬────────┘
                      │
                      ▼
             ┌─────────────────┐
             │ Random Forest   │
             │     Model       │
             └────────┬────────┘
                      │
              ┌───────┴────────┐
              ▼                ▼
           SAFE             PHISHING
```

---

## 🛠️ Technologies Used

### Frontend

* HTML
* CSS
* JavaScript

### Backend

* Node.js
* Express.js
* CORS

### Machine Learning

* Python
* Scikit-learn
* Pandas
* Random Forest Classifier

### Machine Learning API

* Flask

### Development Tools

* Visual Studio Code
* Git
* GitHub

---

## 📂 Project Structure

```text
phishing_scam_detection/
│
├── Frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── backend/
│   ├── server.js
│   ├── package.json
│   └── package-lock.json
│
├── ml/
│   ├── app.py
│   ├── train.py
│   ├── predict.py
│   ├── model.pkl
│   ├── features.pkl
│   └── phishing_features.csv
│
├── venv/
├── .gitignore
└── README.md
```

> **Note:** The dataset and virtual environment may be excluded from GitHub using `.gitignore`.

---

# 🔍 How the Detection Works

The system analyzes different characteristics of a URL.

The machine learning model uses the following features:

* URL length
* Number of dots
* HTTPS usage
* Presence of an IP address
* Number of subdirectories
* Number of URL parameters
* Suspicious words
* Number of special characters
* Number of digits
* URL entropy

These features are passed to a **Random Forest Classifier**, which predicts whether the URL is likely to be phishing.

---

## 🤖 Machine Learning Model

The project uses a **Random Forest Classifier** to classify URLs.

### Workflow

```text
URL Dataset
     │
     ▼
Data Preprocessing
     │
     ▼
Feature Selection
     │
     ▼
Train/Test Split
     │
     ▼
Random Forest Model
     │
     ▼
Model Evaluation
     │
     ▼
Saved Model (.pkl)
```

The trained model is saved as:

```text
model.pkl
```

The model is then loaded by the Python prediction service.

---

## 🧠 Feature Extraction

When a user enters a URL, the system extracts features such as:

```text
URL
 │
 ▼
Feature Extraction
 │
 ├── URL Length
 ├── Number of Dots
 ├── HTTPS
 ├── IP Address
 ├── Subdirectories
 ├── Parameters
 ├── Suspicious Words
 ├── Special Characters
 ├── Digits
 └── Entropy
 │
 ▼
Random Forest Model
 │
 ▼
Prediction
```

---

# 🌐 API Endpoints

## Node.js Backend

### Scan URL

```text
POST /scan
```

Example request:

```json
{
  "input": "http://secure-login-example.com"
}
```

Example response:

```json
{
  "score": 51.8,
  "classification": "PHISHING",
  "reasons": [
    "The ML model detected phishing-like characteristics in this URL."
  ]
}
```

---

## Python Machine Learning API

### Predict URL

```text
POST /predict
```

Example request:

```json
{
  "url": "http://secure-login-example.com"
}
```

Example response:

```json
{
  "prediction": "PHISHING",
  "probability": 51.8
}
```

---

# 🖥️ Application Workflow

```text
1. User enters a URL
        │
        ▼
2. Frontend sends request
        │
        ▼
3. Node.js receives the request
        │
        ▼
4. Node.js sends URL to Flask API
        │
        ▼
5. Flask extracts URL features
        │
        ▼
6. Random Forest analyzes features
        │
        ▼
7. Prediction is generated
        │
        ▼
8. Result is sent back to the user
```

---

# 📊 Prediction Result

The application displays:

* Classification
* Risk Score
* Detection Information

Example:

```text
Detection Result

PHISHING

Risk Score: 51.8%

Detection Reasons:

⚠️ The ML model detected phishing-like characteristics
   in this URL.
```

---

# 📥 Dataset

The machine learning model is trained using a phishing URL dataset containing URL-based features.

The dataset contains features such as:

```text
url
label
url_length
num_dots
has_https
has_ip
num_subdirs
num_params
suspicious_words
tld
special_char_count
digits_count
entropy
```

Labels:

```text
0 → Legitimate / Safe
1 → Phishing
```

---

# ⚠️ Dataset Limitation

The original dataset used in this project is highly imbalanced.

Example:

```text
Phishing URLs:    159,244
Legitimate URLs:      820
```

To reduce class imbalance during training, the training process samples an equal number of phishing and legitimate URLs.

For future improvements, the model can be trained using a larger and more balanced dataset containing more legitimate URLs.

---

# 🔮 Future Improvements

The project can be improved by adding:

* 📧 Email phishing detection
* 💬 Scam message detection
* 📱 SMS scam detection
* 🔗 Real-time URL reputation checking
* 🧠 Advanced machine learning models
* 🗄️ Database for scan history
* 👤 User authentication
* 📊 User dashboard and analytics
* 🚨 Real-time security alerts
* 🌐 Deployment using Docker
* 🔐 Improved cybersecurity protection

---

# ⚠️ Disclaimer

This project is developed for educational and demonstration purposes.

The prediction generated by the machine learning model should not be considered a guarantee that a website is safe or malicious. Users should exercise caution when visiting unknown websites or entering sensitive information online.

---

# 👨‍💻 Author

**Chethan Kumar**

---

# ▶️ How to Run the Project

## 1. Clone the Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

Move into the project folder:

```bash
cd phishing_scam_detection
```

---

## 2. Create and Activate Python Virtual Environment

Create a virtual environment:

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

---

## 3. Install Python Dependencies

```bash
pip install flask scikit-learn pandas
```

If required:

```bash
pip install requests
```

---

## 4. Train the Machine Learning Model

Go to the ML folder:

```bash
cd ml
```

Run:

```bash
python train.py
```

This creates:

```text
model.pkl
features.pkl
```

---

## 5. Start the Flask Machine Learning API

Inside the `ml` folder:

```bash
python app.py
```

The Flask server will run on:

```text
http://127.0.0.1:5000
```

Keep this terminal running.

---

## 6. Start the Node.js Backend

Open a new terminal.

Go to the backend folder:

```bash
cd backend
```

Install dependencies:

```bash
npm install
```

Start the backend:

```bash
node server.js
```

The backend will run on:

```text
http://localhost:3000
```

Keep this terminal running.

---

## 7. Run the Frontend

Open the `Frontend` folder in Visual Studio Code.

Run the project using the **Live Server extension**.

The website will open at an address similar to:

```text
http://127.0.0.1:5500/Frontend/
```

---

# 🎯 Running Summary

Open three terminals/services:

### Terminal 1 — Flask ML API

```bash
cd ml
python app.py
```

### Terminal 2 — Node.js Backend

```bash
cd backend
node server.js
```

### Terminal 3 — Frontend

Open:

```text
Frontend/index.html
```

Run it using **Live Server**.

---

## 🛡️ Final Application Flow

```text
Frontend :5500
      │
      ▼
Node.js Backend :3000
      │
      ▼
Flask ML API :5000
      │
      ▼
Random Forest Model
      │
      ▼
PHISHING / SAFE Prediction
```

## ⭐ If you found this project useful

Consider giving the repository a ⭐ on GitHub.
