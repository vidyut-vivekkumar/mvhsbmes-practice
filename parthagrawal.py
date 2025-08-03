import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report

features = [
    "Alcohol",
    "Malic acid",
    "Ash",
    "Alcalinity of ash",
    "Magnesium",
    "Total phenols",
    "Flavanoids",
    "Nonflavanoid phenols",
    "Proanthocyanins",
    "Color intensity",
    "Hue",
    "OD280/OD315 of diluted wines",
    "Proline"
]

data = pd.read_csv('wine.data')
data = pd.read_csv(
    "wine.data",
    names= features,  # new column names
    header=None,                   # no header row in file
    index_col=False

)
print(data.head(2))
print(data.info())
print(data.shape)
y = data.iloc[:, :1]   # columns index 0
x = data.iloc[:, 1:]
print(x.head(2))
print(y.head(2))

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42, stratify=y
)
print(len(x_test))
print(y_test['Alcohol'].value_counts())

scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)

knn = KNeighborsClassifier(n_neighbors=5)  # you can tune k
knn.fit(x_train_scaled, y_train["Alcohol"])

y_pred = knn.predict(x_test_scaled)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification report:\n", classification_report(y_test, y_pred))