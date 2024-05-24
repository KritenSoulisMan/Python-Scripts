import re
import requests
from urllib.parse import quote
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Функция для транслитерации
def transliterate(text):
    text = re.sub(r'[ъь]', 'y', text)
    text = re.sub(r'[щшч]', 'sh', text)
    # и т.д. для остальных букв

    return text

# Скачиваем статьи    
topics = ["Машинное обучение", "Искусственный интеллект", "Робототехника"]
labels = ['ML', 'AI', 'Robotics']

articles = []
for topic in topics:
    url = "https://ru.wikipedia.org/wiki/" + quote(transliterate(topic))
    article = requests.get(url).text
    articles.append(article)
    
# Обучение и классификация как в предыдущем примере

# ... код для обучения модели и классификации  

# Извлекаем признаки 
vectorizer = CountVectorizer()
features = vectorizer.fit_transform(articles)

# Обучаем классификатор
model = MultinomialNB()
model.fit(features, labels)

# Цикл самообучения
while True:
  
  # Запрашиваем новую статью
  topic = input("Введите тему для классификации: ")
  url = "https://en.wikipedia.org/wiki/" + topic
  articles = articles(url)
  articles.download()
  articles.parse()
  
  # Извлекаем признаки
  new_features = vectorizer.transform([article.text]) 
  
  # Классифицируем
  prediction = model.predict(new_features)[0]
  print(prediction)

  # Предлагаем пользователю подтвердить метку
  actual_label = input("Подтвердите метку (y/n): ")
  
  if actual_label == 'y':
    # Добавляем новые данные в обучающую выборку
    features = np.vstack([features, new_features])
    labels.append(prediction)
    model.fit(features, labels) # Переобучаем
    
  print("Модель обучена на {} объектах".format(len(labels)))
