import psutil
import time
from lab1.task6.src.task6 import bubble_sort

# Начало замера времени
t_start = time.perf_counter()

# Пример вызова функции bubble_sort
input_data = [12, 4, 56, 2, 10]
result = bubble_sort(input_data)

# Вывод результатов и замеров
print(f"Результат сортировки: {result} \n"
      "Время работы: %s секунд" % (time.perf_counter() - t_start))
print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ")


def test_bubble_sort():
    assert bubble_sort([12, 4, 56, 2, 10]) == [2, 4, 10, 12, 56], "Тест не пройден для [12, 4, 56, 2, 10]"
    assert bubble_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5], "Тест не пройден для отсортированного массива"
    assert bubble_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5], "Тест не пройден для обратного массива"
    assert bubble_sort([7, 7, 7, 7, 7]) == [7, 7, 7, 7, 7], "Тест не пройден для одинаковых элементов"
    print("Все тесты прошли успешно!")

test_bubble_sort()
