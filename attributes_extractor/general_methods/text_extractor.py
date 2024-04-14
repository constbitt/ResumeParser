import os
import io
import re
from os.path import exists
from docx import Document
import docx
import pypdf
from bs4 import BeautifulSoup

class TextExtractor:

    def __init__(self, file_path):
        self.file_path = file_path

    def extract_text(self, file_path):
        if not (exists(file_path)):
            print("File not found.")
            return None
        text = ""
        try:
            file_extension = os.path.splitext(file_path)[1].lower()

            if file_extension == '.docx':
                text = self._extract_text_from_docx(file_path)
            elif file_extension == '.pdf':
                text = self._extract_text_from_pdf(file_path)
            elif file_extension == '.txt':
                text = self._extract_text_from_txt(file_path)
            elif file_extension == '.rtf' or file_extension == '.md' or file_extension == '.markdown':
                text = self._extract_text_from_rtf_md(file_path)
            elif file_extension == '.html' or file_extension == '.htm':
                text = self._extract_text_from_html(file_path)
            else:
                return "format_error"
        except Exception as e:
            print("Extracting data from file went wrong")
        text = re.sub(r"[^a-zA-Zא-ת,\s@().0-9/:-]", " ", text)
        text = re.sub(r'\s+', ' ', text)
        print(text)
        return text

    def _extract_text_from_docx(self, file_path):
        text = ""
        docx_file = open(file_path, 'rb')
        document = docx_file.read()
        doc = docx.Document(io.BytesIO(document))
        for paragraph in doc.paragraphs:
            text += paragraph.text + "\n"
        docx_file.close()
        return text.strip()


    def _extract_text_from_txt(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read().strip()


    def _extract_text_from_rtf_md(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read().strip()
        return text


    def _extract_text_from_pdf(self, file_path):
        text = ""
        with open(file_path, 'rb') as file:
            reader = pypdf.PdfReader(file)
            for page_num in range(len(reader.pages)):
                page = reader.pages[page_num]
                text += page.extract_text()
        return text.strip()


    def _extract_text_from_html(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            soup = BeautifulSoup(file, 'html.parser')
            return soup.get_text().strip()




