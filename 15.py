import requests
from bs4 import BeautifulSoup

response = requests.get(url)
content = response.text

soup = BeautifulSoup(content, 'html.parser')

class Central:
    def start(self):
        print("Привет! Что вы хотели?")
        action = input()

        if action == "парсин":
            print("Введите URL сайта для парсинга:")
            url = input()
            self.parse_website(url)
        elif action == "гугл":
            print("Введите запрос для поиска в Google:")
            query = input()
            self.google_search(query)
        else:
            print("Извините, я не могу выполнить это действие.")
            self.start() # Запрашиваем повторный ввод

    def parse_website(self, url):

      response = requests.get(url)
      content = response.text
      
      soup = BeautifulSoup(content, 'html.parser')
      
      video_title_element = soup.select_one('h1.title')
      
      parse_website('')
      
      if video_title_element:
        title = video_title_element.text
        print(title)
      else:
        print("Title not found")

    def google_search(self, query):
            links = []
            for result in search(query, num_results=5):
                links.append(result)

            print("Вот что я нашел:")
            for link in links:
                print(link)

url = 'https://www.example.com'

parse_website(url)
central = Central()
central.start()
