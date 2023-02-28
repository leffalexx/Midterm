def user_interface():
       return input('Меню записной книжки: \
                    \n1. Добавить запись\
                    \n2. Найти заметку\
                    \n3. Редактировать заметку\
                    \n4. Удалить заметку\
                    \n5. Показать все заметки\
                    \n6. Показать заметки за дату\
                    \n7. Закрыть меню\
                    \n Выберите номер операции: ')


def new_note():
    note = input('Введите название: '), input('Введите текст: ')
    return note

def show_note(data):
    result ='Тема: ' + data['header'] + ' \nСодержание заметки: ' + data['body']
    print(result)

def show_error():
    print('Заметка не найдена!')

def id_input():
    return input('Введите номер заметки: ')

def confirmation():
    print('Изменения сохранены! \n')

def get_date():
     return input ('Введите дату, на которую вывести заметки: ')