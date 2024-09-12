# 1)Дан list:
#   list = [22, 3,5,2,8,2,-23, 8,23,5]
#   - знайти мін число
#   - видалити усі дублікати
#   - замінити кожне 4-те значення на 'X'


my_list = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
# print(min(my_list))
# print(list(set(my_list)))
# print(["X" if not(i+1) % 4 else item for i,item in enumerate(my_list)])
from random import choice


# вивести на екран пустий квадрат з "*" сторона якого вказана як агрумент функції
def square(a):
    for i in range(a):
        if i==0 or i==a-1:
            print("*"*a)
        else:
            print("*"+" "*(a-2)+"*")




# 3) вывести табличку множення за допомогою цикла while
def multi_table():
    size = 9
    i = 1
    while i <= size:
        j = 1
        while j <= size:
            res = i*j
            print("" if res//10 else " ", end=" ")
            print(res,end="")
            j += 1
        print()
        i +=1



while True:
    print("1) Знайти мінімульне число")
    print("2) Видалити усі дубликіти")
    print("3) Замінити кожне значення на X")
    print("4) Вивести квадрат")
    print("5) Вивести табличку множення")
    print("0) ВИХІД")

    choice = input("Зробіть свій вибір:")

    if choice == "1":
     print(min(my_list))
    elif choice == "2":
        print(list(set(my_list)))
    elif choice == "3":
        print(["X" if not (i + 1) % 4 else item for i, item in enumerate(my_list)])
    elif choice == "4":
        square(6)
    elif choice == "5":
        multi_table()
    elif choice == "0":
        break


