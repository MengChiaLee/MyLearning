# PCA example
# author: Allee, Hartin updated by sdm

import numpy as np                                     # needed for arrays
import pandas as pd                                    # data frame
import matplotlib.pyplot as plt                        # modifying plot
from sklearn.model_selection import train_test_split   # splitting data
from sklearn.preprocessing import StandardScaler       # scaling data
from sklearn.linear_model import LogisticRegression    # learning algorithm
from sklearn.decomposition import PCA                  # PCA package
from sklearn.metrics import accuracy_score             # grading
from sklearn.metrics import confusion_matrix           # generate the  matrix
from m5_plotdr import plot_decision_regions            # fancy plot

# read the database. Since it lacks headers, put them in
df_wine = pd.read_csv('m6_wine.csv',header=None)
df_wine.columns = ['class label','alcohol','malic acid','ash',
                   'alcalinity of ash','magnesium','total phenols','flavanoids',
                   'nonflavanoid phenols','proanthocyanins','color intensity',
                   'hue','od280/0d315 of diluted wines','proline']

# list out the labels
print('Class labels', np.unique(df_wine['class label']))

X = df_wine.iloc[:,1:].values       # features are in columns 1:(N-1)
y = df_wine.iloc[:,0].values        # classes are in column 0!

# now split the data
X_train, X_test, y_train, y_test = \
         train_test_split(X, y, test_size=0.3, random_state=0)

stdsc = StandardScaler()                     # apply standardization
X_train_std = stdsc.fit_transform(X_train)
X_test_std = stdsc.transform(X_test) 

# NOTE: only keep two features as that's all plot_decision_regions can handle!

pca = PCA(n_components=2)                    # only keep two "best" features!
X_train_pca = pca.fit_transform(X_train_std) # apply to the train data
X_test_pca = pca.transform(X_test_std)       # do the same to the test data

# now create a Logistic Regression and train on it
lr = LogisticRegression(solver='liblinear', multi_class='ovr')
lr.fit(X_train_pca,y_train)

y_pred = lr.predict(X_test_pca)              # how do we do on the test data?
print('Number in test ',len(y_test))
print('Misclassified samples: %d' % (y_test != y_pred).sum())
print('Accuracy: %.2f' % accuracy_score(y_test, y_pred))

# now combine the train and test data and see how we do
X_comb_pca = np.vstack((X_train_pca, X_test_pca))
y_comb = np.hstack((y_train, y_test))
print('Number in combined ',len(y_comb))
y_comb_pred = lr.predict(X_comb_pca)
print('Misclassified combined samples: %d' % (y_comb != y_comb_pred).sum())
print('Combined Accuracy: %.2f' % accuracy_score(y_comb, y_comb_pred))

confuse = confusion_matrix(y_comb,y_comb_pred)
print(confuse)

# Now visualize the results
plot_decision_regions(X_train_pca, y_train, classifier=lr)
plt.xlabel('PC 1')
plt.ylabel('PC 2')
plt.legend(loc='lower left')
plt.title('wine analysis with two components')
plt.show()
