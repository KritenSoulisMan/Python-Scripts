import tkinter as tk
import socket
import threading

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
