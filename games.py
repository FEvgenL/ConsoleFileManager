import random

def quiz():
    writers = {'А.С.Пушкина': '06.06.1799',
               'Ф.И.Тютчева': '05.12.1803',
               'М.Ю.Лермонтова': '15.10.1814',
               'И.С.Тургенева': '28.10.1818',
               'Ф.М.Достоевскова': '11.11.1821',
               'Л.Н.Толстова': '09.09.1828',
               'А.П.Чехова': '29.01.1860',
               'И.А.Бунина': '10.10.1870',
               'М.А.Булгакова': '15.05.1891',
               'В.В.Маяковскова': '19.07.1893'}
    days = {'05': 'пятое', '06': 'шестое', '09': 'девятое', '10': 'десятое', '11': 'одиннадцотое', '15': 'пятнадцатое',
            '19': 'девятнадцатое', '28': 'двадцать восьмое', '29': 'двадцать девятое'}
    month = {'01': 'января', '05': 'мая', '06': 'июня', '07': 'июля', '09': 'сентября', '10': 'октября',
             '11': 'ноября', '12': 'декабря'}
    answers = 5
    yes = ['Да', 'да', 'Yes', 'yes', 'y']

    writers_lst = list(writers.keys())

    while True:
        right_answer = 0
        writers_rmd = random.sample(writers_lst, answers)
        print('Введите даты рождения следующих писателей в формате "dd.mm.yyyy"')
        for writer in writers_rmd:
            answer = input(f'Дата рождения {writer}: ')
            if answer == writers[writer]:
                right_answer += 1
            else:
                date_lst = writers[writer].split('.')
                print(f'Верный ответ: {days[date_lst[0]]} {month[date_lst[1]]} {date_lst[2]} года')
            right_answer_pct = right_answer * 100 / answers
        print('-' * 30)
        print(f'Количество правильных ответов: {right_answer}')
        print(f'Количество неправлиьных ответов: {answers - right_answer}')
        print(f'Процент правильных ответов: {right_answer_pct}')
        print(f'Процент неправильных ответов: {100 - right_answer_pct}')
        yes_or_no = input('\nХотите повторить игру? ')
        print()
        if yes_or_no in yes:
            continue
        else:
            break