import os
from datetime import datetime, timedelta


def is_file_old(file_path, days):
    """
    Проверяет, является ли файл старше заданного количества дней.

    :param file_path: путь к файлу
    :param days: количество дней
    :return: True, если файл старше, иначе False
    """
    if not os.path.exists(file_path):
        return False

    file_time = datetime.fromtimestamp(os.path.getmtime(file_path))
    current_time = datetime.now()
    return (current_time - file_time) > timedelta(days=days)


def delete_old_files(directory, days):
    """
    Удаляет файлы в указанной директории старше заданного количества дней.

    :param directory: путь к директории
    :param days: количество дней
    :return: список удаленных файлов
    """
    if not os.path.exists(directory):
        return None

    deleted_files = []
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path) and is_file_old(file_path, days):
            os.remove(file_path)
            deleted_files.append(filename)
    return deleted_files


def delete_old_files_wrong1(directory, days):
    """
    Неправильная реализация: удаляет все файлы, независимо от их возраста
    """
    if not os.path.exists(directory):
        return None

    deleted_files = []
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)
            deleted_files.append(filename)
    print('Deleted files:', deleted_files)
    return deleted_files


def delete_old_files_wrong2(directory, days):
    """
    Неправильная реализация: не удаляет файлы, а только составляет список
    """
    if not os.path.exists(directory):
        return False

    old_files = []
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path) and is_file_old(file_path, days):
            old_files.append(filename)
    return old_files


functions = {
    "right": delete_old_files,
    "wrong1": delete_old_files_wrong1,
    "wrong2": delete_old_files_wrong2,
}


def get_function():
    name = os.environ['FUNCTION_VERSION']
    return functions[name]
