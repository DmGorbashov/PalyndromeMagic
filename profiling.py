"""Профилирование кода программы
    Цель:
    - Выялвение бутолычных горлышек в коде программы.
"""
import cProfile
import main as mn

cProfile.run('mn.main()')
