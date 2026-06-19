# Cyberbullying Detection on Social Media

## Overview

This project aims to detect cyberbullying and offensive content on social media platforms using Natural Language Processing (NLP) and Machine Learning techniques. The system analyzes user comments and classifies them as bullying or non-bullying based on a trained machine learning model.

---

## Objectives

* Detect harmful and offensive comments.
* Apply NLP techniques for text preprocessing.
* Train a machine learning model for text classification.
* Provide a user-friendly interface for testing comments.

---

## Dataset

* Social media comments dataset
* Approximately 27,000 records
* Contains comment text and corresponding class labels

---

## Technologies Used

* Python
* Pandas
* NumPy
* Regex
* NLTK
* Scikit-Learn
* Streamlit

---

## Project Workflow

1. Data Collection
2. Data Exploration
3. Data Cleaning
4. Text Preprocessing
5. Feature Extraction (TF-IDF)
6. Machine Learning Model Training
7. Model Evaluation
8. User Interface Development
9. Prediction System

---

## Current Progress

### Week 1 Completed

* Project topic finalized
* Dataset collected
* Dataset loaded using Pandas
* Dataset exploration completed
* DataFrame and Series operations performed
* Column selection completed
* Dataset columns renamed for better readability
* Basic dataset analysis completed using:

  * read_csv()
  * head()
  * tail()
  * shape
  * columns
  * info()
  * describe()

### Week 2 Completed

* Missing value analysis performed
* Missing values removed from dataset
* Duplicate record detection completed
* Duplicate records removed
* Class distribution analysis completed
* Dataset validation performed
* Cleaned dataset generated and saved for further processing

---

## Upcoming Work

### Week 3

* Regex-based text preprocessing
* Lowercase conversion
* URL removal
* Punctuation removal
* Number removal
* Extra space removal
* Tokenization
* Stopword removal

### Future Phases

* Lemmatization
* TF-IDF implementation
* Train-Test Split
* Logistic Regression model training
* Model evaluation
* Model saving using Pickle
* Streamlit UI development
* Final project deployment

---

## Expected Output

The system will classify a given social media comment as:

* Cyberbullying
* Non-Cyberbullying

Example:

Input:
"You are stupid and useless"

Output:
"Cyberbullying Detected"

---

## Author

**Vivek Choudhary**
B.Tech CSE (Cyber Security)
Graphic Era Deemed to be University
