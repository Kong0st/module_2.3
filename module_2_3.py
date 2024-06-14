# my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
#
# # Итерируем по списку
# for num in my_list:
#     if num < 0:
#         break  # Если встретили отрицательное число, прерываем цикл
#     print(num)  # Выводим положительные числа


my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index = 0

while index < len(my_list):
    num = my_list[index]
    if num < 0:
        break
    print(num)
    index += 1  # Иначе зациклица на 1 числе
