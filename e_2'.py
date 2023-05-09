# exercise 2'
# запрашиваем у пользователя трехзначное число
number = input("Введите трехзначное число: ")

# вычисляем сумму цифр
sum = int(number[0]) + int(number[1]) + int(number[2])

# выводим результат на экран
print('->', sum, '(', number[0], '+', number[1], '+', number[2], ')')