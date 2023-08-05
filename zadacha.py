def filter_strings(arr):
    new_arr = []
    for s in arr:
        if len(s) <= 3:
            new_arr.append(s)
    return new_arr

# Ввод массива строк с клавиатуры
n = int(input("Введите количество строк: "))
input_strings = []
for i in range(n):
    input_str = input(f"Введите строку {i+1}: ")
    input_strings.append(input_str)

result = filter_strings(input_strings)

print("Исходный массив строк:", input_strings)
print("Новый массив строк (длина <= 3):", result)
