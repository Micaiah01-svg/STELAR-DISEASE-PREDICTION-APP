<img width="2559" height="1372" alt="image" src="https://github.com/user-attachments/assets/09eabce0-4122-46f6-8ec4-4f079b5890dd" />



**STELAR Disease Prediction App**

A symptom-based machine learning web application built with \*\*Streamlit\*\* that predicts the most likely disease from user-selected symptoms.

**Live Demo**

[View the deployed app here](https://stelar-disease-prediction-app-ztzpgdeaawkwkzp4vhkqt8.streamlit.app/)

**Overview**

The **STELAR Disease Prediction App** was developed as part of a machine learning project to demonstrate the end-to-end process of building a deployable ML application.

The app allows users to:

\- select symptoms from a predefined list

\- generate a disease prediction using a trained machine learning model

\- view the top predicted outcomes in an interactive interface

This project combines data preprocessing, model training, model serialization, web app development, and deployment into one complete workflow.

**Features**

- Symptom-based disease prediction
- Interactive web interface built with Streamlit
- Top 3 predicted disease outcomes
- Clean and simple user experience
- Deployment-ready project structure

**Tools**

- Python
- Pandas
- Scikit-learn
- Joblib
- Streamlit

**Machine Learning Workflow**

The development process included:

1\. Sourcing a disease-and-symptoms dataset from Kaggle

2\. Loading and exploring the dataset

3\. Identifying the correct dataset file from multiple CSV files

4\. Cleaning the data and separating the \`Disease\` target column from symptom columns

5\. Converting symptom text into machine-readable binary features using MultiLabelBinarizer.

6\. Splitting the dataset into training and testing sets

7\. Training a RandomForestClassifier.

8\. Evaluating model performance

9\. Saving the trained model and encoder using Joblib.

**Project Structure**

- STELAR-Disease-Prediction-App/
- │── app.py
- │── disease_model.pkl
- │── symptom_encoder.pkl
- │── requirements.txt
- │── README.md

**Installation and Setup**

**1\. Clone the repository**

git clone https://github.com/[Micaiah01-svg](https://github.com/Micaiah01-svg)/[STELAR-DISEASE-PREDICTION-APP](https://github.com/Micaiah01-svg/STELAR-DISEASE-PREDICTION-APP).git

**2\. Navigate into the project folder**

cd STELAR-DISEASE-PREDICTION-APP

**3\. Install dependencies**

pip install -r requirements.txt

**4\. Run the application**

streamlit run app.py

**How to Use**

1.  Launch the app locally or open the deployed version
2.  Select one or more symptoms from the dropdown menu
3.  Click **Predict Disease**
4.  View the most likely disease prediction and top results

**Deployment**

The application was deployed using:

- **GitHub**
- **Streamlit Community Cloud**

**Disclaimer**

This project is intended for **educational and demonstration purposes only**.  
It is **not a medical diagnosis system**, and its predictions should not be treated as professional healthcare advice.


**Author**

Micaiah Adeoluwa Adedeji
