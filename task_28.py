# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных
# чисел. Из всех арифметических операций допускаются только +1 и -1. 
# Также нельзя использовать циклы.
# *Пример:*
# 2 2
# 4 
a = int(input("Введите первое неотрицительное число "))
b = int(input("Введите второе неотрицательно число "))
def summa(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return summa(a + 1, b - 1)
    
print(summa(a,b))