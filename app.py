from flask import Flask, request, render_template
from googletrans import Translator

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text_to_translate = request.form['text_to_translate']
        target_language = request.form['target_language']
        translator = Translator()
        translated_text = translator.translate(text_to_translate, dest=target_language)
        return render_template('index.html', translated_text=translated_text.text)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
