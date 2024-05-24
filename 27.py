
import openai
import tkinter as tk
from tkinter import messagebox
import os

openai.api_key = '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'

window = tk.Tk()
window.title("Чат с ИИ")

chat_text = tk.Text(window, height=35, width=90)
chat_text.pack()

def send_message():
    message = user_input.get()
    if message:
        chat_text.insert(tk.END, f"\nUser: {message}")
        bot_response = get_bot_response(message)
        chat_text.insert(tk.END, f"\nBot: {bot_response}")
        user_input.delete(0, tk.END)

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

def save_chat():
    chat = chat_text.get("1.0", tk.END)
    filename = "chat.txt"
    with open(filename, 'w') as file:
        file.write(chat)
    messagebox.showinfo("Chat Application", f"Chat saved as {filename}")

def delete_chat():
    filename = "chat.txt"
    if os.path.exists(filename):
        os.remove(filename)
        messagebox.showinfo("Chat Application", f"{filename} has been deleted.")
    else:
        messagebox.showinfo("Chat Application", f"{filename} does not exist.")

def load_chat():
    filename = "chat.txt"
    chat = load_chat_from_file(filename)
    for sender, message in chat:
        chat_text.insert(tk.END, f"\n{sender}: {message}")
    if os.path.exists(filename):
        chat = []
        with open(filename, 'r') as file:
            for line in file:
                sender, message = line.strip().split(': ')
                chat.append((sender, message))
        display_chat(chat)
    else:
        messagebox.showinfo("Chat Application", f"{filename} does not exist.")


def load_chat_from_file(filename):
    chat = []
    with open(filename, 'r') as file:
        for line in file:
            data = line.strip().split(': ')
            sender = data[0]
            message = ': '.join(data[1:])
            chat.append({"sender": sender, "content": message})
    return chat

filename = "chat.txt"
chat = load_chat_from_file("C:/полный/путь/к/файлу/chat.txt")
for message in chat:
    sender = message["sender"]
    content = message["content"]
    chat_text.insert(tk.END, f"\n{sender}: {content}")


def display_chat(chat):
    chat_text.delete("1.0", tk.END)
    for sender, message in chat:
        chat_text.insert(tk.END, f"\n{sender}: {message}")

user_input = tk.Entry(window, width=50)
user_input.pack()

send_button = tk.Button(window, text="Отправить", command=send_message)
send_button.pack()

save_button = tk.Button(window, text="Сохранить чат", command=save_chat)
save_button.pack()

load_button = tk.Button(window, text="Загрузить чат", command=load_chat)
load_button.pack()

delete_button = tk.Button(window, text="Удалить чат", command=delete_chat)
delete_button.pack()

window.mainloop()
