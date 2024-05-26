#import asyncio
import flet as ft
from converter import converter_pdf2docx


def start():
    def interface(page: ft.Page):
        page.title = "File Convertor"  # Название приложения (сверху)
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.window_width = 650  # window's width
        page.window_height = 400  # window's height

        def file_picked(e: ft.FilePickerResultEvent):
            if not e.files:  # Если файла нет, то вернуться назад
                return

            #pick_files_button.disabled = True  # Отключить кнопку при выборе файла
            #progress_ring.visible = True  # Включить кольцо ожидания
            #page.update()  # Обновить UI

            for file in e.files:
                file_path = file.path
                convert_and_show_result(file_path)

            #progress_ring.visible = False  # Выключить кольцо ожидания
            #pick_files_button.disabled = False  # Включить кнопку при выборе файла
            #page.update()  # Обновить UI

        def convert_and_show_result(file_path):
            try:
                converter_pdf2docx(file_path)  # Вызов функции ковертации
                page.snack_bar = ft.SnackBar(
                    ft.Text(value=f"Successfully converted!", color="green")  # Всплывающее сообщение об успехе операции
                )
            except Exception as err:
                page.snack_bar = ft.SnackBar(
                    ft.Text(value=f"Converting error!", color="red")  # Всплывающее сообщение об ошибке операции
                )
                raise Exception(f"Error: {err}")
            finally:
                #await asyncio.sleep(3)
                page.snack_bar.open = True  # Активация всплывающего сообщения
                page.update()

        # Создание экземпляра FilePicker
        file_picker = ft.FilePicker(on_result=file_picked)
        page.overlay.append(file_picker)

        def pick_files(e):
            # Открытие диалогового окна для выбора файлов
            file_picker.pick_files()

        # Кнопка для выбора файлов и кольцо загрузки
        progress_ring = ft.ProgressRing(visible=False)
        pick_files_button = ft.ElevatedButton("Choose one of the file", on_click=pick_files)
        page.add(
            ft.Column(
                [
                    ft.Row([pick_files_button], alignment=ft.MainAxisAlignment.CENTER),
                    ft.Row([progress_ring], alignment=ft.MainAxisAlignment.CENTER),
                ]
            )
        )
        page.update()

    # Запуск интерфейса
    ft.app(interface)
