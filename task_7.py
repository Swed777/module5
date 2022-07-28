print('Задача 7. Костя хочет выигрывать')
print()
# После игры в кубики Костя захотел немного изучить работу игровых автоматов,
# а заодно математику и теорию вероятностей.
# Но ему нужно с чего-то начать:
# написать программу, которая поможет выявить закономерности в комбинациях чисел на автомате.
 
# Даны три целых числа.
# Определите, сколько среди них совпадающих.
# Программа должна вывести одно из чисел:
# 3 (если все совпадают),
# 2 (если два совпадает) или 0 (если все числа различны).

first_number  = int(input('Введите 1 число: '))
second_number = int(input('Введите 2 число: '))
thrid_number  = int(input('Введите 3 число: '))
print('__________________')

coincidence = 0

if first_number == second_number == thrid_number:
  coincidence = 3
elif first_number == second_number or second_number == thrid_number or first_number == thrid_number:
    coincidence = 2
print('Совпадают', coincidence)