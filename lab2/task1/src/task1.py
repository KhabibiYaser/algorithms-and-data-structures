def insertion_sort(arr):
    for i in range(1, len(arr)):  # начинаем со второго элемента
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]  # сдвигаем элемент вправо
            j -= 1

        arr[j + 1] = key  # вставляем key на его место
    return arr

with open('input.txt', 'r') as infile:
    n = int(infile.readline().strip())  # Читаем количество элементов
    arr = list(map(int, infile.readline().strip().split()))  # Читаем массив

#  проверка условия

if 1 <= n <= 1000 and len(arr) == n and all(abs(x) <= 10**9 for x in arr):
    sorted_arr = insertion_sort(arr)  # Если всё в порядке, сортируем
    with open('output.txt', 'w') as outfile:
        outfile.write(' '.join(map(str, sorted_arr)))  # Записываем отсортированный массив
else:
    print("Ошибка ввода данных.")
