# импортируем все из get_records и selection
from get_records import *
from selection import *
from plot import *
import numpy as np
# Функция, которая создаёт два списка(positive_id, negative_id), в которых соответственно хранятся положительные
# и отрицательные ключи(id абонентов) от records
def get_sort_id(records):
    positive_id = []
    neutral_id = []
    negative_id = []
    for key in records:
        user_list = records[key]
        tariff_id_list = []
        for ul in user_list:
            tariff_id_list.append(ul.tariff_id)
        length = len(tariff_id_list)
        tariff_id_list = set(tariff_id_list)
        if length == 3:
            if len(tariff_id_list) > 1 and ul.MNP_out == 0:
                positive_id.append(key)
            elif ul.MNP_out == 0:
                neutral_id.append(key)
            else:
                negative_id.append(key)
    return positive_id, neutral_id, negative_id

def get_training_list(rec, user_id):
    user = rec[user_id]
    user_rec = []
    for u in user:
        u.get_filds_to_index()

    for p in range(user[0].get_filds_to_index()):
        param = []
        for u in range(len(user)):
            param.append( user[u].filds_to_index[p])
        user_rec += (normalise_list(param))
    return user_rec

# Функция, которая предварительно собирает данные для обучения нейронной сети
def prepearing(path):
    records = get_records(path)
    positive_id, neutral_id, negative_id = get_sort_id(records)
    castom_positive_id = select_random(positive_id, len(negative_id))
    castom_neutral_id = select_random(neutral_id, len(negative_id))
    castom_negative_id = negative_id
    training_dict = {}
    x = []
    y = []
    for iter in range(len(negative_id)):
        training_dict[castom_positive_id[iter]] = [1, 0, 0]
        training_dict[castom_neutral_id[iter]] = [0, 1, 0]
        training_dict[castom_negative_id[iter]] = [0, 0, 1]
    for rtd in training_dict:
        x.append(get_training_list(records, rtd))
        y.append(training_dict[rtd])
    return x, y

# Функция, вызываемая из get_training_list, она сравнивает значения за текущий и следующий период
def fild_calc(a, b):
    if a > b:
        return 1
    else:
        return 0


def normalise_list(my_list):
    normalised = []
    lenght = len(my_list)
    minimal = min(my_list)
    maximal = max(my_list)
    new_max = maximal - minimal
    if minimal == maximal:
        for l in range(lenght):
            normalised.append(0)
        return normalised
    else:
        for e in my_list:
            normalised.append((e - minimal)/new_max)
        return normalised