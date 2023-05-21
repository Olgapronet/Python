# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# Пример:
# 385916 -> yes
# 123456 -> no

numb = int (input("Номер билета: "))

num1 = numb % 1000000 // 100000
# print(num1)
num2 = numb % 100000 // 10000
# print(num2)
num3 = numb % 10000 // 1000
# print(num3)

result1 = num1+num2+num3
# print(result1)

num4 = numb % 1000 // 100
# print(num4)
num5 = numb // 10 % 10
# print(num5)
num6 = numb % 10
# print(num6)

result2 = num4+num5+num6
# print(result2)

if((result1) == (result2)):
        print ("Yes")
else:
        print ("No")