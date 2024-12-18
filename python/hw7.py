import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Perceptron, LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Load the data
data = pd.read_csv(r'C:\Users\super\OneDrive\桌面\python\python_project1\heart1.csv')
X = data.drop('a1p2', axis=1) 
y = data['a1p2']

# Split into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Function to train and evaluate models
def train_and_evaluate_model(model, X_train, X_test, y_train, y_test):
    model.fit(X_train, y_train)
    y_test_pred = model.predict(X_test)
    test_accuracy = accuracy_score(y_test, y_test_pred)
    return y_test_pred, test_accuracy

# Prepare models (using the same configurations as in the original script)
# Note: For KNN, we'll use the best K from the original script
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Individual models
models = [
    ('Logistic Regression', LogisticRegression(max_iter=1000)),
    ('SVM', SVC(kernel='linear', C=1, gamma='scale')),
    ('Random Forest', RandomForestClassifier()),
    ('Decision Tree', DecisionTreeClassifier(max_depth=5)),
    ('Perceptron', Perceptron(max_iter=1000, tol=1e-4, penalty='l2', alpha=0.001)),
    ('KNN', KNeighborsClassifier(n_neighbors=7))  # Using K=7 as an example
]

# Evaluate individual models
individual_results = []
predictions = []

print("Individual Model Accuracies:")
for name, model in models:
    # For KNN, use scaled data
    if name == 'KNN':
        y_test_pred, test_accuracy = train_and_evaluate_model(model, X_train_scaled, X_test_scaled, y_train, y_test)
    else:
        y_test_pred, test_accuracy = train_and_evaluate_model(model, X_train, X_test, y_train, y_test)
    
    individual_results.append((name, test_accuracy))
    predictions.append(y_test_pred)
    print(f"{name}: {test_accuracy * 100:.2f}%")

# Sort models by accuracy
sorted_models = sorted(individual_results, key=lambda x: x[1], reverse=True)

# Ensemble methods
def ensemble_predict(predictions, num_methods, tie_handling='greater'):
    # Sum up predictions
    sum_predictions = np.sum(predictions[:num_methods], axis=0)
    
    # Determine threshold based on number of methods
    if tie_handling == 'greater':
        thresh = num_methods * 1.5  # e.g., for 3 methods: 4.5, for 4 methods: 6
        results = np.where(sum_predictions > thresh, 2, 1)
    else:  # 'greater_equal'
        thresh = num_methods * 1.5  # e.g., for 3 methods: 4.5, for 4 methods: 6
        results = np.where(sum_predictions >= thresh, 2, 1)
    
    return results, accuracy_score(y_test, results)

# Ensemble with top 3 methods
top_3_indices = [models.index(next(m for m in models if m[0] == name)) for name, _ in sorted_models[:3]]
top_3_predictions = [predictions[i] for i in top_3_indices]
ensemble_3_results, ensemble_3_accuracy = ensemble_predict(top_3_predictions, 3)
print(f"\nEnsemble with top 3 methods: {ensemble_3_accuracy * 100:.2f}%")

# Ensemble with top 4 methods
top_4_indices = [models.index(next(m for m in models if m[0] == name)) for name, _ in sorted_models[:4]]
top_4_predictions = [predictions[i] for i in top_4_indices]

# Try both tie-breaking methods
ensemble_4_results_greater, ensemble_4_accuracy_greater = ensemble_predict(top_4_predictions, 4, 'greater')
ensemble_4_results_greater_equal, ensemble_4_accuracy_greater_equal = ensemble_predict(top_4_predictions, 4, 'greater_equal')

print(f"Ensemble with top 4 methods (ties > 1.5 * methods): {ensemble_4_accuracy_greater * 100:.2f}%")
print(f"Ensemble with top 4 methods (ties >= 1.5 * methods): {ensemble_4_accuracy_greater_equal * 100:.2f}%")

# Ensemble with top 5 methods
top_5_indices = [models.index(next(m for m in models if m[0] == name)) for name, _ in sorted_models[:5]]
top_5_predictions = [predictions[i] for i in top_5_indices]
ensemble_5_results, ensemble_5_accuracy = ensemble_predict(top_5_predictions, 5)
print(f"Ensemble with top 5 methods: {ensemble_5_accuracy * 100:.2f}%")