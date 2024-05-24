import tkinter as tk
import openai
import os

# Установите ваш API ключ OpenAI
openai.api_key = 'YOUR_API_KEY'

# Создаем переменную для хранения предыдущего ответа
previous_response = ""

# Создаем директорию для сохранения чата
chat_directory = "chat_logs"
os.makedirs(chat_directory, exist_ok=True)

def chat_with_gpt(prompt):
    global previous_response
    # Добавляем предыдущий ответ к запросу
    prompt_with_memory = f"{previous_response} {prompt}"
    
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt_with_memory,
        max_tokens=100,
        temperature=0.7,
        n=1,
        stop=None
    )
    
    # Обновляем значение предыдущего ответа
    previous_response = response.choices[0].text.strip()
    
    return previous_response

# Пример использования
while True:
    user_input = input("Введите ваш запрос: ")
    
    # Проверяем, если пользователь вводит команду для начала нового чата
    if user_input.lower() == "/новый_чат":
        previous_response = ""
        print("Начат новый чат.")
        continue
    
    response = chat_with_gpt(user_input)
    print(response)
    
    # Сохраняем чат в файл
    with open(os.path.join(chat_directory, "chat_log.txt"), "a") as file:
        file.write(f"Пользователь: {user_input}\n")
        file.write(f"AI: {response}\n")
        file.write("\n")
