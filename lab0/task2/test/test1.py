import psutil
import time
from lab0.task2.src.fib import fib_number


# Начало замера времени
t_start = time.perf_counter()

# Вызов функции fib_number
result = fib_number(10)

# Вывод результатов и замеров
print(f"Результат вычислений: {result} \n"
    "Время работы: %s секунд" % (time.perf_counter() - t_start))
print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ")

# Функция тестирования
def test_fib_numbers():
    assert fib_number(10) == 55, "Test case failed for fib_number(10)"
    assert fib_number(5) == 5, "Test case failed for fib_number(5)"
    assert fib_number(0) == 0, "Test case failed for fib_number(0)"
    assert fib_number(1) == 1, "Test case failed for fib_number(1)"
    print("Все тесты прошли успешно!")

# Вызов функции тестирования
test_fib_numbers()