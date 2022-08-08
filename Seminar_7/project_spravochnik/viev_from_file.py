def read_from_file():
    path=r'export_table.csv'
    with open(path,'r', encoding='UTF-8') as data:
        data = data.read()
        print(f"\n Список контактов: \n {data} \n")
