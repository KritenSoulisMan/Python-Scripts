from flask import Flask, render_template, request
import openai

app = Flask(__name__)
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

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['user_input']
    response = chat_with_gpt(user_input)
    return render_template('index.html', response=response)

if __name__ == '__main__':
    app.run(debug=True)
