# Написать функцию, которая принимает путь к директории, путь к файлу и записывает в файл информацию обо всех
# файлах в директории (формат файла, размер, дата создания).
# Информация о файлах должна быть пронумерована, а каждый
# параметр должен быть помечен. Например, «1. Test; Расширение файла: py; Дата создания: 2019-12-12…» и т.д.

import os
from datetime import datetime

def write_directory_info_to_file(directory_path, file_path):
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            # Перебираем все файлы в указанной директории
            for index, filename in enumerate(os.listdir(directory_path), 1):
                file_full_path = os.path.join(directory_path, filename)

                if os.path.isfile(file_full_path):
                    # записываем в переменную расширение файла без точки
                    file_extension = os.path.splitext(filename)[1][1:]
                    
                    #размер
                    file_size = os.path.getsize(file_full_path)

                    #  дата создания файла
                    creation_time = os.path.getctime(file_full_path)
                    creation_date = datetime.fromtimestamp(creation_time).strftime('%Y-%m-%d %H:%M:%S')

                    file_info = (f"{index}. Имя файла: {filename}; "
                                 f"Расширение файла: {file_extension}; "
                                 f"Размер файла: {file_size} байт; "
                                 f"Дата создания: {creation_date}\n")
                    # записываем инф в файл
                    f.write(file_info)

        print(f"Information was succesfully written into {file_path}")
    
    except Exception as exp:
      print(exp) 

directory_path = "D:/Backup/Users/artur/Downloads/Anki"
file_path = 'C:/Users/artur/Desktop/Артур/python лабы/лаба5/text.txt' 
write_directory_info_to_file(directory_path, file_path)
