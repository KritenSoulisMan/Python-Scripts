import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

# Загрузка данных
data = pd.read_csv("data.csv")
X = data.drop("target", axis=1)
y = data["target"]

# Разделение данных на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Обучение модели
model = LinearRegression()
model.fit(X_train, y_train)

# Запись параметров модели в файл
joblib.dump(model, "model.pkl")
