import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics

df = pd.read_csv('/wine.data', header=None)
y = df[0].values
X = df.iloc[:, 1:13].values

X_temp, X_test, y_temp, y_test = train_test_split(X, y, test_size=0.2, shuffle=True, random_state=10, stratify=y)
X_train, X_valid, y_train, y_valid = train_test_split(X_temp, y_temp, test_size=0.2, shuffle=True, random_state=10, stratify=y_temp)

scaler = StandardScaler()
scaler.fit(X_train)
X_train_std = scaler.transform(X_train)
X_valid_std = scaler.transform(X_valid)
X_test_std = scaler.transform(X_test)

clf = KNeighborsClassifier()
clf.fit(X_train, y_train)
train_prediction = clf.predict(X_train)
test_prediction = clf.predict(X_test)
print(metrics.classification_report(y_train, train_prediction, digits=3))