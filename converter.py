from pdf2docx import Converter
import os


# Удалание формата и замена на другой
def replace_file_extension(file_path, new_extension=".docx"):
    base = os.path.splitext(file_path)[0]
    return f"{base}{new_extension}"


# Конвертация из PDF в DOCX
def converter_pdf2docx(file_path):
    #pdf_file = file_path  # Путь к PDF файлу
    docx_file = replace_file_extension(file_path)  # Путь куда сохранить DOCX файл

    try:
        # Convert PFD to DOCX
        cv = Converter(file_path)
        cv.convert(docx_file, multiprocessing=True, start=0, end=None)
        cv.close()
    except Exception as err:
        raise Exception(f"Error: {err}")
