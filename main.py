"""Программа для генерации заклинаний-палиндромов."""
# Standard import
import time
# 3d-party import
import try_to_load as ttl
import is_palindrome as ip
import is_palingram as ip2
import magic_finder as mf


def main():
    """Основное тело программы."""
    # Выбор пользователем словаря для поиска заклинаний
    user_choice = input("Выберете словарь для поиска заклинаний\n1. words.csv\n2. russian.txt\n")
    file_name: str = ""
    match user_choice:
        case '1':
            file_name = "words.csv"
        case '2':
            file_name = "russian.txt"
        case _:
            file_name = user_choice
    # Время начала выполнения программы
    st_time = time.time()
    # Загрузка словаря
    dictionary: set = set(ttl.try_to_load(file_name))
    assert isinstance(dictionary, object)
    print(f"Словарь загружен. Количеств слов в словаре: {len(dictionary)}")
    # Поиск палиндромов
    pali_list: list = []
    for word in dictionary:
        if len(word) > 1 and ip.is_palindrome(word):
            pali_list.append(word)
    print(f"Количество палиндромов: {len(pali_list)}\n"
          f"Потрачено времени на поиск:{time.time() - st_time}\n")
    # Поиск палинграмм
    for word in dictionary:
        if len(word) > 1 and ip2.is_paling(word, dictionary) and word not in pali_list:
            pali_list.append(word)

    # Время конца выполнения программы
    end_time = time.time()

    # Обсуждение результатов поиска
    print(f"Количество палиндромов и палинграмм: {len(pali_list)}\n"
          f"Время начала: {time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(st_time))}\n"
          f"Время окончания: {time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(end_time))}\n"
          f"Время выполнения: {end_time - st_time}")

    # Поиск заклинаний
    st_time = time.time()
    spell_list = mf.find_magic(pali_list)
    spell_list = sorted(spell_list)
    end_time = time.time()

    # Вывод заклинаний
    print(f"\nКоличество заклинаний: {len(spell_list)}\n"
          f"Время начала: {time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(st_time))}\n"
          f"Время окончания: {time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(end_time))}\n"
          f"Время выполнения: {end_time - st_time}\n\nСписок заклинаний:")
    # for spell in spell_list:
    #    print(f"{spell[0]} {spell[1]}")


if __name__ == "__main__":
    main()
