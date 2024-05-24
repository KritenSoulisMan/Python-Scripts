import pickle
import numpy as np

from sklearn.linear_model import LinearRegression

X = np.array([[1, 2], [3, 4], [5, 6]])
y = np.array([3, 7, 11])

model = LinearRegression()

# Обучение модели
model.fit(X, y)

# Сохранение модели в файл
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

# Загрузка модели из файла
with open('model.pkl', 'rb') as f:
    loaded_model = pickle.load(f)

# Использование загруженной модели для предсказаний
predictions = loaded_model.predict(model)
