from googlesearch import search

# Функция для выполнения поискового запроса и получения ссылок на сайты
def get_search_results(query):
    links = []  # Здесь исправленная строка
    for result in search(query, num_results=5):
        links.append(result)
    return links

# Пример использования функции для получения ссылок на сайты
user_query = input("Введите запрос: ")
search_results = get_search_results(user_query)

# Вывод ссылок на сайты
for link in search_results:
    print(link)

