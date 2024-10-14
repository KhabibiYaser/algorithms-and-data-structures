import psutil
import time
from lab2.task1.src.task1 import insertion_sort

# Начало замера времени
t_start = time.perf_counter()

#  вызова функции insertion_sort
input_data = [31, 41, 59, 26, 41, 58]
result = insertion_sort(input_data)  # Необходимо передать отсортированный результат тестам

# Вывод результатов и замеров
print(f"Результат сортировки: {result} \n"
      "Время работы: %s секунд" % (time.perf_counter() - t_start))
print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ")


#  тестики
def test_insertion_sort():
    assert insertion_sort([31, 41, 59, 26, 41, 58]) == [26, 31, 41, 41, 58, 59], "Тест не пройден для [31, 41, 59, 26, 41, 58]"
    assert insertion_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5], "Тест не пройден для отсортированного массива"
    assert insertion_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5], "Тест не пройден для обратного массива"
    assert insertion_sort([]) == [], "Тест не пройден для пустого массива"
    print("Все тесты прошли успешно!")

# Вызов функции тестирования
test_insertion_sort()
