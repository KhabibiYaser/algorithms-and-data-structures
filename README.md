# Лабораторная работа №2: Алгоритмы сортировки и перестановки элементов

## Цель лабораторной:
- Научиться реализовывать и применять алгоритмы сортировки, такие как сортировка вставками, пузырьковая сортировка и сортировка выбором.
- Понять принцип работы этих алгоритмов и научиться фиксировать перестановки элементов.

## Задачи лабораторной:
- Реализовать сортировку вставками и понять её принцип.
- Реализовать пузырьковую сортировку и разобраться, как она работает.
- Написать модифицированный алгоритм сортировки выбором, фиксирующий все перестановки.
- Протестировать каждую задачу с использованием заранее подготовленных тестов.

## Структура проекта `lab2`:
Каждая задача представлена в отдельной директории с исходным кодом и тестами.

### task1/ - первое задание: сортировка вставками
- `src/` — исходные коды.
- `tests/` — тесты.

### task2/ - второе задание: пузырьковая сортировка
- `src/` — исходные коды.
- `tests/` — тесты.

### task8/ - восьмое задание: фиксирование перестановок
- `src/` — исходные коды.
- `tests/` — тесты.

## Описание задач:
- **Задание 1**: Реализована сортировка вставками. На каждом шаге текущий элемент вставляется на правильное место в уже отсортированной части массива.
- **Задание 2**: Реализована пузырьковая сортировка. Элементы массива сравниваются попарно и переставляются местами, пока массив не будет отсортирован.
- **Задание 8**: Модифицированная сортировка выбором с фиксацией всех произведённых перестановок. Перестановки сохраняются и записываются в файл.

## Запуск тестов:
Тесты для каждой задачи находятся в соответствующих папках `tests`. Чтобы запустить тесты, выполните файл с тестами, и программа выведет результат проверки.