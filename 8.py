import string
from transformers import pipeline


    
    

def analyze_text(text):
    if not text:
        return 0, 0, 0, 0
    words = text.split()
    num_words = len(words)
    num_chars = len(text)
    unique_words = set(words)
    num_unique_words = len(unique_words)
    avg_word_length = num_chars / num_words

    return num_words, num_chars, num_unique_words, avg_word_length

while True:
    text = input("Введите текст для анализа (или 'exit' для выхода): ")
    if text == "exit":
        break
    num_words, num_chars, num_unique_words, avg_word_length = analyze_text(text)
    print("Количество слов:", num_words)
    print("Количество символов:", num_chars)
    print("Количество уникальных слов:", num_unique_words)
    print("Средняя длина слова:", avg_word_length)
    return analyze_text(text)
        

