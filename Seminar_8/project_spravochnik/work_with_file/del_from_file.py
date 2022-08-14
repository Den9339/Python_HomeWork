from logger import log


def del_contact(delete):
    path=r'project_spravochnik\export\export_table.csv'
    with open(path,'r', encoding='UTF-8') as data:
        split_list = data.read().split('\n\n')
        del_list = []
        for line in split_list:
            if delete in line:
                del_list.append(line)
        for i in range(len(del_list)):
            print(f'{i}: {del_list[i]}')
        split_list.remove(del_list[int(input("Введите индекс для удаления: "))])
        print('\nЗапись удалена!\n')
        log(delete)


    path=r'project_spravochnik\export\export_table.csv'
    with open(path,'w', encoding='UTF-8') as data:
        for line in split_list:
            data.write(line + '\n\n')