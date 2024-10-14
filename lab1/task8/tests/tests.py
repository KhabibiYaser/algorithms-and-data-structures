import psutil
import time
from lab1.task8.src.task8 import fswaps

# Начало замера времени
t_start = time.perf_counter()

input_data = [3, 1, 4, 2, 2]
swaps = fswaps(input_data)

# Вывод результатов и замеров
print(f"Результат перестановок: {swaps} \n"
      "Время работы: %s секунд" % (time.perf_counter() - t_start))
print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ")


# Функция тестирования
def test_selection_sort_with_swaps():
    assert fswaps([3, 1, 4, 2, 2]) == [(1, 2), (2, 4), (3, 5)], "Тест не пройден для [3, 1, 4, 2, 2]"

    assert fswaps([5, 3, 4, 2, 1]) == [(1, 5), (2, 4), (3, 4)], "Тест не пройден для [5, 3, 4, 2, 1]"

    assert fswaps([6, 5, 4, 3, 2, 1]) == [(1, 6), (2, 5), (3, 4)], "Тест не пройден для [6, 5, 4, 3, 2, 1]"

    assert fswaps([1, 2, 3, 4, 5]) == [], "Тест не пройден для уже отсортированного массива"


    assert fswaps([2, 2, 2, 2]) == [], "Тест не пройден для массива с одинаковыми элементами"

    print("Все тесты прошли успешно!")


test_selection_sort_with_swaps()





