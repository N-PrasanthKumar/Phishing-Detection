# Phishing Website Detection

This project is a machine learning application designed to detect phishing websites based on features extracted from URLs. The system uses a Flask-based web interface to interact with users and make predictions.

---

## **Introduction**

Phishing attacks are a significant threat in cybersecurity, as attackers attempt to steal sensitive information by tricking users into visiting fraudulent websites. This project aims to detect phishing websites by analyzing various features extracted from URLs, leveraging machine learning for accurate classification. The goal is to provide an easy-to-use web application for users to check the legitimacy of a website.

---

## **Project Overview**

This project utilizes:
- **Machine Learning**: A trained classification model predicts whether a given URL is a phishing attempt or legitimate.
- **Feature Extraction**: URL-based features, such as length, special characters, and domain details, are analyzed for predictions.
- **Flask Framework**: A lightweight Python-based web application framework is used to create the front-end interface.
- **Dataset**: The model is trained on a labeled dataset (`phishing.csv`) containing legitimate and phishing URLs.
- **Web Application**: Users can input URLs into a simple interface to receive instant predictions.

The project provides an interactive and user-friendly way to enhance cybersecurity awareness and protection against phishing threats.

---

## Project Structure

- **templates/**: Contains HTML templates for the Flask web app.
  - `index.html`: Main page where users input a URL for classification.
- **pickle/**: Folder containing serialized model files.
  - `model.pkl`: Trained machine learning model for phishing URL detection.
- **app.py**: Main script that runs the Flask web application.
- **requirements.txt**: Lists the dependencies required for the project.
- **phishing URL Detection.ipynb**: Jupyter Notebook for data exploration, feature extraction, model training, and evaluation.
- **phishing.csv**: The dataset used to train and test the phishing detection model.
- **feature.py**: Contains functions to extract relevant features from URLs for classification.
- **__pycache__/**: Folder containing Python bytecode files (automatically generated).

---
### Installation

1. Clone this repository to your local machine.
2. Install dependencies by running the following command:

   ```bash
   pip install -r requirements.txt
----------
### result Pages
![ligistimate image Page](https://github.com/N-PrasanthKumar/Phishing-Detection/blob/main/images/legitimate.png)


![phishing image Page](https://github.com/N-PrasanthKumar/Phishing-Detection/blob/main/images/phishing.png)

   
