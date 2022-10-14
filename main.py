# 14. Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр.
num =input('Введите ввещественное число: ')
# разделим введённое (тип данных строка) на две части
buf = num.split(".")
cel = int(buf[0])
sum = 0
if cel < 0:
    cel = -1 * cel
# сумма чисел целой части
while (cel != 0):
    sum = sum + cel % 10
    cel = cel // 10
# сумма чисел дробной части (проверка есть ли она)
if len(buf) == 2:
    drob = int(buf[1])
    while (drob != 0):
        sum = sum + drob % 10
        drob = drob // 10
print("Сумма цифр числа равна: ", sum)

# 15. Напишите программу, которая принимает на вход число
# N и выдает набор произведений чисел от 1 до N.
N = int(input('Введите целое число N: '))
ind = 1
for i in range(1, N):
    ind = ind * i
    print(ind, end = ',')
else:
    print(ind * N)

# 16. Задайте список из n чисел последовательности $(1+\frac 1 n)^n$
# и выведите на экран их сумму.
N = int(input('Введите целое число N: '))
sum = 0
print('{', end = '')
for i in range(1, N):
    sum = sum + (1 + 1 / i) ** i
    print(f"{i}:{format((1 + 1 / i) ** i, '.2f')}", end=',')
else:
    print(f"{N}:{format((1 + 1 / N) ** N, '.2f')}")
    sum = sum + (1 + 1 / N) ** N
print(f"Сумма: {format(sum, '.2f')}")

# Доп. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в
# файле file.txt в одной строке одно число.
N = int(input('Введите целое число N: '))
from random import randint
mas = [randint(-1*N, N) for _ in range(N)]
print(mas)
data = open('file.txt', 'r')
for line in data:
    buf = line.split(" ")
    i = int(buf[0])
    j = int(buf[1])
    pr = mas[i] * mas[j]
    print(f"Произведение [{i}] и [{j}] элемент:{pr}")
data.close()

# Доп. Реализуйте алгоритм перемешивания списка.
N = int(input('Введите целое число N: '))
from random import randint
massiv = [randint(-100, 100) for _ in range(N)]
print(massiv)

mas = []
mas.append(randint(0, N-1))
for _ in range(N+1):
    number = randint(0, N-1)
    for i in range(len(mas)):
        if number in mas:
            number = randint(0, N - 1)
            i = 0
        else:
            mas.append(number)
            i = len(mas)
print(mas)
print('[', end = '')
for j in range(0, N-1):
    print(massiv[mas[j]], end=',')
else:
    print(massiv[mas[N-1]], end=']')

# Доп. Даны два массива. Надо вернуть их пересечение
mas_A = input("Введите через пробел значение первого массива: ").split()
mas_B = input("Введите через пробел значение второго массива: ").split()
mas_Rez  = []
for i in mas_A:
    for j in mas_B:
        if i == j:
            mas_Rez.append(i)
            break
print(mas_Rez)