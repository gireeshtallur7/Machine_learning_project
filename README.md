
# 🎓 Student Exam Performance Predictor

End to End a Machine Learning web application that predicts a student's Mathematics score based on demographic and academic features. The application is built using **Python**, **Flask**, **Scikit-learn**, and deployed on **AWS Elastic Beanstalk**.

---

## 🚀 Live Demo

🔗 AWS Elastic Beanstalk Deployment

[https://YOUR-ELASTIC-BEANSTALK-DOMAIN/predictdata](http://studentperformanceapplication-env.eba-4mchcewy.us-east-1.elasticbeanstalk.com/predictdata)

---

## 📌 Project Overview

The objective of this project is to predict a student's Mathematics score using Machine Learning techniques. The application accepts user input through a Flask web interface, preprocesses the data using a trained pipeline, and predicts the Mathematics score using the best-performing regression model.

---

## ✨ Features

- Predicts Mathematics score instantly
- Interactive Flask web application
- End-to-end Machine Learning pipeline
- Data preprocessing using Scikit-learn Pipeline
- Automatic handling of categorical and numerical features
- Model serialization using Dill
- Modular project architecture
- Custom exception handling
- Logging for debugging
- Deployable on AWS Elastic Beanstalk

---

## 🛠️ Tech Stack

### Programming Language

- Python 3.12

### Machine Learning

- Scikit-learn
- Linear Regression
- GridSearchCV

### Data Processing

- Pandas
- NumPy

### Web Framework

- Flask

### Deployment

- AWS Elastic Beanstalk
- Gunicorn

### Model Serialization

- Dill

### Version Control

- Git
- GitHub

---

## 📂 Project Structure

```
machine_learning_project/
│
├── SOURCE/
│   ├── components/
│   │   ├── data_ingestions.py
│   │   ├── data_transformation.py
│   │   ├── training_model.py
│   │
│   ├── pipelines/
│   │   ├── prediction_pipelines.py
│   │   └── train_pipeline.py
│   │
│   ├── logger.py
│   ├── exception.py
│   └── ulits.py
│
├── templates/
├── static/
├── artifacts/
├── artifact_model/
├── app.py
├── setup.py
├── requirements.txt
├── Procfile
└── README.md
```

---

## 📊 Dataset

The project uses the **Student Performance Dataset**, containing information such as:

- Gender
- Race / Ethnicity
- Parental Level of Education
- Lunch Type
- Test Preparation Course
- Reading Score
- Writing Score

### Target Variable

- Mathematics Score

---

## ⚙️ Machine Learning Workflow

1. Data Collection
2. Data Ingestion
3. Data Validation
4. Data Preprocessing
5. Feature Engineering
6. Model Training
7. Hyperparameter Tuning using GridSearchCV
8. Model Evaluation
9. Model Serialization
10. Flask Application Development
11. AWS Deployment

---

## 🧠 Model Used

- Linear Regression

The model is trained using Scikit-learn and evaluated using the R² Score.

---

## 📈 Evaluation Metric

- R² Score (Coefficient of Determination)

---

## 🌐 Deployment

The application is deployed using:

- AWS Elastic Beanstalk
- Gunicorn
- Python 3.12 Environment

Deployment includes:

- Flask Application
- Serialized Machine Learning Model
- Preprocessing Pipeline
- Static Files
- HTML Templates


## 📸 Application Preview

### Home Page

(Add screenshot here)

### Prediction Page

<img width="1334" height="728" alt="image" src="https://github.com/user-attachments/assets/593fea26-a8f1-4170-a655-eec6113cb707" />


---

## 🔮 Future Improvements

- Add multiple regression algorithms comparison
- Model performance dashboard
- Docker containerization
- CI/CD using GitHub Actions
- User authentication
- Input validation
- Database integration
- CloudWatch monitoring

---

## 💼 Resume Highlights

This project demonstrates experience in:

- Machine Learning
- Data Preprocessing
- Feature Engineering
- Model Training
- Hyperparameter Tuning
- Scikit-learn Pipelines
- Flask Web Development
- AWS Elastic Beanstalk Deployment
- Model Serialization
- REST-based Web Application
- Software Engineering Best Practices

---

## 👨‍💻 Author

**Gireesh Tallur**

GitHub:
https://github.com/gireeshtallur7

LinkedIn:
(Add your LinkedIn profile)

---

## ⭐ If you found this project useful, please give it a star!
