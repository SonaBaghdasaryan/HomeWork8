# Напишите функцию, которая получает на вход директорию и рекурсивно
# обходит её и все вложенные директории. Результаты обхода сохраните в
# файлы json, csv и pickle.
# ○ Для дочерних объектов указывайте родительскую директорию.
# ○ Для каждого объекта укажите файл это или директория.
# ○ Для файлов сохраните его размер в байтах, а для директорий размер
# файлов в ней с учётом всех вложенных файлов и директорий.
# Соберите из созданных на уроке и в рамках домашнего задания функций
# пакет для работы с файлами разных форматов.

# import os
# import json
# import csv
# import pickle
#
# PATH = "."
# dict_list = []
#
# def get_data(path):
#     for root, dirs, files in os.walk(path):
#         data = get_objects(root, dirs, files, dict_list)
#     return data
#
#
# def get_objects(root, dirs, files, dict_list):
#     temp_dict = {}
#     temp_root = root.split('\\')[-1]
#     temp_dict["name"] = temp_root
#     temp_dict['type'] = "dir"
#     temp_dict["parent"] = root
#     temp_dict['size'] = os.path.getsize(str(root))
#     dict_list.append(temp_dict)
#     for f in files:
#         temp_dict = {}
#         temp_dict["name"] = f
#         temp_dict['type'] = "file"
#         temp_dict["parent"] = root
#         temp_dict['size'] = os.path.getsize(str(os.path.join(root, f)))
#         dict_list.append(temp_dict)
#     return dict_list
#
#
# def write_data(data):
#     with open('my_file.json', 'w', encoding="utf-8") as outfile:
#         for d in data:
#             json.dump(d, outfile, indent=1)
#
#     headers = list(data[0])
#     with open("my_file.csv", "w", encoding='utf-8') as outfile:
#         file_writer = csv.DictWriter(outfile, delimiter=";", lineterminator="\r", fieldnames=headers)
#         file_writer.writeheader()
#         for d in data:
#             file_writer.writerow(d)
#
#     with open('my_file.pickle', 'wb') as f:
#         pickle.dump(data, f)
#
#
# if __name__ == '__main__':
#     data = get_data(PATH)
#     write_data(data)