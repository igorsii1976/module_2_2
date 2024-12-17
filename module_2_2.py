print()
print("Введите первое число:")
first = int(input())
print("Введите второе число:")
second = int(input())
print("Введите второе число:")
third = int(input())
print()
if first == second and first == third:
    print("Количество одинаковых чисел среди 3-х введённых:")
    print(3)
elif first == second or first == third or second == third:
    print("Количество одинаковых чисел среди 3-х введённых:")
    print(2)
else:
    print("Количество одинаковых чисел среди 3-х введённых:")
    print(0)
