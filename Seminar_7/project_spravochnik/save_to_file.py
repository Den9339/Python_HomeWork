def save_contact(inside_of_program):
    path=r'export_table.csv'
    with open(path,'a', encoding='UTF-8') as data:
        data.writelines(f"\n{inside_of_program[0]} : {inside_of_program[1]} : {inside_of_program[2]} : {inside_of_program[3]} \n")