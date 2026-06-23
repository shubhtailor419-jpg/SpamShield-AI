# SpamShield AI

## Overview

SpamShield AI is a Machine Learning-powered web application built with Streamlit that identifies whether a message is Spam or Ham (legitimate). The application supports both single-message analysis and bulk CSV-based spam detection, making it useful for message filtering, educational projects, and machine learning demonstrations.

## Features

* Real-time spam message prediction
* Confidence score display for each prediction
* Bulk spam detection using CSV file uploads
* Download prediction results as CSV
* Dataset preview and statistics dashboard
* Interactive and user-friendly Streamlit interface

## Technologies Used

* Python
* Streamlit
* Scikit-learn
* Pandas
* Joblib

## Project Structure

```text
SpamShield-AI/
│
├── app.py
├── spam_model.pkl
├── vectorizer.pkl
├── spam.csv
├── requirements.txt
└── README.md
```

## Installation

### Clone the Repository

```bash
git clone https://github.com/yourusername/SpamShield-AI.git
cd SpamShield-AI
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
streamlit run app.py
```

## Usage

### Single Prediction

1. Navigate to the Single Prediction tab.
2. Enter a message.
3. Click **Analyze Message**.
4. View the prediction result and confidence score.

### Bulk Detection

1. Navigate to the Bulk Detection tab.
2. Upload a CSV file containing a `text` column.
3. Click **Detect Spam**.
4. Download the generated prediction results.

### Dataset Preview

* View sample records from the dataset.
* Check total records.
* View spam and ham message statistics.

## Sample Dataset Format

```csv
text
Congratulations! You've won a free prize.
Hey, are we still meeting today?
Limited offer! Claim your reward now.
```

## Future Enhancements

* Advanced visualization dashboard
* Multiple machine learning model comparison
* Deep Learning-based spam classification
* Email integration
* API deployment support
* Real-time message monitoring

## Author

**Shubh Tailor**

Aspiring Data Analyst and Machine Learning Enthusiast passionate about building practical AI-powered applications.

## Acknowledgements

* Streamlit Team
* Scikit-learn Community
* Open Source Python Ecosystem
