import os
import shutil

from my_bank_account import my_bank_account
from games import quiz

if __name__ == '__main__':

    while True:
        print()
        print(' 1. Создать папку')
        print(' 2. Удалить (файл/папку)')
        print(' 3. Копировать (файл/папку)')
        print(' 4. Просмотр содержимого рабочей директории')
        print(' 5. Сохранить содержимое рабочей директории')
        print(' 6. Посмотреть только папки')
        print(' 7. Посмотреть только файлы')
        print(' 8. Посмотреть информацию об операционной системе')
        print(' 9. Создатель программы')
        print('10. Играть в викторину')
        print('11. Мой банковский счёт')
        print('12. Смена рабочей директории')
        print('13. Выход')
        print()

        current_folder = os.getcwd()
        listdir = os.listdir(current_folder)

        choice = input('Выберите пункт меню: ')

        if choice == '1':
            try:
                folder = input('Введите имя вновь создаваемой папки: ')
                print()
                os.mkdir(folder)
            except FileExistsError:
                print('Каталог с таким именем уже существует')
        elif choice == '2':
            file_dir_del = input('Введите имя файла или папки для удаления: ')
            file_dir_path = os.path.join(current_folder, file_dir_del)
            try:
                shutil.rmtree(file_dir_path)
            except IsADirectoryError:
                os.rmdir(file_dir_path)
            except NotADirectoryError:
                os.remove(file_dir_path)
            except FileNotFoundError:
                print('Указанного файла или папки не существует')
            print()
        elif choice == '3':
            file_dir_copy_from = input('Введите имя копироемого файла или папки: ')
            file_dir_copy_to = input('Введите имя нового файла или папки: ')
            try:
                if os.path.isdir(os.path.join(current_folder, file_dir_copy_from)):
                    shutil.copytree(file_dir_copy_from, file_dir_copy_to)
                else:
                    shutil.copy2(file_dir_copy_from, file_dir_copy_to)
            except FileNotFoundError:
                print('Указанного файла или папки не существует')
        elif choice == '4':
            for item in list_dir:
                print(item)
            print()
        elif choice == '5':
            files_lst, dirs_lst = [], []
            sep = ', '
            for item in list_dir:
                if os.path.isfile(os.path.join(current_folder, item)):
                    files_lst.append(item)
                else:
                    dirs_lst.append(item)
            with open('listdir.txt', 'w') as f:
                f.write(f'files: {sep.join(files_lst)}\ndirs: {sep.join(dirs_lst)}')
        elif choice == '6':
            for item in list_dir:
                if os.path.isdir(os.path.join(current_folder, item)):
                    print(item)
        elif choice == '7':
            for item in list_dir:
                if os.path.isfile(os.path.join(current_folder, item)):
                    print(item)
        elif choice == '8':
            os_info = list(os.uname())
            print(f'Имя операционной системы: {os_info[0]}')
            print(f'Имя машины в сети: {os_info[1]}')
            print(f'Релиз операционной системы: {os_info[2]}')
            print(f'Версия операционной системы: {os_info[3]}')
            print(f'Идентификатор машины: {os_info[4]}')
        elif choice == '9':
            print('Фадеев Евгений Львович')
        elif choice == '10':
            quiz()
        elif choice == '11':
            my_bank_account()
        elif choice == '12':
            dir_ch = input('Введите название новой рабочей директории: ')
            os.chdir(dir_ch)
        elif choice == '13':
            break
        else:
            print('Неверный пункт меню')
