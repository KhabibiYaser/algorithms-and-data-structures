# Задание 1: Сортировка вставками

## Условие задачи:
Реализовать алгоритм сортировки вставками для массива целых чисел. На каждом шаге алгоритм выбирает текущий элемент и вставляет его на правильную позицию в отсортированной части массива.

### Формат входного файла (`input.txt`):
- Первая строка содержит число \( n \) — количество элементов массива (1 ≤ \( n \) ≤ 1000).
- Вторая строка содержит \( n \) целых чисел, по модулю не превосходящих \( 10^9 \).

### Формат выходного файла (`output.txt`):
- Одна строка с отсортированным массивом. Числа разделены пробелом.

## Описание алгоритма:
Алгоритм сортировки вставками работает следующим образом:
1. Начинаем со второго элемента массива.
2. На каждой итерации выбираем текущий элемент и сдвигаем все элементы, которые больше его, вправо.
3. Вставляем текущий элемент на правильную позицию.

## Структура проекта:
- `src/` — исходные коды.
- `tests/` — тесты для проверки работы программы.

## Запуск тестов:
Для запуска тестов выполните файл с тестами из директории `tests`. Убедитесь, что тесты находятся в одной папке с исходным кодом.