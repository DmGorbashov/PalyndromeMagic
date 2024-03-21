"""Найти все заклинания под условие
    Аргументы:
    - Список всех слов палиндромов и слов участвующих в палинграмах
    Возвращает:
    - Список всевозможных заклинаний.
"""


def find_magic(pali_list):
    """Тело основной функции."""
    magic_list: list = []
    words = set(pali_list)
    for word in words:
        end = len(word)
        rev_word = word[::-1]
        if end > 1:
            for i in range(end):
                if word[i:] == rev_word[:end - i] and rev_word[end - i:] in words:
                    magic_list.append((word, rev_word[end-i:]))
                if word[:i] == rev_word[end - i:] and rev_word[:end - i] in words:
                    magic_list.append((rev_word[:end-i], word))
    return magic_list
