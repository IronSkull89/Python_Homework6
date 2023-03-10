# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

def in_range(array, min_value, max_value):
    return [i for i, v in enumerate(array) if v >= min_value and v <= max_value]

array = map(int, input("Эллементы массива: ").split())
min_value = int(input("Минимум: "))
max_value = int(input("Максимум: "))

print(in_range(array,min_value,max_value))