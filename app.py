from flask import Flask, render_template, request, jsonify
import os
import pyperclip
import shutil
import tempfile

from attributes_extractor.attributes_extractor import extract_attributes
from utils import to_csv_format
from pdf_converter import FileConverter

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
    languages = None
    language = 'english'
    pdf_name = ''
    try:
        if request.method == 'POST':
            text = None
            file_name = None
            cv_holder_name = None
            birth = None
            numbers = None
            mails = None
            links = None
            education = None
            languages = None
            text = request.form.get('text_input')
            file = request.files.get('file_input')
            language = request.form.get('language')
            if file:
                # Создаем временный файл для сохранения загруженного файла
                temp_dir = tempfile.gettempdir()
                temp_path = os.path.join(temp_dir, file.filename)
                file.save(temp_path)
                file_name = file.filename
                # Код обработки загруженного файла
                try:
                    cv_holder_name, birth, numbers, mails, links, education, languages = extract_attributes(temp_path, language)
                except:
                    return render_template('index.html', error_message='Wrong file format!')

                # Конвертация в pdf для предпросмотра
                static_dir = os.path.join(app.root_path, 'static')
                for filename in os.listdir(static_dir):
                    file_path = os.path.join(static_dir, filename)
                    if os.path.isfile(file_path):
                        os.remove(file_path)

                file_name, file_extension = os.path.splitext(file_name)
                pdf_name = file_name + '.pdf'
                converter = FileConverter()
                pdf_path = os.path.join(static_dir, pdf_name)
                converter.convert_to_pdf(temp_path, pdf_path)

                # Удаление временного файла
                os.remove(temp_path)
    except:
        return render_template('index.html', error_message='Something went wrong!')
    return render_template('index.html', text=text, file_name=pdf_name, cv_holder_name=cv_holder_name, birth=birth,
                           numbers=numbers, mails=mails, education=education, links=links, languages=languages, error_message=None)


@app.route('/copy_data', methods=['POST'])
def copy_data():
    data = request.json
    csv_data = to_csv_format(data, delimiter='\t')
    pyperclip.copy(csv_data)
    return "Text copied to clipboard"


@app.route('/process_data', methods=['POST'])
def process_data():
    data = request.json
    csv_data = to_csv_format(data, delimiter=';')
    return jsonify({"csv_data": csv_data})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
