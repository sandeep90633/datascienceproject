# Wine Quality Prediction Pipeline

## Project Overview

This project builds an automated data pipeline to train and predict wine quality based on user inputs. The pipeline handles data ingestion, validation, transformation, model training, and prediction, and provides a Flask-based user interface for real-time interaction.

## Key features:

End-to-end automated pipeline for ML model lifecycle.

User input form via Flask app to predict wine quality.

Experiment tracking with MLflow for trained models.

Modular OOP-based design for configuration and pipeline management.

## Workflow

Data Ingestion – Downloads dataset from GitHub.

Data Validation – Ensures data consistency and quality.

Data Transformation – Preprocesses and splits data into train/test sets.

Model Training – Trains ML models and stores them.

Model Prediction – Uses trained model to predict wine quality from user inputs via Flask app.

## Tech Stack

Python – Data pipeline, OOPs-based configuration, preprocessing, and modeling.

Flask – User-friendly interface for predictions.

MLflow – Tracks experiments, parameters, and metrics.

## How to Run

Clone this repository:

```bash
git clone <repo-link>
cd <repo-folder>
```
Create a virtual environment:
```
conda create -p venv python=3.10 -y
conda activate venv/
```
Install dependencies:
```
pip install -r requirements.txt
```
Run the application:
```
python app.py
```

Open your browser and access the app – enter the input attributes to predict wine quality.