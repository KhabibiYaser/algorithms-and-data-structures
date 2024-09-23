import time

def fib_number(n):
    if 0 <= n <= 45:
        a, b = 0, 1
        for i in range(n):
            a, b = b, a + b
        return a
    else:
        print("Ты вышел за диапазон, попробуй еще раз")
        return 0


# t_start = time.perf_counter()
# file_input = open("input.txt")
# n = int(file_input.readline())
# t_start = time.perf_counter()
# num =  fib_number(n)
# print("Время работы: %s секунд" % (time.perf_counter() - t_start))
# file_output = open("output.txt", "w")
# file_output.write(str(num))
# file_output.close()