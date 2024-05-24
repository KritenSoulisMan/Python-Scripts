import openai

# Установите ваш API ключ OpenAI
openai.api_key = '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'

def chat_with_gpt(prompt):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=3000,
        temperature=0.7,
        n=1,
        stop=None
    )
    return response.choices[0].text.strip()

# Список чатов
chats = [
    "Привет, как дела?",
    "Что нового?",
    "Какой твой любимый фильм?",
    "Какая твоя любимая книга?",
    "Какие у тебя хобби?",
    "Что ты умеешь делать?"
]

# Основной чат с ботом
def main_chat():
    while True:
        user_input = input("Введите ваш запрос: ")
        if user_input.lower() == "выход":
            break
        prompt = "Вы: " + user_input + "\nБот:"
        response = chat_with_gpt(prompt)
        print(response)

# Пример использования
print("Добро пожаловать в чат с ботом!")
print("Введите 'выход', чтобы завершить чат.")
main_chat()

def send_message():
    message = entry.get()
    chat_box.insert(tk.END, "You: " + message + "\n")
    # Отправка сообщения по сокету

def receive_message():
    while True:
        message = []
        # Получение сообщения по сокету
        chat_box.insert(tk.END, "Friend: " + message + "\n")

def start_chat():
    # Создание сокета и подключение к серверу
    threading.Thread(target=receive_message).start()

# Создание графического интерфейса с помощью Tkinter
root = tk.Tk()
root.title("Chat Application")

# Создание меню
menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Exit", command=root.quit)

# Создание окна чата
chat_box = tk.Text(root)
chat_box.pack()

# Создание поля ввода и кнопки отправки
entry = tk.Entry(root)
entry.pack()

send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack()

# Запуск чата
start_chat()

# Запуск графического интерфейса
root.mainloop()

