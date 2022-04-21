# Найти произведение ряда чисел от 1 до 10.
# Полученный результат вывести на экран(можно поискать в интернете алгоритм факториала в python).

composition = 1
for number in range(1, 11):
    composition *= number
print(composition)
