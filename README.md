# Cyberbullying Detection on Social Media

## Overview

This project aims to detect cyberbullying and offensive content on social media platforms using Natural Language Processing (NLP) and Machine Learning techniques. The system analyzes user comments and classifies them as bullying or non-bullying using a trained machine learning model.

---

## Objectives

- Detect harmful and offensive comments.
- Clean and preprocess social media text.
- Apply NLP techniques for feature extraction.
- Train a machine learning model for classification.
- Develop a simple user interface for prediction.

---

## Dataset

- Social Media Comments Dataset
- Approximately 27,000 records
- Contains comment text and class labels

---

## Technologies Used

- Python
- Pandas
- NumPy
- Regular Expressions (Regex)
- NLTK
- Scikit-Learn
- Streamlit

---

## Project Workflow

1. Data Collection
2. Data Exploration
3. Data Cleaning
4. Text Preprocessing
5. Feature Extraction
6. Machine Learning Model Training
7. Model Evaluation
8. User Interface Development

---

## Current Progress

### Week 1 - Dataset Exploration

- Dataset collected and loaded
- DataFrame exploration completed
- Column selection performed
- Column renaming completed
- Dataset structure analyzed using:
  - head()
  - tail()
  - shape
  - info()
  - describe()

### Week 2 - Data Cleaning

- Missing value analysis completed
- Missing values removed
- Duplicate records detected and removed
- Dataset validation completed
- Clean dataset generated

### Week 3 - Text Preprocessing

- Regex-based text cleaning implemented
- Converted text to lowercase
- Removed URLs
- Removed punctuation
- Removed numbers
- Removed extra spaces
- Tokenization implemented using NLTK
- Stopword removal completed
- Preprocessed dataset generated and saved

---

## Upcoming Work

### Week 4

- Lemmatization
- TF-IDF Feature Extraction
- Train-Test Split
- Logistic Regression Model Training

### Week 5

- Model Evaluation
- Accuracy Score
- Precision, Recall, F1 Score
- Confusion Matrix
- Model Saving using Pickle
- Streamlit UI Development
- Final Project Integration

-
- Author
-  Vivek Choudhary
B.Tech CSE (Cyber Security)
Graphic Era Deemed to be University

---

## Expected Output

Input:

```text
You are stupid and useless

Output:

Cyberbullying Detected

Input:

Have a nice day

Output:

Non-Cyberbullying



