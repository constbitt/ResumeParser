from flask import Flask, render_template, request
import os
import shutil
import tempfile
from attributes_extractor.attributes_extractor import extract_attributes

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    text = None
    file_name = None
    cv_holder_name = None
    birth = None
    numbers = None
    mails = None
    links = None
    education = None
    language = 'english'

    if request.method == 'POST':
        text = request.form.get('text_input')
        file = request.files.get('file_input')
        language = request.form.get('language')
        if file:
            # Создаем временный файл для сохранения загруженного файла
            temp_dir = tempfile.gettempdir()
            temp_path = os.path.join(temp_dir, file.filename)
            file_name = file.filename
            file.save(temp_path)
            # Ваш код обработки загруженного файла

            cv_holder_name, birth, numbers, mails, links, education = extract_attributes(temp_path, language)

            # Удаление временного файла
            os.remove(temp_path)
            return render_template('index.html', text=text, file_name=temp_path, cv_holder_name=cv_holder_name, birth=birth, numbers=numbers, mails=mails, education=education, links=links)
            # os.remove(temp_path)
        else:
            return 'Oops! Wrong file!'
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
