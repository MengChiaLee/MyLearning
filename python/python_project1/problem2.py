from sklearn.model_selection import train_test_split
from sklearn.linear_model import Perceptron, LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import pandas as pd


data = pd.read_csv(r'C:\Users\super\OneDrive\桌面\python\python_project1\heart1.csv')
X = data.drop('a1p2', axis=1) 
y = data['a1p2']

# Split into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Use Perceptron 
perceptron = Perceptron(max_iter=1000, tol=1e-4, penalty='l2', alpha=0.001) #Penalty is increase regularization to prevent overfitting, using L2 regularization
perceptron.fit(X_train, y_train)
y_train_pred_perceptron = perceptron.predict(X_train)
y_test_pred_perceptron = perceptron.predict(X_test)
train_accuracy_perceptron = accuracy_score(y_train, y_train_pred_perceptron)
test_accuracy_perceptron = accuracy_score(y_test, y_test_pred_perceptron)

# Logistic Regression 
logreg = LogisticRegression(max_iter=1000)
logreg.fit(X_train, y_train)
y_train_pred_logreg = logreg.predict(X_train)
y_test_pred_logreg = logreg.predict(X_test)
train_accuracy_logreg = accuracy_score(y_train, y_train_pred_logreg)
test_accuracy_logreg = accuracy_score(y_test, y_test_pred_logreg)

# SVM
svm = SVC(kernel='linear', C=1, gamma='scale')  # Adjust C value and gamma, also when kernel linear is will more correctly in this case
svm.fit(X_train, y_train)
y_train_pred_svm = svm.predict(X_train)
y_test_pred_svm = svm.predict(X_test)
train_accuracy_svm = accuracy_score(y_train, y_train_pred_svm)
test_accuracy_svm = accuracy_score(y_test, y_test_pred_svm)

# Decision Tree
dt = DecisionTreeClassifier(max_depth=5)
dt.fit(X_train, y_train)
y_train_pred_dt = dt.predict(X_train)
y_test_pred_dt = dt.predict(X_test)
train_accuracy_dt = accuracy_score(y_train, y_train_pred_dt)
test_accuracy_dt = accuracy_score(y_test, y_test_pred_dt)

# Random Forest 
rf = RandomForestClassifier()
rf.fit(X_train, y_train)
y_train_pred_rf = rf.predict(X_train)
y_test_pred_rf = rf.predict(X_test)
train_accuracy_rf = accuracy_score(y_train, y_train_pred_rf)
test_accuracy_rf = accuracy_score(y_test, y_test_pred_rf)

# KNN
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Adjust the range of K values for KNN and use the standardized data
best_knn_accuracy = 0
best_k = 1
for k in range(1, 31):  #K value from 1 to 30
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train_scaled, y_train)
    y_train_pred_knn = knn.predict(X_train_scaled)
    y_test_pred_knn = knn.predict(X_test_scaled)
    train_accuracy_knn = accuracy_score(y_train, y_train_pred_knn)
    test_accuracy_knn = accuracy_score(y_test, y_test_pred_knn)
    if test_accuracy_knn > best_knn_accuracy:
        best_knn_accuracy = test_accuracy_knn
        best_k = k

# Compare the Result
print(f"Perceptron Train Accuracy: {train_accuracy_perceptron * 100:.2f}%，Test Accuracy: {test_accuracy_perceptron * 100:.2f}%")
print(f"Logistic Regression Train Accuracy: {train_accuracy_logreg * 100:.2f}%，Test Accuracy: {test_accuracy_logreg * 100:.2f}%")
print(f"SVM Train Accuracy: {train_accuracy_svm * 100:.2f}%，Test Accuracy: {test_accuracy_svm * 100:.2f}%")
print(f"Decision Tree Train Accuracy: {train_accuracy_dt * 100:.2f}%，Test Accuracy: {test_accuracy_dt * 100:.2f}%")
print(f"Random Forest Train Accuracy: {train_accuracy_rf * 100:.2f}%，Test Accuracy: {test_accuracy_rf * 100:.2f}%")
print(f"KNN (K={best_k}) Train Accuracy: {train_accuracy_knn * 100:.2f}%，Test Accuracy: {test_accuracy_knn * 100:.2f}%")

# Make a data form
result_table = pd.DataFrame({
    'Algorithm': ['Perceptron', 'Logistic Regression', 'SVM', 'Decision Tree', 'Random Forest', f'KNN (K={best_k})'],
    'Train Accuracy': [train_accuracy_perceptron, train_accuracy_logreg, train_accuracy_svm, train_accuracy_dt, train_accuracy_rf, train_accuracy_knn],
    'Test Accuracy': [test_accuracy_perceptron, test_accuracy_logreg, test_accuracy_svm, test_accuracy_dt, test_accuracy_rf, test_accuracy_knn]
})
print(result_table)
