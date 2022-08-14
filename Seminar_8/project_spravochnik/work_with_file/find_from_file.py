from logger import log


def find_contact(find):
    path=r'project_spravochnik\export\export_table.csv'
    with open(path,'r', encoding='UTF-8') as data:
        split_list = data.read().split('\n\n')
        find_list = ''
        for line in split_list:
            if find in line:
                find_list += '\n' + line + '\n'
        if find_list == '':
            print('\nНет такого контакта\n')
        else:
            print(f'\nСписок включающих "{find}" контактов: \n{find_list}')
        log(find_list)

# def find_contact(find):
#     path=r'project_spravochnik\export\export_table.csv'
#     with open(path,'r', encoding='UTF-8') as data:
#         for line in data:
#             if find in line:
#                 print(f"\nИскомый(-е) контакт(-ы): \n{line} \n")
#         if line not in data:
#             print('\nНет такого контакта \n')
#         # log(line)

# find_contact('sdf')