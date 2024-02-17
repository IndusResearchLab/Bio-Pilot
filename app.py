from flask import Flask, request, render_template
import os
from openai import OpenAI

app = Flask(__name__)

# Use an environment variable for the API key
openai_api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=openai_api_key)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/test-api', methods=['POST'])
def test_api():
    user_input = request.form['user_input']
    completion = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": user_input}
      ]
    )
    return render_template('index.html', response=completion.choices[0].message)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=True)
