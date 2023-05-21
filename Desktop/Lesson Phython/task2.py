# Задача 2: Найдите сумму цифр трехзначного числа.
# Пример:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) 


numb = int (input("Ввести трехзначное число: "))
a = numb // 100
# print(a)
b = numb // 10 % 10
# print(b)
c = numb % 10
# print(c)
result = a+b+c
print (result)

