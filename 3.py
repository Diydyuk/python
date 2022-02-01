print("Введите три целых числа")
a = int(input())
b = int(input())
c = int(input())
if a > b and a > c:
    print("Наибольшее число:", a)
elif b > a and b > c:
    print("Наибольшее число:", b)
else:
    print("Наибольшее число:", c)