import pandas as pd
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import GaussianNB
import pickle as pk


def training(dataset: pd.DataFrame):
    X = dataset.iloc[:, :len(dataset.columns) - 2]
    X.columns = X.columns.astype('str')
    y = dataset.iloc[:, len(dataset.columns) - 1]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

    standard_scaler = StandardScaler()
    X_train = standard_scaler.fit_transform(X_train)
    X_test = standard_scaler.transform(X_test)

    gnb = GaussianNB()
    y_pred = gnb.fit(X_train, y_train).predict(X_test)

    accuracy = confusion_matrix(y_pred, y_test)
    print("Accuracy: ", accuracy)

    with open('./nd_supervised_models/linear_regression.pkl', 'wb') as f:
        pk.dump(gnb, f)