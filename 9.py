import wikipedia
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Получение текста со страницы Wikipedia на русском языке
def get_text_from_wikipedia(page_title):
    page = wikipedia.page(page_title)
    return page.content

# Загрузка текстов
positive_text = get_text_from_wikipedia("Художественная литература")
negative_text = get_text_from_wikipedia("Математика")

# Создание списка меток (1 для положительных текстов, 0 для отрицательных текстов)
labels = [1] * len(positive_text) + [0] * len(negative_text)

# Объединение положительных и отрицательных текстов
texts = positive_text + negative_text

# Преобразование текстов в числовой вид с помощью параметризации TF-IDF
vectorizer = TfidfVectorizer()
features = vectorizer.fit_transform(texts)

# Разделение данных на обучающий и тестовый наборы
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

# Обучение модели с использованием случайного леса
classifier = RandomForestClassifier()
classifier.fit(X_train, y_train)

# Предсказание меток для тестового набора
y_pred = classifier.predict(X_test)

# Оценка точности модели
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
