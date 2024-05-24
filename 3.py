mport pandas as pd
from sklearn.linear_model import LinearRegression

# Загрузка данных для обучения модели
data = pd.read_csv('path_to_your_data.csv')  # путь к файлу с данными
X = data[['feature1', 'feature2', ...]]  # Здесь укажите названия признаков, которые будут использоваться для обучения
y = data['target_variable']  # Здесь укажите название целевой переменной, которую нужно предсказать

# Создание объекта модели регрессии
model = LinearRegression()

# Обучение модели на обучающих данных
model.fit(X, y)

# Предсказание на новых данных
new_data = pd.read_csv('path_to_new_data.csv')  # путь к файлу с новыми данными для предсказания
predictions = model.predict(new_data)

# Вывод предсказаний
print(predictions)
