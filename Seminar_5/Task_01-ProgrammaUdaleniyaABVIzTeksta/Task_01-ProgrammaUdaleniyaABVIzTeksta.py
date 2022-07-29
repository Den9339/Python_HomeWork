# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = 'Привет всем абвгдейкам, абв и пока! абв'

def del_char(text: str) -> str:
    text = list(filter(lambda text: "абв" not in text, text.split()))
    return ' '.join(text)

new_text = del_char(text)
print(new_text)

# path = r'Task_01-ProgrammaUdaleniyaABVIzTeksta\text.txt'
# with open(path, 'w') as new_textt:
#     new_textt.write(f'\n{new_text}')