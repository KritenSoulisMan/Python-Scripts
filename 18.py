import openai

# Установите ваш API ключ OpenAI
openai.api_key = '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'

# Создаем переменную для хранения предыдущего ответа
previous_response = ""

def chat_with_gpt(prompt):
    global previous_response
    # Добавляем предыдущий ответ к запросу
    prompt_with_memory = f"{previous_response} {prompt}"
    
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt_with_memory,
        max_tokens=3120,
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
    if user_input.lower() == "выход":
        break
    response = chat_with_gpt(user_input)
    print(response)
