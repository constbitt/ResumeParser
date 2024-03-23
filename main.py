from flask import Flask, render_template, request
import os
import shutil
import tempfile
from English.InfoExtraction import extract_atributes
from English.InfoExtraction import extract_text_from_pdf

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    text = None
    file_name = None
    cv_holder_name = None
    phone_numbers = None
    emails = None
    links = None
    if request.method == 'POST':
        text = request.form.get('text_input')
        file = request.files.get('file_input')
        if file:
            # Создаем временный файл для сохранения загруженного файла
            temp_dir = tempfile.gettempdir()
            temp_path = os.path.join(temp_dir, file.filename)
            file.save(temp_path)
            file_name = file.filename
            # Ваш код обработки загруженного файла

            cv_text = extract_text_from_pdf(temp_path)
            cv_holder_name, phone_numbers, emails, links = extract_atributes(cv_text)

            # Удаление временного файла
            os.remove(temp_path)
    return render_template('index.html', text=text, file_name=file_name, cv_holder_name=cv_holder_name, phone_numbers=phone_numbers, emails=emails, links=links)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
