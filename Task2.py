# 2. Для чисел в пределах от 20 до N найти числа, кратные 20 или 21. Use comprehension.
# in
# 100
# out
# [20, 21, 40, 42, 60, 63, 80, 84, 100]

def arr(num):
    if num > 20:
        my_list = [i for i in range(20, num + 1) if i % 20 == 0 or i % 21 == 0]
        return my_list
    else:
        print("Wrong number!")


my_arr = arr(int(input("n = ")))
print(my_arr)
