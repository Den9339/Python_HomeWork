from datetime import datetime


def log(argument):
    time = datetime.today()
    path = r'project_spravochnik\log\log.csv'
    with open(path, 'a') as file:
        file.writelines('\n -----------------------------------------------------\n')
        file.writelines(f'{time} ---> {argument}\n')
        file.writelines(' -----------------------------------------------------')