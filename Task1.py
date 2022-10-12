# 1. Представлен список чисел. 
# Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента. 
# Use comprehension.
# in
# 9
# out
# [15, 16, 2, 3, 1, 7, 5, 4, 10]
# [16, 3, 7, 10]

from random import sample

def create_list(number):
    my_list = sample(range(20), number)
    return my_list


def elements(my_list):
    length = len(my_list)
    new_list = [my_list[i] for i in range(1, length) if my_list[i] > my_list[i-1]]
    print(new_list)


my_list = create_list(int(input("n = ")))
print(my_list)
elements(my_list)
