# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

path = r'Task_05-SummaMnogochlenov\polynomial_1.txt'
with open(path, 'r') as data:
    data_1 = data.readline().split()

path = r'Task_05-SummaMnogochlenov\polynomial_2.txt'
with open(path, 'r') as data:
    data_2 = data.readline()

def file_readline_to_str(path: Path) -> str:
    with open(path, 'r') as file:
        return file.readline()

# Слим:
# #Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
# import os
# #------------------------------------------------------Читает из файла строку-----------------------------------------------------+
# def get_polinomial(path:str) ->str:
#     with open(path,'r') as reader:
#         data = reader.readline()
#         return data
# #---------------------------------------------------Ищем буквы в членах мночлена--------------------------------------------------+
# def find_letters(pol_list:list, letter_list:list):
#     for item in pol_list:
#         for char in item:
#             if char.isalpha():
#                 if not char in letter_list:
#                     letter_list.append(char)
# #---------------------------------------------------Найдем коэффициент одночлена--------------------------------------------------+
# def get_coeff(s_pol:str) -> int:
#     s_coeff = ''
#     for char in s_pol:
#         if char.isdigit():
#             s_coeff += char
#         else:
#             return int(s_coeff)
# #----------------------------------------------------Сложим многочлены------------------------------------------------------------+
# def sum_polinomials(fp_list:list[str], sp_list:list[str]) ->str:
#     letter_list = list()
#     output_str =''
#     find_letters(fp_list, letter_list)
#     find_letters(sp_list,letter_list)
    
#     for letter in letter_list: # переберем все найденные буква в одночленах
#         for first_pol in fp_list: # первый многочлен
#             for sec_pol in sp_list:# второй многочлен
#                 if first_pol.__contains__(letter) and sec_pol.__contains__(letter): # если буква совпадает
#                     if first_pol[len(first_pol)-1] == sec_pol[len(first_pol)-1]: # и степень совпадает
#                         output_str += str(get_coeff(first_pol) + get_coeff(sec_pol)) + letter + "**" + sec_pol[len(first_pol)-1]
#                         print(output_str)
#             if first_pol == '+' and output_str[len(output_str)-1] != " ":
#                 output_str += " + "
#             elif first_pol == "-" and output_str[len(output_str)-1] != " ":
#                 output_str += " - "
#     return output_str

# #-----------------------------------------------------------main()----------------------------------------------------------------+
# first_input_path = os.path.join('Folder', 'first_polinom.txt')
# sec_input_path   = os.path.join('Folder', 'sec_polinom.txt')
# res_input_path   = os.path.join('Folder', 'result_sum_polinoms.txt')

# first_polinom = get_polinomial(first_input_path)
# sec_polinom   = get_polinomial(sec_input_path)

# fp_list = first_polinom.split(' ')
# sp_list = sec_polinom.split(' ')

# result = sum_polinomials(fp_list, sp_list)

# print(f'Сумма многочлена {first_polinom} и многочлена {sec_polinom} равна {result}.')
# print('Запишем результат в файл')


# Максим:
# def get_coefficients_of_polynomial(poly: list) -> list:
#     coefficients = []
#     for i in poly:
#         if ('x' in i) and ('(' in i):
#             coefficients.append(
#                 [int(i[i.find('(')+1:i.find(')')]), int(i[0:i.find('*')])])
#         elif ('x' in i) and ('(' not in i):
#             coefficients.append([1, int(i[0:i.find('*')])])
#         elif ('x' not in i) and (i != '+') and (i != '=') and (i != '0'):
#             coefficients.append([0, int(i)])
#     return coefficients


# path1 = Path('HWfiles', 'S4Hw5_poly1.txt')
# path2 = Path('HWfiles', 'S4Hw5_poly2.txt')
# poly1 = file_readline_to_str(path1)
# poly2 = file_readline_to_str(path2)
# split_poly1 = poly1.split()
# split_poly2 = poly2.split()
# coef_list1 = get_coefficients_of_polynomial(split_poly1)
# coef_list2 = get_coefficients_of_polynomial(split_poly2)

# sum_str = str()

# for i in coef_list1:

#     for j in coef_list2:
#         if (j[0] == i[0] > 1):
#             sum_str += f'{i[1]+j[1]}*x**({i[0]}) + '
#         elif (j[0] == i[0] == 1):
#             sum_str += f'{i[1]+j[1]}*x + '
#         elif (j[0] == i[0] == 0):
#             sum_str += f'{i[1]+j[1]} + '

# sum_str = sum_str[0:len(sum_str)-2]+'= 0'