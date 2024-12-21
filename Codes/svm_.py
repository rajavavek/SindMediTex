# -*- coding: utf-8 -*-
"""SVM .ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1GrbzpXPLExG12B_vrMSPprqbaq4ghelF
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import GridSearchCV

# Load dataset
url = 'https://github.com/rajavavek/SindMediTex/blob/main/SindMediTex.csv?raw=true'
data = pd.read_csv(url)

# Inspect dataset
print(data.head())

# Dataset columns
text_column = "Text"
label_column = "Label"

# Preprocess labels
label_encoder = LabelEncoder()
data[label_column] = label_encoder.fit_transform(data[label_column])
labels = data[label_column].values

# Preprocess text
train_texts, test_texts, train_labels, test_labels = train_test_split(
    data[text_column], labels, test_size=0.2, random_state=42
)

# Create a pipeline with TF-IDF and SVM classifier
svm_model = make_pipeline(
    TfidfVectorizer(max_features=5000),  # Use a TF-IDF vectorizer to extract features
    SVC(kernel='linear', C=1)  # Use SVM with a linear kernel
)

# Train the model
svm_model.fit(train_texts, train_labels)

# Predict on test data
predictions = svm_model.predict(test_texts)

# Evaluate the model
accuracy = accuracy_score(test_labels, predictions)
print(f"Test Accuracy: {accuracy:.2f}")

# Print classification report
print(classification_report(test_labels, predictions, target_names=label_encoder.classes_))

# Plot training accuracy and validation accuracy (from cross-validation if used)
# This part is optional, as SVM doesn't have built-in training history like deep learning models
# but we can use GridSearchCV for hyperparameter tuning to track accuracy for each fold.

# Define parameter grid for tuning SVM
param_grid = {
    'svc__C': [0.1, 1, 10],  # Regularization parameter
    'svc__kernel': ['linear', 'rbf'],  # Types of kernels
}

# Perform Grid Search
grid_search = GridSearchCV(svm_model, param_grid, cv=3, n_jobs=-1, verbose=2)
grid_search.fit(train_texts, train_labels)

# Best parameters from Grid Search
print("Best Parameters:", grid_search.best_params_)

# Predict with the best model
best_model = grid_search.best_estimator_
predictions = best_model.predict(test_texts)

# Evaluate the best model
accuracy = accuracy_score(test_labels, predictions)
print(f"Test Accuracy: {accuracy:.2f}")

# Print classification report
print(classification_report(test_labels, predictions, target_names=label_encoder.classes_))

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.pipeline import make_pipeline
import seaborn as sns

# Load dataset
url = 'https://github.com/rajavavek/SindMediTex/blob/main/SindMediTex.csv?raw=true'
data = pd.read_csv(url)

# Inspect dataset
print(data.head())

# Dataset columns
text_column = "Text"
label_column = "Label"

# Preprocess labels
label_encoder = LabelEncoder()
data[label_column] = label_encoder.fit_transform(data[label_column])
labels = data[label_column].values

# Preprocess text
train_texts, test_texts, train_labels, test_labels = train_test_split(
    data[text_column], labels, test_size=0.2, random_state=42
)

# Create a pipeline with TF-IDF and SVM classifier
svm_model = make_pipeline(
    TfidfVectorizer(max_features=5000),  # Use a TF-IDF vectorizer to extract features
    SVC(kernel='linear', C=1)  # Use SVM with a linear kernel
)

# Train the model
svm_model.fit(train_texts, train_labels)

# Predict on test data
predictions = svm_model.predict(test_texts)

# Evaluate the model
accuracy = accuracy_score(test_labels, predictions)
print(f"Test Accuracy: {accuracy:.2f}")

# Print classification report
report = classification_report(test_labels, predictions, target_names=label_encoder.classes_)
print(report)

# Plot the classification report as a bar plot
report_dict = classification_report(test_labels, predictions, target_names=label_encoder.classes_, output_dict=True)
df_report = pd.DataFrame(report_dict).transpose()

# Remove accuracy row (it might not exist)
if 'accuracy' in df_report.index:
    df_report.drop('accuracy', axis=0, inplace=True)  # Drop 'accuracy' row from the report

# Plot precision, recall, and F1 score for each class
df_report.plot(kind='bar', figsize=(10, 6))
plt.title('Precision, Recall, and F1 Score for Each Class')
plt.ylabel('Score')
plt.xlabel('Class')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Confusion Matrix Plot
cm = confusion_matrix(test_labels, predictions)
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=label_encoder.classes_, yticklabels=label_encoder.classes_)
plt.title('Confusion Matrix')
plt.xlabel('Predicted Labels')
plt.ylabel('True Labels')
plt.tight_layout()
plt.show()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.pipeline import make_pipeline
import seaborn as sns

# Load dataset
url = 'https://github.com/rajavavek/SindMediTex/blob/main/SindMediTex.csv?raw=true'
data = pd.read_csv(url)

# Inspect dataset
print(data.head())

# Dataset columns
text_column = "Text"
label_column = "Label"

# Preprocess labels
label_encoder = LabelEncoder()
data[label_column] = label_encoder.fit_transform(data[label_column])
labels = data[label_column].values

# Preprocess text
train_texts, test_texts, train_labels, test_labels = train_test_split(
    data[text_column], labels, test_size=0.2, random_state=42
)

# Create a pipeline with TF-IDF and SVM classifier
svm_model = make_pipeline(
    TfidfVectorizer(max_features=5000),  # Use a TF-IDF vectorizer to extract features
    SVC(kernel='linear', C=1)  # Use SVM with a linear kernel
)

# Train the model
svm_model.fit(train_texts, train_labels)

# Predict on test data
predictions = svm_model.predict(test_texts)

# Evaluate the model
accuracy = accuracy_score(test_labels, predictions)
print(f"Test Accuracy: {accuracy:.2f}")

# Print classification report
report = classification_report(test_labels, predictions, target_names=label_encoder.classes_)
print(report)

# Plot the classification report as a bar plot
report_dict = classification_report(test_labels, predictions, target_names=label_encoder.classes_, output_dict=True)
df_report = pd.DataFrame(report_dict).transpose()

# Extract precision, recall, and F1-score for each class (excluding 'accuracy' row)
df_report = df_report.drop('accuracy', axis=0, errors='ignore')

# Plot precision, recall, and F1 score for each class
df_report[['precision', 'recall', 'f1-score']].plot(kind='bar', figsize=(10, 6))
plt.title('Precision, Recall, and F1 Score for Each Class')
plt.ylabel('Score')
plt.xlabel('Class')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Confusion Matrix Plot
cm = confusion_matrix(test_labels, predictions)
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=label_encoder.classes_, yticklabels=label_encoder.classes_)
plt.title('Confusion Matrix')
plt.xlabel('Predicted Labels')
plt.ylabel('True Labels')
plt.tight_layout()
plt.show()