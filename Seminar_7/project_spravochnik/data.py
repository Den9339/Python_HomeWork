def init_data(name, surname, phone, comment):
    global n, s, p, c
    n = name
    s = surname
    p = phone
    c = comment

def return_data():
    global n, s, p, c
    return n, s, p, c


n = ''
s = ''
p = ''
c = ''