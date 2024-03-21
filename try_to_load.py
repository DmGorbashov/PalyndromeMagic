"""Выбрать способ загрузки и загрузить файл
    Аргументы:
    - Имя файла
    Возвращает:
    - Список слов из файла.
"""
import sys
import load_dict as ld


def try_to_load(file_name: str):
    """Основное тело функции."""
    extension: str = file_name[file_name.find(".")::]
    match extension:
        case ".csv":
            return ld.load_csv(file_name)
        case ".txt":
            return ld.load_txt(file_name)
        case _:
            print("Формат файла не поддерживается")
    sys.exit(404)
