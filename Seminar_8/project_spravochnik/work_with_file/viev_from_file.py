from logger import log
import interface

def read_contact():
    path=r'project_spravochnik\export\export_table.csv'
    with open(path,'r', encoding='UTF-8') as data:
        data = data.read()
        print(f"\nСписок контактов: \n {data} \n")
        log(data)

