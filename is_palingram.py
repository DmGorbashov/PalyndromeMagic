"""Проверка на палинграмность
    Атрибуты:
    - Слово на проверку
    - Словарь для поиска соответствий
    Возвращает:
    - True, если слово часть палинграммы
    - False, если слово не является частью палинграммы.
"""


def is_paling(word: str, dictionary: set):
    """Тело функции."""
    end = len(word)
    rev_word = word[::-1]
    if end > 1:
        for i in range(end):
            if word[i:] == rev_word[:end-i] and rev_word[end-i:] in dictionary:
                return True
            if word[:i] == rev_word[end-i:] and rev_word[:end-i] in dictionary:
                return True

    return False
