from data import input_data
import save_to_file
import viev_from_file


def inside_of_program():
    while True:
        print('Список команд: \n 1 - добавить контакт \n 2 - посмотреть список контактов \n 3 - завершить работу \n ')
        command = int(input('Введите номер команды: '))
        if command == 1:       
            name = input('Введите имя - ')
            surname = input('Введите фамилию - ')
            phone = input('Введите тел - ')
            comment = input('Введите описание - ')
            contact = input_data(name, surname, phone, comment)
            save_to_file.save_contact(contact)
        if command == 2:
            viev_from_file.read_from_file()
        if command == 3:
            print('\n До свидания!\n')
            break
    

