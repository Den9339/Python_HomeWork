from data import input_data
from logger import log
import work_with_file.save_to_file as save_to_file
import work_with_file.viev_from_file as viev_from_file
import work_with_file.find_from_file as find_from_file
import work_with_file.del_from_file as del_from_file


def inside_of_program():
    while True:
        print('Список команд: \n 1 - добавить контакт \n 2 - найти контакт \n 3 - удалить контакт \n 4 - посмотреть список контактов \n 5 - завершить работу \n ')
        command = int(input('Введите номер команды: '))
        if command == 1:       
            name = input('Введите имя - ')
            surname = input('Введите фамилию - ')
            phone = input('Введите тел - ')
            comment = input('Введите описание - ')
            contact = input_data(name, surname, phone, comment)
            save_to_file.save_contact(contact)
            log(command)
        if command == 2:       
            find = input('Введите имя/фамилию/номер телефона/описание для поиска контакта: ')
            find_from_file.find_contact(find)
            log(command)
        if command == 3:       
            delete = input('Введите имя/фамилию/номер телефона/описание для удаления контакта: ')
            del_from_file.del_contact(delete)
            log(command)
        if command == 4:
            viev_from_file.read_contact()
            log(command)
        if command == 5:
            print('\nДо свидания!\n')
            log(command)
            break
    

