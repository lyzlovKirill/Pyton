#Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их
#деление. Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

# Запрашиваем два числа
dividend = int(input("Введите делимое "))
divider = int(input("Введите делитель "))


# Функция производит деление и проверяет не введен ли 0 в качестве делителя
def division(dividend, divider):
    try:
        return dividend / divider
    except ZeroDivisionError:
        return ("Введите делитель отличный от 0")

# Выводим результат
print(division(dividend, divider))






