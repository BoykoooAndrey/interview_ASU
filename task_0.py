# Вводится целое число, обозначающее код символа по таблице ASCII. Определить, это код английской буквы или какой-либо иной символ.
num = int(input("Введите целое число:"))

a = ord("a")
z = ord("z")
A = ord("A")
Z = ord("Z")

if (a <= num <= z) or (A <= num <= Z):
    print('Это буква', chr(num))
else:
    print('Это символ', chr(num))
