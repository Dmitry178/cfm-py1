# Console File Manager

import os
import platform
import shutil

import victory
from my_bill import my_bill

def cfm_menu():
    while True:
        print('')
        print('0 - создать директорию')
        print('1 - удалить (файл / директорию)')
        print('2 - копировать (файл / директорию)')
        print('3 - просмотр содержимого рабочей директории')
        print('4 - посмотреть только директории')
        print('5 - посмотреть только файлы')
        print('6 - просмотр информации об операционной системе')
        print('7 - создатель программы')
        print('8 - играть в викторину')
        print('9 - мой банковский счет')
        print('a - смена рабочей директории')
        print('x - выход')
        cmd = input('Введите команду: ')

        if cmd == '0':
            cfm_create_dir()
        elif cmd == '1':
            cfm_del_file()
        elif cmd == '2':
            cfm_copy_file()
        elif cmd == '3':
            cfm_workdir_content()
        elif cmd == '4':
            cfm_browse_dirs()
        elif cmd == '5':
            cfm_browse_files()
        elif cmd == '6':
            cfm_OS_info()
        elif cmd == '7':
            cfm_about()
        elif cmd == '8':
            victory.victory()
        elif cmd == '9':
            my_bill()
        elif cmd.lower() == 'a' or cmd.lower() == 'ф':
            cfm_workdir_change()
        elif cmd.lower() == 'x' or cmd.lower() == 'ч':
            break;

# создать директорию
def cfm_create_dir():
    print('')
    dir = input('Введите название новой директории: ')

    if os.path.exists(dir):
        print('Директория уже существует')
    else:
        try:
            os.mkdir(dir)
            print('Успешно')
        except:
            print('Ошибка создания директории')

    print('')
    input('Нажмите ENTER для продолжения')


# удалить (файл / директорию)
def cfm_del_file():
    print('')
    file = input('Введите название файла / директории для удаления: ')

    if os.path.exists(file):
        try:
            if os.path.isfile(file):
                os.remove(file)
            else:
                # os.rmdir(file)
                shutil.rmtree(file)
            print('Успешно')

        except:
            print('Ошибка удаления файла / директории')

    else:
        print('Файл / директория не существует')

    print('')
    input('Нажмите ENTER для продолжения')


# копировать (файл / директорию)
def cfm_copy_file():
    print('')
    file_in = input('Введите название файла / директории для копирования: ')

    if os.path.exists(file_in):
        try:
            file_out = input('Введите новое название: ')

            if os.path.isfile(file_in):
                shutil.copy(file_in, file_out)
            else:
                shutil.copytree(file_in, file_out)

            print('Успешно')

        except:
            print('Ошибка копирования файла / директории')

    else:
        print('Файл / директория не существует')

    print('')
    input('Нажмите ENTER для продолжения')


# просмотр содержимого рабочей директории
def cfm_workdir_content():
    print('')

    for file in os.listdir():
        print(file)

    print('')
    input('Нажмите ENTER для продолжения')


# посмотреть только директории
def cfm_browse_dirs():
    print('')
    print('Список директорий:')

    for dir in next(os.walk('.'), (None, None, []))[1]:
        print(dir)

    print('')
    input('Нажмите ENTER для продолжения')


# посмотреть только файлы
def cfm_browse_files():
    print('')
    print('Список файлов:')

    for file in next(os.walk('.'), (None, None, []))[2]:
        print(file)

    print('')
    input('Нажмите ENTER для продолжения')


# просмотр информации об операционной системе
def cfm_OS_info():
    print('')
    print('Информации об архитектуре:', platform.architecture())
    print('Тип машины:', platform.machine())
    print('Сетевое имя компьютера:', platform.node())
    print('Сведения о базовой платформе:', platform.platform())
    print('Сведения о выпуске системы:', platform.release())
    print('Имя операционной системы:', platform.system())
    print('')
    input('Нажмите ENTER для продолжения')


# создатель программы
def cfm_about():
    print('')
    print('Создатель программы: Дмитрий Одегов')
    print('https://github.com/Dmitry178/')
    print('')
    input('Нажмите ENTER для продолжения')


# смена рабочей директории
def cfm_workdir_change():
    print('')
    print('Текущая рабочая директория:', os.getcwd())
    dir = input('Введите новую рабочую директорию: ')

    try:
        os.chdir(dir)
        print('Успешно')

    except:
        print('Ошибка смены рабочей директории')

    print('')
    input('Нажмите ENTER для продолжения')


if __name__ == '__main__':
    cfm_menu()
