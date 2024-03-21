"""Загрузка файла

    Аргументы:
    - Имя файла
    Исключения:
    - IOError, если путь/имя указан/но некорректно
    Возвращает:
    - Список всех строк в CSV фале из первого столбца
    Требует:
    - import csv
    - import sys.
"""
import csv
import sys


def load_csv(file_name):
    """Загрузка словаря из CSV файла."""
    dictionary = []
    try:
        with open(file_name, newline='', encoding='UTF8') as file:
            words_list = csv.reader(file)
            for word in words_list:
                dictionary.append(word[0])
        return dictionary
    except IOError as e:
        print(f"{e}\nОшибка при открытии {file_name}.\nЗавершение выполнения")
        sys.exit(1)


def load_txt(file_name):
    """Загрузка словаря из TXT файла"""
    try:
        with open(file_name) as file:
            loaded_file = file.read().strip().split('\n')
            loaded_file = [x.lower() for x in loaded_file]
            return loaded_file
    except IOError as e:
        print(f"{e}\nОшибка при открытии {file_name}.\nЗавершение выполнения")
        sys.exit(1)
