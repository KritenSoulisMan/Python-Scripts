import openai
import os
import tkinter as tk

openai.api_key = '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'

previous_response = ""

chat_directory = "chat_logs"
os.makedirs(chat_directory, exist_ok=True)

def send_message():
    user_input = user_message.get()
    chat_history.insert(tk.END, "Я: " + user_input + "\n")
    response = chat_with_gpt(user_input)
    chat_history.insert(tk.END, "Бот: " + response + "\n")
    user_message.delete(0, tk.END)

def chat_with_gpt(prompt):
    global previous_response
    
    prompt_with_memory = f"{previous_response} {prompt}"
    
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt_with_memory,
        max_tokens=3000,
        temperature=0.7,
        n=1,
        stop=None
    )
    
    previous_response = response.choices[0].text.strip()
    
    return previous_response

window = tk.Tk()
window.title("ChatBot")

chat_history = tk.Text(window)
chat_history.pack()

user_message = tk.Entry(window, width=50)
user_message.pack()

send_button = tk.Button(window, text="Отправить", command=send_message)
send_button.pack()

window.mainloop()
