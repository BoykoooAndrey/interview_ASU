# Пользователь последовательно вводит с клавиатуры числа в консоль. 
# Как только пользователь ввел «пустую строку» вывести на экран сумму введенных чисел и завершить работу программы.
nums = []

def request_num():
    number = input("Введите число -->")
    if number == "":
        print(sum(nums))
    else:
        nums.append(int(number))
        request_num()
request_num()


