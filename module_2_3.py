# my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
#
# # Итерируем по списку
# for num in my_list:
#     if num < 0:
#         break  # Если встретили отрицательное число, прерываем цикл
#     print(num)  # Выводим положительные числа


# my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
# index = 0
#
# while index < len(my_list):
#     num = my_list[index]
#     if num < 0:
#         break
#     print(num)
#     index += 1

my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index = 0

# Начинаем цикл while
while index < len(my_list):
    # Если число отрицательное, прерываем цикл
    if my_list[index] < 0:
        break
    # Если число равно нулю, пропускаем и переходим к следующему элементу списка
    elif my_list[index] == 0:
        index += 1
        continue
    # Печатаем число, если оно положительное
    print(my_list[index])
    # Переходим к следующему элементу списка
    index += 1
