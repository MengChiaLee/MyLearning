import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats


data = pd.read_csv(r'C:\Users\super\OneDrive\桌面\python\python_project1\heart1.csv')
print(data.head())

#Calculate the correlation between each variable in the dataset
correlation_matrix = data.corr()

#Use np.tri() to create a lower triangular mask and set the lower-left corner to 0
mask = np.tri(*correlation_matrix.shape, k=-1, dtype=bool)
correlation_matrix = correlation_matrix.where(~mask, 0)

print("Modified Correlation Matrix (with lower triangle set to 0):")
print(correlation_matrix)

#Use a heatmap to enhance the visual effect
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Modified Correlation Matrix Heatmap')
plt.show()

#create covariance_matri
covariance_matrix = data.cov()
print("Covariance Matrix:")
print(covariance_matrix)

# draw Pair Plot
sns.pairplot(data)
plt.title('Pair Plot')
plt.show()

#Identify the variable most strongly correlated with 'a1p2'
correlation_with_target = correlation_matrix['a1p2'].sort_values(ascending=False)
print("Correlation with 'a1p2' (Heart Disease):")
print(correlation_with_target)

# Identify the top few most important features
important_features = correlation_with_target[1:5]  
print("最可能影響心臟疾病的變數包括：")
print(important_features)

