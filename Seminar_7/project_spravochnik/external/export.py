import view


path = r'export_table.csv'
with open(path, 'a') as data:
    data.write(view_data)
