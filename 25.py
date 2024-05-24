import tkinter as tk
from transformers import ChatGPT

# Создание экземпляра модели ChatGPT
model = ChatGPT()

# Создание графического интерфейса чата
root = tk.Tk()
root.title("Chat")
root.geometry("400x500")

# Создание текстового поле для отображения сообщений
messages = tk.Text(root)
messages.pack()

# Создание текстового поля для ввода сообщений
input_field = tk.Entry(root)
input_field.pack()

# Функция для отправки сообщений
def send_message(event):
    message = input_field.get()
    messages.insert(tk.END, "You: " + message + "\n")
    input_field.delete(0, tk.END)
    
    # Получение ответа от модели ChatGPT
    response = model.generate_response(message)
    messages.insert(tk.END, "AI: " + response + "\n")

# Привязка функции отправки сообщений к нажатию Enter
root.bind("<Return>", send_message)

# Запуск графического интерфейса чата
root.mainloop()
