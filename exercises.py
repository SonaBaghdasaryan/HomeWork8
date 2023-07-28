# Напишите функцию, которая ищет json файлы в указанной
# директории и сохраняет их содержимое в виде
# одноимённых pickle файлов.

# import os
# import json
# import pickle
#
# def json_to_pickle(dir_):
#     json_files = [i for i in os.listdir(dir_) if i.endswith('.json')]
#     for json_file in json_files:
#         with (open(os.path.join(dir_, json_file), 'r', encoding='UTF - 8') as f,
#               open(os.path.join(dir_, json_file.rstrip('.json') + '.pickle'), 'wb') as f_c):
#             pickle.dump(json.load(f), f_c)
#
# if __name__ == '__main__':
#     json_to_pickle(os.getcwd())
#     with open('file2.pickle', 'rb') as f:
#         print(pickle.load(f))

# Напишите функцию, которая преобразует pickle файл
# хранящий список словарей в табличный csv файл.
# Для тестированию возьмите pickle версию файла из задачи
# 4 этого семинара.
# Функция должна извлекать ключи словаря для заголовков
# столбца из переданного файла.

# import csv
# import pickle
#
#
# def pickle_to_csv(pickle_path, result_path):
#     with (open(pickle_path, 'rb') as p,
#           open(result_path, 'w', encoding='UTF - 8', newline='') as c):
#         pkl = pickle.load(p)
#         headers = pkl[0].keys()
#         csv_writer = csv.DictWriter(c, fieldnames=headers)
#         csv_writer.writeheader()
#         csv_writer.writerows(pkl)
# pickle_to_csv('file1.pickle', 'file2.csv')