
import openai
import tkinter as tk
from tkinter import messagebox
import os

# Подключение к ChatGPT
openai.api_key = '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'

# Создание главного окна приложения
window = tk.Tk()
window.title("Chat Application")

# Создание текстового поля для отображения чата
chat_text = tk.Text(window, height=35, width=90)
chat_text.pack()

# Функция для отправки сообщения боту
def send_message():
    message = user_input.get()
    if message:
        chat_text.insert(tk.END, f"\nUser: {message}")
        bot_response = get_bot_response(message)
        chat_text.insert(tk.END, f"\nBot: {bot_response}")
        user_input.delete(0, tk.END)

# Функция для получения ответа от ChatGPT
def get_bot_response(message):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"User: {message}\nBot:",
        temperature=1,
        max_tokens=3000,
        n=1,
        stop=None
    )
    return response.choices[0].text.strip()

# Функция для сохранения чата в файл
def save_chat():
    chat = chat_text.get("1.0", tk.END)
    filename = "chat.txt"
    with open(filename, 'w') as file:
        file.write(chat)
    messagebox.showinfo("Chat Application", f"Chat saved as {filename}")

# Функция для удаления чата
def delete_chat():
    filename = "chat.txt"
    if os.path.exists(filename):
        os.remove(filename)
        messagebox.showinfo("Chat Application", f"{filename} has been deleted.")
    else:
        messagebox.showinfo("Chat Application", f"{filename} does not exist.")

# Создание поля для ввода сообщения
user_input = tk.Entry(window, width=50)
user_input.pack()

# Создание кнопки для отправки сообщения
send_button = tk.Button(window, text="Send", command=send_message)
send_button.pack()

# Создание кнопки для сохранения чата
save_button = tk.Button(window, text="Save Chat", command=save_chat)
save_button.pack()

# Создание кнопки для удаления чата
delete_button = tk.Button(window, text="Delete Chat", command=delete_chat)
delete_button.pack()

# Запуск главного цикла приложения
window.mainloop()
