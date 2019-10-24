# Библиотека для создания псевдослучайных последовательностей - рандома
from random import *

# Функция, которая выбирает случайным образом id(без повторений) из non_positive_id
def select_random(list_id, cout):
    selected_id = []
    while len(selected_id) < cout:
        element = list_id[randint(0, len(list_id) - 1)]
        if not selected_id.__contains__(element):
            selected_id.append(element)
    return selected_id
