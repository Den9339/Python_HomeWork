import data
from view import view_data


def magic_button():
    table_data = {
        (input('Введите имя: ')), (input('Введите фамилию: ')),
        (input('Введите номе телефона: ')), (input('Введите описание: '))
        }
    data.init_data(*table_data)
    itog = data.return_data()
    view_data(text = 'Строка таблицы: ', data=itog)
