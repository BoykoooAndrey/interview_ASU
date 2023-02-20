#Написать функцию, которая определяет количество разрядов введенного целого числа.
import math
num = 111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111

hundreads = len(str(num))//3
dozens = int(round (len(str(num))/3,0))
unit = math.ceil(len(str(num))/3)

print(f"Сотни --> {hundreads}")
print(f"Десятки --> {dozens}")
print(f"Еденицы --> {unit}")