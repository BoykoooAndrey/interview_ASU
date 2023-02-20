#С клавиатуры вводится натуральное число. Найти его наибольшую цифру.
num = input("Введите число:")

def find_max(x):
    return int(max(str(x)))

print(find_max(num))




