from tkinter import *
import work_with_file.save_to_file as save_to_file
import work_with_file.viev_from_file as viev_from_file
import work_with_file.find_from_file as find_from_file
import work_with_file.del_from_file as del_from_file

# В идеале я вижу этот файл как графические ссылки на команды из файла controller, т.е. например - 
# btn = Button(window,text="Добавить контакт",command=COMMAND == 1 FROM CONTROLLER.PY)
# Не знаю можно ли по такой логике (скорее всего нет) и как построить такой графический интерфейс.

def program():
    window = Tk()
    window.title("Справочник контактов")
    window.geometry('600x400')
    
    lbl = Label(window, text="Справочник",font=(50) )
    lbl.grid(column=2, row=0) 

    btn = Button(window,text="Добавить контакт",command=save_to_file.save_contact)
    btn.grid(column=0, row=2)  
    btn = Button(window,text="Найти контакт",command=find_from_file.find_contact)
    btn.grid(column=1, row=2)  
    btn = Button(window,text="Удалить контакт",command=del_from_file.del_contact)
    btn.grid(column=2, row=2) 
    btn = Button(window,text="Посмотреть список контактов ",command=viev_from_file.read_contact)
    btn.grid(column=3, row=2) 

    btn = Button(window,text="Выход ",command=exit)
    btn.grid(column=4, row=2)  
    window.mainloop()