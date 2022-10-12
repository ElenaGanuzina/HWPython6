# 3. Написать функцию, аргументы - имена сотрудников, возвращает словарь, 
# ключи — первые буквы имён, значения — списки, содержащие имена, 
# начинающиеся с соответствующей буквы.
# in
# "Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"
# out
# {'А': ['Алина'], 'Б': ['Бибочка'], 'И': ['Иван', 'Илья'], 'М': ['Марина', 'Мария'], 'П': ['Петр', 'Петр']}


def name_dict(names):
    dictionary = {}
    for name in names:
        first = name[0]
        if first in dictionary.keys():
            dictionary[first].append(name)
        else:
            temp = [name]
            dictionary[first] = temp
    dictionary = sorted(dictionary.items(), key= lambda i: i[0])        
    return dictionary


names = list("Петя, Вася, Коля, Аня, Алла, Дима, Соня, Даша".split(", "))
print(name_dict(names))
