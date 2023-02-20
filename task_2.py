#Создать массив из 20 элементов в диапазоне (случайным образом)  значений от -15 до 14 включительно. 
# Определить количество элементов по модулю больших, чем максимальный.
import random


array_nums = []
max_num = -15
count = 0
for i in range(20):
    array_nums.append(random.randint(-15, 14))
    if array_nums[i] > max_num:
        max_num = array_nums[i]
print(array_nums)
print("----------------")
print(f"Максимальное число --> {max_num}")
print("----------------")
print("Элементы большие по модулю:")
for i in range(20):
    if array_nums[i] * -1 > max_num:
        print(array_nums[i])
        count += 1
print("----------------")
print(f"Количество: {count}")
