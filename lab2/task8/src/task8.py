def fswaps(arr):
    n = len(arr)
    swaps = []

    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # Меняем местами только, если элемент найден, и он отличается
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            swaps.append((i + 1, min_idx + 1))

    return swaps


# Чтение данных из файла input.txt
with open('input.txt', 'r') as infile:
    n = int(infile.readline().strip())  # Читаем количество элементов
    arr = list(map(int, infile.readline().strip().split()))  # Читаем массив

# Проверки
if 3 <= n <= 5000 and len(arr) == n and all(abs(x) <= 10 ** 9 for x in arr):
    # Сортируем массив с записью всех перестановок
    swaps = fswaps(arr)

    # Запись результатов в файл output.txt
    with open('output.txt', 'w') as outfile:
        for swap in swaps:
            outfile.write(f"Swap elements at indices {swap[0]} and {swap[1]}\n")
        outfile.write("No more swaps needed.\n")
else:
    print("Ошибка: входные данные не соответствуют ограничениям.")
