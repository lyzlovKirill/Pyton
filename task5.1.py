#Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

f_1 = open("task5.1.txt", 'w', encoding="UTF-8")
while True:
    line = input("Введите строку ")
    if line == "":
        break
    f_1.write(line + '\n')
f_1.close()
